"""
Controlador principal de la aplicación Torneo de Fútbol.

Este módulo maneja toda la lógica de negocio y conecta la vista con los modelos.
Implementa el patrón MVC para separar responsabilidades.

Autor: [Tu Nombre]
Versión: 1.0.0
Fecha: Enero 2026
"""

import sys
import csv
import os
from datetime import datetime
from PySide6.QtWidgets import (QMainWindow, QMessageBox, QTableWidgetItem,
                               QFileDialog, QColorDialog, QTreeWidgetItem)
from PySide6.QtCore import Qt, QDate, QTime
from PySide6.QtGui import QColor, QIcon, QPixmap

from views.mainwindow import Ui_MainWindow
from views.partido_en_vivo_widget import PartidoEnVivoWidget
from models.equipo import Equipo
from models.participante import Participante
from models.partido import Partido
from models.estadistica_partido import EstadisticaPartido


class MainController(QMainWindow):
    """
    Controlador principal de la aplicación.
    
    Gestiona todas las interacciones del usuario con la interfaz y coordina
    las operaciones con la base de datos a través de los modelos.
    """
    
    def __init__(self, app):
        """Inicializa el controlador y configura la interfaz."""
        super().__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Configurar tamaño de ventana
        self.resize(1200, 700)
        self.setMinimumHeight(300)
        
        # Posicionar ventana arriba y centrada horizontalmente
        self.position_window_top()
        
        # Habilitar scroll con rueda del ratón en todas las páginas
        self.ui.Stacked_Paginas.setFocusPolicy(Qt.StrongFocus)
        
        # Variables de estado
        self.equipo_seleccionado_id = None
        self.participante_seleccionado_id = None
        self.partido_seleccionado_id = None
        
        # Crear e integrar la página de Partido en Vivo
        self.partido_en_vivo_widget = PartidoEnVivoWidget(self.app)
        self.ui.Stacked_Paginas.addWidget(self.partido_en_vivo_widget)
        self.indice_partido_vivo = self.ui.Stacked_Paginas.count() - 1
        
        # Conectar botón volver del partido en vivo
        self.partido_en_vivo_widget.btn_volver.clicked.connect(
            lambda: self.ui.Stacked_Paginas.setCurrentIndex(0)
        )
        
        # Configurar conexiones de botones
        self.conectar_senales()
        
        # Cargar datos iniciales
        self.cargar_datos_iniciales()
        
        # Configurar iconos en botones
        self.configurar_iconos()
        
        # Configurar tooltips
        self.configurar_tooltips()
        
        print("✓ Controlador principal inicializado")
    
    def position_window_top(self):
        """Posiciona la ventana en la parte superior centrada horizontalmente."""
        from PySide6.QtGui import QScreen
        screen = QScreen.availableGeometry(self.screen())
        x = (screen.width() - self.width()) // 2
        y = 0  # Pegada arriba
        self.move(x, y)
    
    def cambiar_pagina(self, indice):
        """
        Cambia a la página especificada y verifica si hay notificaciones importantes.
        
        Args:
            indice (int): Índice de la página a mostrar
        """
        self.ui.Stacked_Paginas.setCurrentIndex(indice)
        
        # Al entrar a Calendario (página 3), verificar partidos sin árbitro y cargar equipos disponibles
        if indice == 3:
            # Cargar equipos disponibles según la eliminatoria seleccionada
            self.cargar_equipos_disponibles_eliminatoria()
            
            partidos = Partido.obtener_todos(solo_pendientes=True)
            sin_arbitro = [p for p in partidos if not p.arbitro_id]
            if sin_arbitro and len(sin_arbitro) >= 3:
                QMessageBox.warning(
                    self, "Atención", 
                    f"Hay {len(sin_arbitro)} partidos sin árbitro asignado.\n"
                    "Recuerda asignar árbitros antes de los partidos."
                )
    
    def conectar_senales(self):
        """Conecta todas las señales de botones con sus métodos correspondientes."""
        
        # ===== EQUIPOS =====
        self.ui.B_CrearEquipo.clicked.connect(self.crear_equipo)
        self.ui.B_EditarEquipo.clicked.connect(self.editar_equipo)
        self.ui.B_EliminarEquipo.clicked.connect(self.eliminar_equipo)
        self.ui.B_LimpiarFormEquipo.clicked.connect(self.limpiar_form_equipo)
        self.ui.B_SeleccionarColor.clicked.connect(self.seleccionar_color)
        self.ui.B_SeleccionarEmblema.clicked.connect(self.seleccionar_emblema)
        self.ui.B_VerJugadoresEquipo.clicked.connect(self.ver_jugadores_equipo)
        self.ui.Table_Equipos.itemSelectionChanged.connect(self.seleccionar_equipo)
        
        # ===== PARTICIPANTES =====
        self.ui.B_RegistrarParticipante.clicked.connect(self.registrar_participante)
        self.ui.B_EditarParticipante.clicked.connect(self.editar_participante)
        self.ui.B_EliminarParticipante.clicked.connect(self.eliminar_participante)
        self.ui.B_LimpiarFormParticipante.clicked.connect(self.limpiar_form_participante)
        self.ui.Table_Participantes.itemSelectionChanged.connect(self.seleccionar_participante)
        self.ui.Combo_FiltroParticipantes.currentTextChanged.connect(self.aplicar_filtro_participantes)
        self.ui.Combo_OrdenParticipantes.currentTextChanged.connect(self.aplicar_filtro_participantes)
        self.ui.Check_EsJugador.stateChanged.connect(self.toggle_campos_jugador)
        
        # ===== PARTIDOS =====
        self.ui.B_ProgramarPartido.clicked.connect(self.programar_partido)
        self.ui.B_EditarPartido.clicked.connect(self.editar_partido)
        self.ui.B_EliminarPartido.clicked.connect(self.eliminar_partido)
        self.ui.B_LimpiarFormPartido.clicked.connect(self.limpiar_form_partido)
        self.ui.B_ReiniciarTorneo.clicked.connect(self.reiniciar_torneo)
        self.ui.Tree_Partidos.itemSelectionChanged.connect(self.seleccionar_partido)
        self.ui.Combo_FiltroEliminatoria.currentTextChanged.connect(self.cargar_partidos)
        self.ui.Combo_Eliminatoria.currentTextChanged.connect(self.cargar_equipos_disponibles_eliminatoria)
        
        # ===== RESULTADOS =====
        self.ui.B_GuardarResultado.clicked.connect(self.guardar_resultado)
        self.ui.B_AgregarEstadisticaJugador.clicked.connect(self.agregar_estadistica_jugador)
        self.ui.B_LimpiarResultado.clicked.connect(self.limpiar_form_resultado)
        self.ui.Combo_PartidosJugados.currentTextChanged.connect(self.cargar_partido_resultado)
        
        # ===== CLASIFICACIÓN =====
        self.ui.B_GenerarSiguienteRonda.clicked.connect(self.generar_siguiente_ronda)
        self.ui.B_ActualizarClasificacion.clicked.connect(self.actualizar_clasificacion)
        self.ui.B_ExportarCSV.clicked.connect(self.exportar_csv)
        
        # ===== MENÚ =====
        self.ui.Action_Salir.triggered.connect(self.close)
        self.ui.Action_Notificaciones.triggered.connect(self.mostrar_notificaciones)
        self.ui.Action_MenuPrincipal.triggered.connect(lambda: self.ui.Stacked_Paginas.setCurrentIndex(0))
        self.ui.Action_GenerarInformes.triggered.connect(self.abrir_generador_informes)
        self.ui.Action_VerAyuda.triggered.connect(lambda: self.ui.Stacked_Paginas.setCurrentIndex(7))
        self.ui.Action_Creditos.triggered.connect(lambda: self.ui.Stacked_Paginas.setCurrentIndex(6))
        
        # ===== NAVEGACIÓN - BOTONES DEL MENÚ PRINCIPAL =====
        self.ui.B_GestionEquipos.clicked.connect(lambda: self.cambiar_pagina(1))
        self.ui.B_GestionParticipantes.clicked.connect(lambda: self.cambiar_pagina(2))
        self.ui.B_GestionCalendario.clicked.connect(lambda: self.cambiar_pagina(3))
        # Mantener la página 4 para resultados tradicionales
        self.ui.B_ActualizarResultados.clicked.connect(lambda: self.abrir_partido_en_vivo())
        self.ui.B_Clasificacion.clicked.connect(lambda: self.cambiar_pagina(5))
        self.ui.B_Creditos.clicked.connect(lambda: self.ui.Stacked_Paginas.setCurrentIndex(6))
        self.ui.B_Ayuda.clicked.connect(lambda: self.ui.Stacked_Paginas.setCurrentIndex(7))
        
        # ===== NAVEGACIÓN - BOTONES VOLVER =====
        self.ui.B_VolverDesdeEquipos.clicked.connect(lambda: self.ui.Stacked_Paginas.setCurrentIndex(0))
        self.ui.B_VolverDesdeParticipantes.clicked.connect(lambda: self.ui.Stacked_Paginas.setCurrentIndex(0))
        self.ui.B_VolverDesdeCalendario.clicked.connect(lambda: self.ui.Stacked_Paginas.setCurrentIndex(0))
        self.ui.B_VolverDesdeResultados.clicked.connect(lambda: self.ui.Stacked_Paginas.setCurrentIndex(0))
        self.ui.B_VolverDesdeClasificacion.clicked.connect(lambda: self.ui.Stacked_Paginas.setCurrentIndex(0))
        self.ui.B_VolverDesdeCreditos.clicked.connect(lambda: self.ui.Stacked_Paginas.setCurrentIndex(0))
        self.ui.B_VolverDesdeAyuda.clicked.connect(lambda: self.ui.Stacked_Paginas.setCurrentIndex(0))
        
    def cargar_datos_iniciales(self):
        """Carga todos los datos iniciales en las vistas."""
        self.cargar_equipos()
        self.cargar_participantes()
        self.cargar_partidos()
        self.cargar_combos()
        self.actualizar_clasificacion()
        
        # Establecer fecha actual en DateEdits
        self.ui.Dateedit_FechaNacimiento.setDate(QDate.currentDate())
        self.ui.Dateedit_FechaPartido.setDate(QDate.currentDate())
        self.ui.Timeedit_HoraPartido.setTime(QTime.currentTime())
    
    # ==================== GESTIÓN DE EQUIPOS ====================
    
    def crear_equipo(self):
        """Crea un nuevo equipo con los datos del formulario."""
        nombre = self.ui.Lineedit_NombreEquipo.text().strip()
        curso = self.ui.Combo_CursoEquipo.currentText()
        color = self.ui.Lineedit_ColorEquipo.text().strip()
        emblema = self.ui.Lineedit_RutaEmblema.text().strip()
        info = self.ui.Textedit_InfoEquipo.toPlainText().strip()
        
        if not nombre or not curso or not color:
            QMessageBox.warning(self, "Datos incompletos", 
                              "Por favor, complete nombre, curso y color.")
            return
        
        if Equipo.crear(nombre, curso, color, emblema, info):
            QMessageBox.information(self, "Éxito", "Equipo creado correctamente")
            self.limpiar_form_equipo()
            self.cargar_equipos()
            self.cargar_combos()
        else:
            QMessageBox.critical(self, "Error", "No se pudo crear el equipo")
    
    def editar_equipo(self):
        """Edita el equipo seleccionado."""
        if not self.equipo_seleccionado_id:
            QMessageBox.warning(self, "Sin selección", 
                              "Seleccione un equipo de la tabla")
            return
        
        nombre = self.ui.Lineedit_NombreEquipo.text().strip()
        curso = self.ui.Combo_CursoEquipo.currentText()
        color = self.ui.Lineedit_ColorEquipo.text().strip()
        emblema = self.ui.Lineedit_RutaEmblema.text().strip()
        info = self.ui.Textedit_InfoEquipo.toPlainText().strip()
        
        # Leer la imagen y convertirla a bytes si existe
        emblema_blob = None
        if emblema and os.path.exists(emblema):
            try:
                with open(emblema, 'rb') as f:
                    emblema_blob = f.read()
            except Exception as e:
                print(f"Error al leer imagen: {e}")
        else:
            # Si no hay nueva imagen, mantener la existente
            equipo_actual = Equipo.obtener_por_id(self.equipo_seleccionado_id)
            if equipo_actual:
                emblema_blob = equipo_actual.emblema_blob
        
        if Equipo.actualizar(self.equipo_seleccionado_id, nombre, curso, 
                           color, emblema, emblema_blob, info):
            QMessageBox.information(self, "Éxito", "Equipo actualizado correctamente")
            self.limpiar_form_equipo()
            self.cargar_equipos()
            self.cargar_combos()
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar el equipo")
    
    def eliminar_equipo(self):
        """Elimina el equipo seleccionado."""
        if not self.equipo_seleccionado_id:
            QMessageBox.warning(self, "Sin selección", 
                              "Seleccione un equipo de la tabla")
            return
        
        respuesta = QMessageBox.question(
            self, "Confirmar eliminación",
            "¿Está seguro de eliminar este equipo?\nSe eliminarán también sus partidos.",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            if Equipo.eliminar(self.equipo_seleccionado_id):
                QMessageBox.information(self, "Éxito", "Equipo eliminado")
                self.limpiar_form_equipo()
                self.cargar_equipos()
                self.cargar_combos()
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar el equipo")
    
    def seleccionar_equipo(self):
        """Maneja la selección de un equipo en la tabla."""
        items = self.ui.Table_Equipos.selectedItems()
        if items:
            fila = items[0].row()
            self.equipo_seleccionado_id = int(self.ui.Table_Equipos.item(fila, 0).text())
            
            # Cargar datos en el formulario
            equipo = Equipo.obtener_por_id(self.equipo_seleccionado_id)
            if equipo:
                self.ui.Lineedit_NombreEquipo.setText(equipo.nombre)
                self.ui.Combo_CursoEquipo.setCurrentText(equipo.curso)
                self.ui.Lineedit_ColorEquipo.setText(equipo.color_camiseta)
                self.ui.Lineedit_RutaEmblema.setText(equipo.emblema_path or "")
                self.ui.Textedit_InfoEquipo.setPlainText(equipo.info_adicional or "")
                
                # Mostrar vista previa del emblema desde BLOB o ruta
                if equipo.emblema_blob:
                    self.mostrar_vista_previa_emblema(equipo.emblema_blob)
                elif equipo.emblema_path:
                    self.mostrar_vista_previa_emblema(equipo.emblema_path)
                
                # Cargar jugadores del equipo en la tabla de participantes
                self.cargar_jugadores_equipo_seleccionado()
    
    def ver_jugadores_equipo(self):
        """Muestra los jugadores del equipo seleccionado."""
        if not self.equipo_seleccionado_id:
            QMessageBox.warning(self, "Sin selección", 
                              "Seleccione un equipo de la tabla")
            return
        
        jugadores = Equipo.obtener_jugadores(self.equipo_seleccionado_id)
        equipo = Equipo.obtener_por_id(self.equipo_seleccionado_id)
        
        if not jugadores:
            QMessageBox.information(self, "Sin jugadores",
                                  f"El equipo {equipo.nombre} no tiene jugadores asignados")
            return
        
        # Crear mensaje con lista de jugadores
        mensaje = f"<h3>Jugadores de {equipo.nombre}</h3><table border='1'>"
        mensaje += "<tr><th>Nombre</th><th>Posición</th><th>Goles</th><th>T.A.</th><th>T.R.</th></tr>"
        
        for j in jugadores:
            mensaje += f"<tr><td>{j['nombre']}</td><td>{j['posicion']}</td>"
            mensaje += f"<td>{j['goles']}</td><td>{j['t_amarillas']}</td><td>{j['t_rojas']}</td></tr>"
        
        mensaje += "</table>"
        
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Jugadores del Equipo")
        msg_box.setTextFormat(Qt.RichText)
        msg_box.setText(mensaje)
        msg_box.exec()
    
    def cargar_jugadores_equipo_seleccionado(self):
        """Carga los jugadores del equipo seleccionado en la tabla de participantes."""
        if not self.equipo_seleccionado_id:
            # Si no hay equipo seleccionado, cargar todos los participantes con filtros
            self.cargar_participantes()
            return
        
        # Obtener jugadores del equipo
        jugadores = Equipo.obtener_jugadores(self.equipo_seleccionado_id)
        equipo = Equipo.obtener_por_id(self.equipo_seleccionado_id)
        
        # Aplicar filtro de orden si está configurado
        orden = self.ui.Combo_OrdenParticipantes.currentText()
        if orden == "Goles":
            jugadores.sort(key=lambda x: x['goles'], reverse=True)
        elif orden == "Tarjetas Amarillas":
            jugadores.sort(key=lambda x: x['t_amarillas'], reverse=True)
        elif orden == "Tarjetas Rojas":
            jugadores.sort(key=lambda x: x['t_rojas'], reverse=True)
        else:  # Por defecto ordenar por nombre
            jugadores.sort(key=lambda x: x['nombre'])
        
        # Configurar tabla
        self.ui.Table_Participantes.setRowCount(len(jugadores))
        self.ui.Table_Participantes.setColumnCount(8)
        self.ui.Table_Participantes.setHorizontalHeaderLabels(
            ["ID", "Nombre", "Curso", "Tipo", "Posición", "Goles", "T.A.", "T.R."]
        )
        
        # Llenar tabla con jugadores
        for i, j in enumerate(jugadores):
            self.ui.Table_Participantes.setItem(i, 0, QTableWidgetItem(str(j['id'])))
            self.ui.Table_Participantes.setItem(i, 1, QTableWidgetItem(j['nombre']))
            self.ui.Table_Participantes.setItem(i, 2, QTableWidgetItem(j['curso']))
            self.ui.Table_Participantes.setItem(i, 3, QTableWidgetItem("Jugador"))
            self.ui.Table_Participantes.setItem(i, 4, QTableWidgetItem(j['posicion']))
            self.ui.Table_Participantes.setItem(i, 5, QTableWidgetItem(str(j['goles'])))
            self.ui.Table_Participantes.setItem(i, 6, QTableWidgetItem(str(j['t_amarillas'])))
            self.ui.Table_Participantes.setItem(i, 7, QTableWidgetItem(str(j['t_rojas'])))
        
        self.ui.Table_Participantes.resizeColumnsToContents()
        
        # Mostrar mensaje informativo si no hay jugadores
        if not jugadores:
            self.ui.Table_Participantes.setRowCount(1)
            item = QTableWidgetItem(f"El equipo {equipo.nombre} no tiene jugadores asignados")
            item.setForeground(QColor("gray"))
            self.ui.Table_Participantes.setItem(0, 1, item)
            self.ui.Table_Participantes.setSpan(0, 1, 1, 7)

    
    def seleccionar_color(self):
        """Abre un diálogo para seleccionar color."""
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.Lineedit_ColorEquipo.setText(color.name())
            self.ui.Lineedit_ColorEquipo.setStyleSheet(
                f"background-color: {color.name()}; color: white;"
            )
    
    def seleccionar_emblema(self):
        """Abre un diálogo para seleccionar archivo de emblema."""
        archivo, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar Emblema",
            "", "Imágenes (*.png *.jpg *.jpeg *.svg *.bmp)"
        )
        if archivo:
            self.ui.Lineedit_RutaEmblema.setText(archivo)
            self.mostrar_vista_previa_emblema(archivo)
    
    def mostrar_vista_previa_emblema(self, ruta_imagen_o_bytes):
        """Muestra una vista previa del emblema en el formulario.
        
        Args:
            ruta_imagen_o_bytes: Puede ser una ruta de archivo (str) o bytes de imagen (bytes)
        """
        pixmap = None
        
        # Si es una ruta de archivo
        if isinstance(ruta_imagen_o_bytes, str):
            if not ruta_imagen_o_bytes or not os.path.exists(ruta_imagen_o_bytes):
                if hasattr(self.ui, 'Label_VistaEmblema'):
                    self.ui.Label_VistaEmblema.clear()
                    self.ui.Label_VistaEmblema.setText("Sin imagen")
                return
            
            try:
                pixmap = QPixmap(ruta_imagen_o_bytes)
            except Exception as e:
                print(f"Error al mostrar vista previa desde archivo: {e}")
                return
        
        # Si es un BLOB (bytes)
        elif isinstance(ruta_imagen_o_bytes, (bytes, bytearray)):
            try:
                pixmap = QPixmap()
                pixmap.loadFromData(ruta_imagen_o_bytes)
            except Exception as e:
                print(f"Error al mostrar vista previa desde bytes: {e}")
                return
        
        # Mostrar el pixmap si es válido
        if pixmap and not pixmap.isNull():
            # Escalar manteniendo proporciones (máximo 100x100)
            pixmap_escalado = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            
            # Si existe un label para vista previa, usarlo
            if hasattr(self.ui, 'Label_VistaEmblema'):
                self.ui.Label_VistaEmblema.setPixmap(pixmap_escalado)
    
    def limpiar_form_equipo(self):
        """Limpia el formulario de equipos."""
        self.equipo_seleccionado_id = None
        self.ui.Lineedit_NombreEquipo.clear()
        self.ui.Combo_CursoEquipo.setCurrentIndex(0)
        self.ui.Lineedit_ColorEquipo.clear()
        self.ui.Lineedit_ColorEquipo.setStyleSheet("")
        self.ui.Lineedit_RutaEmblema.clear()
        self.ui.Textedit_InfoEquipo.clear()
    
    def cargar_equipos(self):
        """Carga todos los equipos en la tabla."""
        equipos = Equipo.obtener_todos()
        
        self.ui.Table_Equipos.setRowCount(len(equipos))
        self.ui.Table_Equipos.setColumnCount(6)
        self.ui.Table_Equipos.setHorizontalHeaderLabels(
            ["ID", "Nombre", "Curso", "Color", "Emblema", "Info"]
        )
        
        # Ajustar altura de filas para mostrar imágenes
        self.ui.Table_Equipos.verticalHeader().setDefaultSectionSize(50)
        
        for i, equipo in enumerate(equipos):
            self.ui.Table_Equipos.setItem(i, 0, QTableWidgetItem(str(equipo.id)))
            self.ui.Table_Equipos.setItem(i, 1, QTableWidgetItem(equipo.nombre))
            self.ui.Table_Equipos.setItem(i, 2, QTableWidgetItem(equipo.curso))
            self.ui.Table_Equipos.setItem(i, 3, QTableWidgetItem(equipo.color_camiseta))
            
            # Agregar emblema como icono en la tabla desde BLOB
            emblema_item = QTableWidgetItem()
            pixmap = None
            
            # Priorizar BLOB sobre ruta
            if equipo.emblema_blob:
                try:
                    pixmap = QPixmap()
                    pixmap.loadFromData(equipo.emblema_blob)
                except Exception as e:
                    print(f"Error al cargar emblema desde BLOB: {e}")
            elif equipo.emblema_path and os.path.exists(equipo.emblema_path):
                try:
                    pixmap = QPixmap(equipo.emblema_path)
                except Exception as e:
                    print(f"Error al cargar emblema desde archivo: {e}")
            
            if pixmap and not pixmap.isNull():
                icon = QIcon(pixmap)
                emblema_item.setIcon(icon)
                emblema_item.setText("")
            else:
                emblema_item.setText("Sin emblema")
            
            self.ui.Table_Equipos.setItem(i, 4, emblema_item)
            self.ui.Table_Equipos.setItem(i, 5, QTableWidgetItem(equipo.info_adicional or ""))
        
        self.ui.Table_Equipos.resizeColumnsToContents()
        # Hacer la columna de emblema un poco más ancha para ver los iconos
        self.ui.Table_Equipos.setColumnWidth(4, 100)
    
    # ==================== GESTIÓN DE PARTICIPANTES ====================
    
    def registrar_participante(self):
        """Registra un nuevo participante."""
        nombre = self.ui.Lineedit_NombreParticipante.text().strip()
        fecha_nac = self.ui.Dateedit_FechaNacimiento.date().toString("yyyy-MM-dd")
        curso = self.ui.Combo_CursoParticipante.currentText()
        es_jugador = self.ui.Check_EsJugador.isChecked()
        es_arbitro = self.ui.Check_EsArbitro.isChecked()
        posicion = self.ui.Combo_PosicionJugador.currentText() if es_jugador else ""
        
        # Obtener ID del equipo seleccionado
        equipo_id = None
        if self.ui.Combo_EquipoAsignado.currentIndex() > 0:
            equipo_texto = self.ui.Combo_EquipoAsignado.currentText()
            # Extraer ID del texto (formato: "ID - Nombre")
            if " - " in equipo_texto:
                equipo_id = int(equipo_texto.split(" - ")[0])
        
        goles = self.ui.Spin_Goles.value()
        t_amarillas = self.ui.Spin_TarjetasAmarillas.value()
        t_rojas = self.ui.Spin_TarjetasRojas.value()
        
        if not nombre or not curso:
            QMessageBox.warning(self, "Datos incompletos",
                              "Complete al menos nombre y curso")
            return
        
        if not es_jugador and not es_arbitro:
            QMessageBox.warning(self, "Tipo requerido",
                              "Debe ser jugador, árbitro o ambos")
            return
        
        if Participante.crear(nombre, fecha_nac, curso, es_jugador, es_arbitro,
                             posicion, equipo_id, goles, t_amarillas, t_rojas):
            QMessageBox.information(self, "Éxito", "Participante registrado")
            self.limpiar_form_participante()
            self.cargar_participantes()
            self.cargar_combos()
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar")
    
    def editar_participante(self):
        """Edita el participante seleccionado."""
        if not self.participante_seleccionado_id:
            QMessageBox.warning(self, "Sin selección",
                              "Seleccione un participante")
            return
        
        nombre = self.ui.Lineedit_NombreParticipante.text().strip()
        fecha_nac = self.ui.Dateedit_FechaNacimiento.date().toString("yyyy-MM-dd")
        curso = self.ui.Combo_CursoParticipante.currentText()
        es_jugador = self.ui.Check_EsJugador.isChecked()
        es_arbitro = self.ui.Check_EsArbitro.isChecked()
        posicion = self.ui.Combo_PosicionJugador.currentText() if es_jugador else ""
        
        equipo_id = None
        if self.ui.Combo_EquipoAsignado.currentIndex() > 0:
            equipo_texto = self.ui.Combo_EquipoAsignado.currentText()
            if " - " in equipo_texto:
                equipo_id = int(equipo_texto.split(" - ")[0])
        
        if Participante.actualizar(self.participante_seleccionado_id, nombre, fecha_nac,
                                  curso, es_jugador, es_arbitro, posicion, equipo_id):
            # Actualizar estadísticas si es jugador
            if es_jugador:
                goles = self.ui.Spin_Goles.value()
                t_amarillas = self.ui.Spin_TarjetasAmarillas.value()
                t_rojas = self.ui.Spin_TarjetasRojas.value()
                Participante.actualizar_estadisticas(self.participante_seleccionado_id, 
                                                    goles, t_amarillas, t_rojas, sumar=False)
            
            QMessageBox.information(self, "Éxito", "Participante actualizado")
            self.limpiar_form_participante()
            self.cargar_participantes()
            self.cargar_combos()
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar")
    
    def eliminar_participante(self):
        """Elimina el participante seleccionado."""
        if not self.participante_seleccionado_id:
            QMessageBox.warning(self, "Sin selección",
                              "Seleccione un participante")
            return
        
        respuesta = QMessageBox.question(
            self, "Confirmar eliminación",
            "¿Está seguro de eliminar este participante?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            if Participante.eliminar(self.participante_seleccionado_id):
                QMessageBox.information(self, "Éxito", "Participante eliminado")
                self.limpiar_form_participante()
                self.cargar_participantes()
                self.cargar_combos()
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar")
    
    def seleccionar_participante(self):
        """Maneja la selección de un participante en la tabla."""
        items = self.ui.Table_Participantes.selectedItems()
        if items:
            fila = items[0].row()
            self.participante_seleccionado_id = int(
                self.ui.Table_Participantes.item(fila, 0).text()
            )
            
            # Cargar datos en el formulario
            p = Participante.obtener_por_id(self.participante_seleccionado_id)
            if p:
                self.ui.Lineedit_NombreParticipante.setText(p.nombre)
                fecha = QDate.fromString(p.fecha_nacimiento, "yyyy-MM-dd")
                self.ui.Dateedit_FechaNacimiento.setDate(fecha)
                self.ui.Combo_CursoParticipante.setCurrentText(p.curso)
                self.ui.Check_EsJugador.setChecked(p.es_jugador)
                self.ui.Check_EsArbitro.setChecked(p.es_arbitro)
                self.ui.Combo_PosicionJugador.setCurrentText(p.posicion or "Portero")
                
                # Seleccionar equipo en combo
                if p.equipo_id:
                    for i in range(self.ui.Combo_EquipoAsignado.count()):
                        if self.ui.Combo_EquipoAsignado.itemText(i).startswith(str(p.equipo_id)):
                            self.ui.Combo_EquipoAsignado.setCurrentIndex(i)
                            break
                
                self.ui.Spin_Goles.setValue(p.goles)
                self.ui.Spin_TarjetasAmarillas.setValue(p.t_amarillas)
                self.ui.Spin_TarjetasRojas.setValue(p.t_rojas)
    
    def toggle_campos_jugador(self):
        """Habilita/deshabilita campos según si es jugador."""
        es_jugador = self.ui.Check_EsJugador.isChecked()
        self.ui.Combo_PosicionJugador.setEnabled(es_jugador)
        self.ui.Combo_EquipoAsignado.setEnabled(es_jugador)
    
    def limpiar_form_participante(self):
        """Limpia el formulario de participantes."""
        self.participante_seleccionado_id = None
        self.ui.Lineedit_NombreParticipante.clear()
        self.ui.Dateedit_FechaNacimiento.setDate(QDate.currentDate())
        self.ui.Combo_CursoParticipante.setCurrentIndex(0)
        self.ui.Check_EsJugador.setChecked(False)
        self.ui.Check_EsArbitro.setChecked(False)
        self.ui.Combo_PosicionJugador.setCurrentIndex(0)
        self.ui.Combo_EquipoAsignado.setCurrentIndex(0)
        self.ui.Spin_Goles.setValue(0)
        self.ui.Spin_TarjetasAmarillas.setValue(0)
        self.ui.Spin_TarjetasRojas.setValue(0)
    
    def aplicar_filtro_participantes(self):
        """Aplica los filtros de participantes y limpia la selección de equipo."""
        # Limpiar selección de equipo para que los filtros funcionen
        self.ui.Table_Equipos.clearSelection()
        self.equipo_seleccionado_id = None
        # Aplicar filtros
        self.cargar_participantes()
    
    def cargar_participantes(self):
        """Carga todos los participantes en la tabla con filtros."""
        filtro_texto = self.ui.Combo_FiltroParticipantes.currentText()
        filtro = None
        if filtro_texto == "Solo Jugadores":
            filtro = 'jugadores'
        elif filtro_texto == "Solo Árbitros":
            filtro = 'arbitros'
        
        participantes = Participante.obtener_todos(filtro)
        
        # Ordenar según selección
        orden = self.ui.Combo_OrdenParticipantes.currentText()
        if orden == "Goles":
            participantes.sort(key=lambda x: x.goles, reverse=True)
        elif orden == "Tarjetas Amarillas":
            participantes.sort(key=lambda x: x.t_amarillas, reverse=True)
        elif orden == "Tarjetas Rojas":
            participantes.sort(key=lambda x: x.t_rojas, reverse=True)
        
        self.ui.Table_Participantes.setRowCount(len(participantes))
        self.ui.Table_Participantes.setColumnCount(8)
        self.ui.Table_Participantes.setHorizontalHeaderLabels(
            ["ID", "Nombre", "Curso", "Tipo", "Posición", "Goles", "T.A.", "T.R."]
        )
        
        for i, p in enumerate(participantes):
            tipo = []
            if p.es_jugador:
                tipo.append("J")
            if p.es_arbitro:
                tipo.append("Á")
            
            self.ui.Table_Participantes.setItem(i, 0, QTableWidgetItem(str(p.id)))
            self.ui.Table_Participantes.setItem(i, 1, QTableWidgetItem(p.nombre))
            self.ui.Table_Participantes.setItem(i, 2, QTableWidgetItem(p.curso))
            self.ui.Table_Participantes.setItem(i, 3, QTableWidgetItem("/".join(tipo)))
            self.ui.Table_Participantes.setItem(i, 4, QTableWidgetItem(p.posicion or "-"))
            self.ui.Table_Participantes.setItem(i, 5, QTableWidgetItem(str(p.goles)))
            self.ui.Table_Participantes.setItem(i, 6, QTableWidgetItem(str(p.t_amarillas)))
            self.ui.Table_Participantes.setItem(i, 7, QTableWidgetItem(str(p.t_rojas)))
        
        self.ui.Table_Participantes.resizeColumnsToContents()
    
    # ==================== GESTIÓN DE CALENDARIO ====================
    
    def programar_partido(self):
        """Programa un nuevo partido."""
        # Obtener IDs de equipos desde los combos
        local_texto = self.ui.Combo_EquipoLocal.currentText()
        visitante_texto = self.ui.Combo_EquipoVisitante.currentText()
        
        if not local_texto or not visitante_texto:
            QMessageBox.warning(self, "Datos incompletos",
                              "Seleccione ambos equipos")
            return
        
        local_id = int(local_texto.split(" - ")[0])
        visitante_id = int(visitante_texto.split(" - ")[0])
        
        if local_id == visitante_id:
            QMessageBox.warning(self, "Error", 
                              "El equipo local y visitante no pueden ser el mismo")
            return
        
        eliminatoria = self.ui.Combo_Eliminatoria.currentText()
        
        # Validar que se puede crear un partido de esta eliminatoria
        if not self.validar_fase_anterior(eliminatoria):
            return
        
        fecha = self.ui.Dateedit_FechaPartido.date().toString("yyyy-MM-dd")
        hora = self.ui.Timeedit_HoraPartido.time().toString("HH:mm")
        
        arbitro_id = None
        arbitro_texto = self.ui.Combo_ArbitroPartido.currentText()
        if arbitro_texto and arbitro_texto != "Sin árbitro":
            arbitro_id = int(arbitro_texto.split(" - ")[0])
        
        lugar = self.ui.Lineedit_LugarPartido.text().strip()
        
        partido_id = Partido.crear(local_id, visitante_id, fecha, hora,
                                   arbitro_id, eliminatoria, lugar)
        
        if partido_id:
            QMessageBox.information(self, "Éxito", "Partido programado")
            self.limpiar_form_partido()
            self.cargar_partidos()
        else:
            QMessageBox.critical(self, "Error", "No se pudo programar el partido")
    
    def editar_partido(self):
        """Edita el partido seleccionado."""
        if not self.partido_seleccionado_id:
            QMessageBox.warning(self, "Sin selección",
                              "Seleccione un partido")
            return
        
        local_texto = self.ui.Combo_EquipoLocal.currentText()
        visitante_texto = self.ui.Combo_EquipoVisitante.currentText()
        
        local_id = int(local_texto.split(" - ")[0])
        visitante_id = int(visitante_texto.split(" - ")[0])
        
        if local_id == visitante_id:
            QMessageBox.warning(self, "Error", 
                              "El equipo local y visitante no pueden ser el mismo")
            return
        
        fecha = self.ui.Dateedit_FechaPartido.date().toString("yyyy-MM-dd")
        hora = self.ui.Timeedit_HoraPartido.time().toString("HH:mm")
        
        arbitro_id = None
        arbitro_texto = self.ui.Combo_ArbitroPartido.currentText()
        if arbitro_texto and arbitro_texto != "Sin árbitro":
            arbitro_id = int(arbitro_texto.split(" - ")[0])
        
        eliminatoria = self.ui.Combo_Eliminatoria.currentText()
        lugar = self.ui.Lineedit_LugarPartido.text().strip()
        
        if Partido.actualizar(self.partido_seleccionado_id, local_id, visitante_id,
                            fecha, hora, arbitro_id, eliminatoria, lugar):
            QMessageBox.information(self, "Éxito", "Partido actualizado")
            self.limpiar_form_partido()
            self.cargar_partidos()
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar")
    
    def eliminar_partido(self):
        """Elimina el partido seleccionado."""
        if not self.partido_seleccionado_id:
            QMessageBox.warning(self, "Sin selección",
                              "Seleccione un partido")
            return
        
        respuesta = QMessageBox.question(
            self, "Confirmar eliminación",
            "¿Está seguro de eliminar este partido?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            if Partido.eliminar(self.partido_seleccionado_id):
                QMessageBox.information(self, "Éxito", "Partido eliminado")
                self.limpiar_form_partido()
                self.cargar_partidos()
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar")
    
    def seleccionar_partido(self):
        """Maneja la selección de un partido en el árbol."""
        items = self.ui.Tree_Partidos.selectedItems()
        if items:
            item = items[0]
            # Obtener el ID del partido almacenado con setData
            partido_id = item.data(0, Qt.UserRole)
            
            if partido_id is not None:
                self.partido_seleccionado_id = partido_id
                # Cargar datos en formulario
                partido = Partido.obtener_por_id(self.partido_seleccionado_id)
                if partido:
                    # Seleccionar equipos en combos
                    for i in range(self.ui.Combo_EquipoLocal.count()):
                        if self.ui.Combo_EquipoLocal.itemText(i).startswith(str(partido.equipo_local_id)):
                            self.ui.Combo_EquipoLocal.setCurrentIndex(i)
                            break
                    
                    for i in range(self.ui.Combo_EquipoVisitante.count()):
                        if self.ui.Combo_EquipoVisitante.itemText(i).startswith(str(partido.equipo_visitante_id)):
                            self.ui.Combo_EquipoVisitante.setCurrentIndex(i)
                            break
                    
                    fecha = QDate.fromString(partido.fecha, "yyyy-MM-dd")
                    self.ui.Dateedit_FechaPartido.setDate(fecha)
                    
                    hora = QTime.fromString(partido.hora, "HH:mm")
                    self.ui.Timeedit_HoraPartido.setTime(hora)
                    
                    if partido.arbitro_id:
                        for i in range(self.ui.Combo_ArbitroPartido.count()):
                            if self.ui.Combo_ArbitroPartido.itemText(i).startswith(str(partido.arbitro_id)):
                                self.ui.Combo_ArbitroPartido.setCurrentIndex(i)
                                break
                    
                    self.ui.Combo_Eliminatoria.setCurrentText(partido.eliminatoria)
                    self.ui.Lineedit_LugarPartido.setText(partido.lugar or "")
    
    def validar_fase_anterior(self, eliminatoria):
        """
        Valida que todos los partidos de la fase anterior estén jugados
        antes de permitir crear partidos de la siguiente fase.
        """
        # Orden de las fases
        fases = {
            "Previa": None,
            "Dieciseisavos": "Previa",
            "Octavos": "Dieciseisavos",
            "Cuartos": "Octavos",
            "Semifinales": "Cuartos",
            "Final": "Semifinales"
        }
        
        fase_anterior = fases.get(eliminatoria)
        
        # Si no hay fase anterior, permitir
        if fase_anterior is None:
            return True
        
        # Verificar que todos los partidos de la fase anterior estén jugados
        partidos_anteriores = Partido.obtener_por_eliminatoria(fase_anterior)
        
        if not partidos_anteriores:
            QMessageBox.warning(
                self, 
                "Fase anterior incompleta",
                f"No existen partidos de {fase_anterior}.\n"
                f"Debe crear y jugar los partidos de {fase_anterior} antes de programar {eliminatoria}."
            )
            return False
        
        partidos_pendientes = [p for p in partidos_anteriores if not p.jugado]
        
        if partidos_pendientes:
            QMessageBox.warning(
                self,
                "Fase anterior incompleta",
                f"Aún hay {len(partidos_pendientes)} partido(s) de {fase_anterior} sin jugar.\n"
                f"Debe completar todos los partidos de {fase_anterior} antes de programar {eliminatoria}."
            )
            return False
        
        return True
    
    def cargar_equipos_disponibles_eliminatoria(self):
        """
        Carga solo los equipos disponibles para la eliminatoria seleccionada.
        Solo muestra equipos que ganaron en la fase anterior.
        """
        eliminatoria = self.ui.Combo_Eliminatoria.currentText()
        
        # Mapa de fase anterior
        fases_anteriores = {
            "Previa": None,
            "Dieciseisavos": "Previa",
            "Octavos": "Dieciseisavos",
            "Cuartos": "Octavos",
            "Semifinales": "Cuartos",
            "Final": "Semifinales"
        }
        
        fase_anterior = fases_anteriores.get(eliminatoria)
        
        # Si es la primera fase, mostrar todos los equipos
        if fase_anterior is None:
            equipos = Equipo.obtener_todos()
        else:
            # Obtener ganadores de la fase anterior
            equipos = self.obtener_equipos_ganadores(fase_anterior)
        
        # Actualizar combos de equipos
        self.ui.Combo_EquipoLocal.clear()
        self.ui.Combo_EquipoVisitante.clear()
        
        for equipo in equipos:
            texto = f"{equipo.id} - {equipo.nombre} ({equipo.curso})"
            self.ui.Combo_EquipoLocal.addItem(texto)
            self.ui.Combo_EquipoVisitante.addItem(texto)
    
    def obtener_equipos_ganadores(self, eliminatoria):
        """
        Obtiene los equipos que ganaron en una eliminatoria específica.
        """
        partidos = Partido.obtener_por_eliminatoria(eliminatoria)
        equipos_ganadores_ids = []
        
        for partido in partidos:
            if partido.jugado:
                # Determinar ganador
                if partido.goles_local > partido.goles_visitante:
                    equipos_ganadores_ids.append(partido.equipo_local_id)
                elif partido.goles_visitante > partido.goles_local:
                    equipos_ganadores_ids.append(partido.equipo_visitante_id)
                # En caso de empate, no se determina ganador (esto no debería pasar en eliminatorias)
        
        # Obtener objetos Equipo de los ganadores
        equipos_ganadores = []
        for equipo_id in equipos_ganadores_ids:
            equipo = Equipo.obtener_por_id(equipo_id)
            if equipo:
                equipos_ganadores.append(equipo)
        
        return equipos_ganadores
    
    def reiniciar_torneo(self):
        """
        Reinicia el torneo completo desde los octavos de final.
        Elimina todos los partidos de cuartos, semifinales y final.
        Resetea los partidos de octavos como no jugados.
        """
        respuesta = QMessageBox.question(
            self,
            "Confirmar reinicio",
            "⚠️ ¿Estás seguro de que quieres reiniciar el torneo?\n\n"
            "Esta acción:\n"
            "• Eliminará todos los partidos de Cuartos, Semifinales y Final\n"
            "• Marcará todos los partidos de Octavos como NO JUGADOS\n"
            "• Reseteará todos los resultados de Octavos\n\n"
            "Esta acción NO se puede deshacer.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if respuesta != QMessageBox.Yes:
            return
        
        from PySide6.QtSql import QSqlQuery
        
        try:
            # Eliminar partidos de cuartos, semifinales y final
            query = QSqlQuery()
            query.prepare("""
                DELETE FROM partidos 
                WHERE eliminatoria IN ('Cuartos', 'Semifinales', 'Final')
            """)
            
            if not query.exec():
                QMessageBox.critical(self, "Error", 
                                   f"Error al eliminar partidos: {query.lastError().text()}")
                return
            
            # Resetear partidos de octavos
            query.prepare("""
                UPDATE partidos 
                SET jugado = 0, goles_local = NULL, goles_visitante = NULL
                WHERE eliminatoria = 'Octavos'
            """)
            
            if not query.exec():
                QMessageBox.critical(self, "Error", 
                                   f"Error al resetear octavos: {query.lastError().text()}")
                return
            
            obtener_db().commit()
            
            # Recargar vista
            self.cargar_partidos()
            self.cargar_equipos_disponibles_eliminatoria()
            
            QMessageBox.information(
                self,
                "Torneo reiniciado",
                "✅ El torneo ha sido reiniciado correctamente.\n\n"
                "• Se han eliminado los partidos de fases posteriores\n"
                "• Los octavos de final están listos para jugarse de nuevo"
            )
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error inesperado: {str(e)}")
    
    def limpiar_form_partido(self):
        """Limpia el formulario de partidos."""
        self.partido_seleccionado_id = None
        self.ui.Combo_EquipoLocal.setCurrentIndex(0)
        self.ui.Combo_EquipoVisitante.setCurrentIndex(0)
        self.ui.Dateedit_FechaPartido.setDate(QDate.currentDate())
        self.ui.Timeedit_HoraPartido.setTime(QTime.currentTime())
        self.ui.Combo_ArbitroPartido.setCurrentIndex(0)
        self.ui.Combo_Eliminatoria.setCurrentIndex(0)
        self.ui.Lineedit_LugarPartido.clear()
    
    def cargar_partidos(self):
        """Carga todos los partidos en el árbol organizado por fecha y eliminatoria."""
        self.ui.Tree_Partidos.clear()
        
        # Configurar columnas del árbol
        self.ui.Tree_Partidos.setColumnCount(4)
        self.ui.Tree_Partidos.setHeaderLabels(["Partido / Eliminatoria", "Fecha - Hora", "Árbitro", "Lugar"])
        
        filtro = self.ui.Combo_FiltroEliminatoria.currentText()
        
        if filtro == "Todas":
            partidos = Partido.obtener_todos()
        else:
            partidos = Partido.obtener_por_eliminatoria(filtro)
        
        # Organizar por eliminatoria en orden de torneo
        orden_eliminatorias = ['Previa', 'Dieciseisavos', 'Octavos', 'Cuartos', 'Semifinales', 'Final']
        eliminatorias = {}
        
        for partido in partidos:
            if partido.eliminatoria not in eliminatorias:
                eliminatorias[partido.eliminatoria] = []
            eliminatorias[partido.eliminatoria].append(partido)
        
        # Ordenar partidos por fecha dentro de cada eliminatoria
        for elim in eliminatorias:
            eliminatorias[elim].sort(key=lambda p: (p.fecha, p.hora))
        
        # Crear estructura de árbol
        for eliminatoria in orden_eliminatorias:
            if eliminatoria not in eliminatorias:
                continue
                
            lista_partidos = eliminatorias[eliminatoria]
            
            # Nodo principal de la eliminatoria
            nodo_elim = QTreeWidgetItem(self.ui.Tree_Partidos)
            nodo_elim.setText(0, eliminatoria)
            nodo_elim.setText(1, f"{len(lista_partidos)} partidos")
            nodo_elim.setExpanded(True)
            
            # Agrupar por fechas dentro de la eliminatoria
            fechas_elim = {}
            for partido in lista_partidos:
                if partido.fecha not in fechas_elim:
                    fechas_elim[partido.fecha] = []
                fechas_elim[partido.fecha].append(partido)
            
            # Mostrar partidos agrupados por fecha
            for fecha in sorted(fechas_elim.keys()):
                partidos_fecha = fechas_elim[fecha]
                
                # Si hay varios partidos en la misma fecha, crear subnodo
                if len(partidos_fecha) > 1:
                    nodo_fecha = QTreeWidgetItem(nodo_elim)
                    nodo_fecha.setText(0, f"Fecha: {fecha}")
                    nodo_fecha.setText(1, f"{len(partidos_fecha)} partidos")
                    nodo_fecha.setExpanded(True)
                    padre = nodo_fecha
                else:
                    padre = nodo_elim
                
                # Mostrar cada partido como hijo
                for partido in partidos_fecha:
                    detalle = Partido.obtener_detalle_completo(partido.id)
                    if detalle:
                        item = QTreeWidgetItem(padre)
                        
                        # Guardar el ID del partido en el item
                        item.setData(0, Qt.UserRole, partido.id)
                        
                        # Formato del partido
                        local = detalle['equipo_local']
                        visitante = detalle['equipo_visitante']
                        
                        # Mostrar resultado si el partido ya se jugó, o indicar pendiente
                        if detalle['jugado']:
                            resultado = f"{detalle['goles_local']}-{detalle['goles_visitante']}"
                            partido_texto = f"✓ {local}  [{resultado}]  {visitante}"
                            # Color verde para partidos jugados
                            item.setForeground(0, QColor(0, 128, 0))
                        else:
                            partido_texto = f"⏳ {local}  vs  {visitante}"
                            # Color naranja para partidos pendientes
                            item.setForeground(0, QColor(255, 140, 0))
                        
                        item.setText(0, partido_texto)
                        item.setText(1, f"{detalle['fecha']} - {detalle['hora']}")
                        item.setText(2, detalle['arbitro'] or "Sin asignar")
                        item.setText(3, detalle['lugar'] or "Sin asignar")
        
        # Expandir todos los nodos para mostrar el árbol completo
        self.ui.Tree_Partidos.expandAll()
        
        # Ajustar ancho de columnas al contenido
        for i in range(4):
            self.ui.Tree_Partidos.resizeColumnToContents(i)
    
    # ==================== ACTUALIZACIÓN DE RESULTADOS ====================
    
    def cargar_partido_resultado(self):
        """Carga los datos del partido seleccionado para registrar resultado."""
        texto_partido = self.ui.Combo_PartidosJugados.currentText()
        if not texto_partido or texto_partido == "Seleccione un partido...":
            return
        
        # Extraer ID del partido
        partido_id = int(texto_partido.split(" - ")[0])
        detalle = Partido.obtener_detalle_completo(partido_id)
        
        if detalle:
            self.ui.L_NombreEquipoLocal.setText(detalle['equipo_local'])
            self.ui.L_NombreEquipoVisitante.setText(detalle['equipo_visitante'])
            self.ui.Spin_GolesLocal.setValue(detalle['goles_local'])
            self.ui.Spin_GolesVisitante.setValue(detalle['goles_visitante'])
            
            # Cargar jugadores de ambos equipos en el combo
            self.cargar_jugadores_partido(partido_id)
            
            # Cargar estadísticas ya registradas
            self.cargar_estadisticas_partido(partido_id)
    
    def cargar_jugadores_partido(self, partido_id):
        """Carga los jugadores de ambos equipos del partido."""
        self.ui.Combo_JugadoresPartido.clear()
        self.ui.Combo_JugadoresPartido.addItem("Seleccione un jugador...")
        
        partido = Partido.obtener_por_id(partido_id)
        if partido:
            # Jugadores del equipo local
            jugadores_local = Equipo.obtener_jugadores(partido.equipo_local_id)
            for j in jugadores_local:
                self.ui.Combo_JugadoresPartido.addItem(
                    f"{j['id']} - {j['nombre']} (Local)"
                )
            
            # Jugadores del equipo visitante
            jugadores_visitante = Equipo.obtener_jugadores(partido.equipo_visitante_id)
            for j in jugadores_visitante:
                self.ui.Combo_JugadoresPartido.addItem(
                    f"{j['id']} - {j['nombre']} (Visitante)"
                )
    
    def cargar_estadisticas_partido(self, partido_id):
        """Carga las estadísticas ya registradas del partido."""
        estadisticas = EstadisticaPartido.obtener_por_partido(partido_id)
        
        self.ui.Table_EstadisticasPartido.setRowCount(len(estadisticas))
        self.ui.Table_EstadisticasPartido.setColumnCount(5)
        self.ui.Table_EstadisticasPartido.setHorizontalHeaderLabels(
            ["ID Est.", "Jugador", "Goles", "T.A.", "T.R."]
        )
        
        for i, est in enumerate(estadisticas):
            self.ui.Table_EstadisticasPartido.setItem(i, 0, QTableWidgetItem(str(est['id'])))
            self.ui.Table_EstadisticasPartido.setItem(i, 1, QTableWidgetItem(est['jugador_nombre']))
            self.ui.Table_EstadisticasPartido.setItem(i, 2, QTableWidgetItem(str(est['goles'])))
            self.ui.Table_EstadisticasPartido.setItem(i, 3, QTableWidgetItem(str(est['t_amarillas'])))
            self.ui.Table_EstadisticasPartido.setItem(i, 4, QTableWidgetItem(str(est['t_rojas'])))
        
        self.ui.Table_EstadisticasPartido.resizeColumnsToContents()
    
    def agregar_estadistica_jugador(self):
        """Agrega estadísticas de un jugador al partido actual."""
        texto_jugador = self.ui.Combo_JugadoresPartido.currentText()
        if not texto_jugador or texto_jugador.startswith("Seleccione"):
            QMessageBox.warning(self, "Sin selección", "Seleccione un jugador")
            return
        
        texto_partido = self.ui.Combo_PartidosJugados.currentText()
        if not texto_partido or texto_partido.startswith("Seleccione"):
            QMessageBox.warning(self, "Sin partido", "Seleccione un partido")
            return
        
        partido_id = int(texto_partido.split(" - ")[0])
        jugador_id = int(texto_jugador.split(" - ")[0])
        
        goles = self.ui.Spin_GolesJugador.value()
        t_amarillas = self.ui.Spin_TarjetasAmarillasJugador.value()
        t_rojas = self.ui.Spin_TarjetasRojasJugador.value()
        
        if EstadisticaPartido.registrar(partido_id, jugador_id, goles, t_amarillas, t_rojas):
            QMessageBox.information(self, "Éxito", "Estadística registrada")
            self.cargar_estadisticas_partido(partido_id)
            
            # Limpiar campos
            self.ui.Spin_GolesJugador.setValue(0)
            self.ui.Spin_TarjetasAmarillasJugador.setValue(0)
            self.ui.Spin_TarjetasRojasJugador.setValue(0)
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar")
    
    def guardar_resultado(self):
        """Guarda el resultado del partido y actualiza estadísticas globales."""
        texto_partido = self.ui.Combo_PartidosJugados.currentText()
        if not texto_partido or texto_partido.startswith("Seleccione"):
            QMessageBox.warning(self, "Sin partido", "Seleccione un partido")
            return
        
        partido_id = int(texto_partido.split(" - ")[0])
        goles_local = self.ui.Spin_GolesLocal.value()
        goles_visitante = self.ui.Spin_GolesVisitante.value()
        
        # Registrar resultado del partido
        if Partido.registrar_resultado(partido_id, goles_local, goles_visitante):
            # Actualizar estadísticas globales de jugadores
            estadisticas = EstadisticaPartido.obtener_por_partido(partido_id)
            for est in estadisticas:
                Participante.actualizar_estadisticas(
                    est['jugador_id'],
                    est['goles'],
                    est['t_amarillas'],
                    est['t_rojas']
                )
            
            QMessageBox.information(self, "Éxito", 
                                  "Resultado guardado y estadísticas actualizadas")
            self.limpiar_form_resultado()
            self.cargar_partidos_jugados()
            self.actualizar_clasificacion()
        else:
            QMessageBox.critical(self, "Error", "No se pudo guardar el resultado")
    
    def limpiar_form_resultado(self):
        """Limpia el formulario de resultados."""
        self.ui.Combo_PartidosJugados.setCurrentIndex(0)
        self.ui.Spin_GolesLocal.setValue(0)
        self.ui.Spin_GolesVisitante.setValue(0)
        self.ui.Combo_JugadoresPartido.setCurrentIndex(0)
        self.ui.Spin_GolesJugador.setValue(0)
        self.ui.Spin_TarjetasAmarillasJugador.setValue(0)
        self.ui.Spin_TarjetasRojasJugador.setValue(0)
        self.ui.Table_EstadisticasPartido.setRowCount(0)
    
    def cargar_partidos_jugados(self):
        """Carga los partidos jugados en la tabla."""
        partidos = Partido.obtener_todos(solo_jugados=True)
        
        self.ui.Table_PartidosJugados.setRowCount(len(partidos))
        self.ui.Table_PartidosJugados.setColumnCount(6)
        self.ui.Table_PartidosJugados.setHorizontalHeaderLabels(
            ["Fecha", "Local", "Visitante", "Resultado", "Eliminatoria", "Árbitro"]
        )
        
        for i, partido in enumerate(partidos):
            detalle = Partido.obtener_detalle_completo(partido.id)
            if detalle:
                self.ui.Table_PartidosJugados.setItem(i, 0, QTableWidgetItem(detalle['fecha']))
                self.ui.Table_PartidosJugados.setItem(i, 1, QTableWidgetItem(detalle['equipo_local']))
                self.ui.Table_PartidosJugados.setItem(i, 2, QTableWidgetItem(detalle['equipo_visitante']))
                resultado = f"{detalle['goles_local']} - {detalle['goles_visitante']}"
                self.ui.Table_PartidosJugados.setItem(i, 3, QTableWidgetItem(resultado))
                self.ui.Table_PartidosJugados.setItem(i, 4, QTableWidgetItem(detalle['eliminatoria']))
                self.ui.Table_PartidosJugados.setItem(i, 5, QTableWidgetItem(detalle['arbitro'] or "-"))
        
        self.ui.Table_PartidosJugados.resizeColumnsToContents()
    
    # ==================== CLASIFICACIÓN Y ELIMINATORIAS ====================
    
    def actualizar_clasificacion(self):
        """Actualiza todas las tablas de clasificación."""
        self.cargar_cuadro_eliminatorias()
        self.cargar_clasificacion_equipos()
        self.cargar_goleadores()
        self.cargar_tabla_tarjetas()
    
    def cargar_cuadro_eliminatorias(self):
        """Carga el cuadro de eliminatorias en el árbol."""
        self.ui.Tree_Eliminatorias.clear()
        
        # Configurar encabezados del árbol
        self.ui.Tree_Eliminatorias.setColumnCount(4)
        self.ui.Tree_Eliminatorias.setHeaderLabels(["Fase", "Partido", "Resultado", "Ganador"])
        
        eliminatorias_orden = ['Final', 'Semifinales', 'Cuartos', 'Octavos', 
                              'Dieciseisavos', 'Previa']
        
        for eliminatoria in eliminatorias_orden:
            partidos = Partido.obtener_por_eliminatoria(eliminatoria)
            if partidos:
                grupo = QTreeWidgetItem(self.ui.Tree_Eliminatorias)
                grupo.setText(0, eliminatoria)
                
                for partido in partidos:
                    detalle = Partido.obtener_detalle_completo(partido.id)
                    if detalle:
                        item = QTreeWidgetItem(grupo)
                        partido_texto = f"{detalle['equipo_local']} vs {detalle['equipo_visitante']}"
                        item.setText(1, partido_texto)
                        
                        if detalle['jugado']:
                            resultado = f"{detalle['goles_local']} - {detalle['goles_visitante']}"
                            item.setText(2, resultado)
                            
                            # Determinar ganador
                            if detalle['goles_local'] > detalle['goles_visitante']:
                                ganador = detalle['equipo_local']
                            elif detalle['goles_visitante'] > detalle['goles_local']:
                                ganador = detalle['equipo_visitante']
                            else:
                                ganador = "Empate"
                            item.setText(3, ganador)
                        else:
                            item.setText(2, "Pendiente")
                            item.setText(3, "-")
        
        self.ui.Tree_Eliminatorias.expandAll()
        self.ui.Tree_Eliminatorias.resizeColumnToContents(0)
        self.ui.Tree_Eliminatorias.resizeColumnToContents(1)
        self.ui.Tree_Eliminatorias.resizeColumnToContents(2)
        self.ui.Tree_Eliminatorias.resizeColumnToContents(3)
    
    def cargar_clasificacion_equipos(self):
        """Carga la clasificación general de equipos basada en eliminatorias."""
        equipos = Equipo.obtener_todos()
        
        # Calcular estadísticas para cada equipo
        clasificacion = []
        for equipo in equipos:
            partidos_jugados = 0
            ganados = 0
            perdidos = 0
            goles_favor = 0
            goles_contra = 0
            
            # Obtener partidos como local
            from PySide6.QtSql import QSqlQuery
            query = QSqlQuery()
            query.prepare("""
                SELECT goles_local, goles_visitante 
                FROM partidos 
                WHERE equipo_local_id = ? AND jugado = 1
            """)
            query.addBindValue(equipo.id)
            if query.exec():
                while query.next():
                    partidos_jugados += 1
                    gl = query.value(0)
                    gv = query.value(1)
                    if gl is not None and gv is not None:
                        goles_favor += gl
                        goles_contra += gv
                        if gl > gv:
                            ganados += 1
                        else:
                            perdidos += 1
            
            # Obtener partidos como visitante
            query.prepare("""
                SELECT goles_local, goles_visitante 
                FROM partidos 
                WHERE equipo_visitante_id = ? AND jugado = 1
            """)
            query.addBindValue(equipo.id)
            if query.exec():
                while query.next():
                    partidos_jugados += 1
                    gl = query.value(0)
                    gv = query.value(1)
                    if gl is not None and gv is not None:
                        goles_favor += gv
                        goles_contra += gl
                        if gv > gl:
                            ganados += 1
                        else:
                            perdidos += 1
            
            diferencia = goles_favor - goles_contra
            
            clasificacion.append({
                'equipo': equipo.nombre,
                'pj': partidos_jugados,
                'pg': ganados,
                'pp': perdidos,
                'gf': goles_favor,
                'gc': goles_contra,
                'dif': diferencia
            })
        
        # Ordenar por victorias y diferencia de goles
        clasificacion.sort(key=lambda x: (x['pg'], x['dif'], x['gf']), reverse=True)
        
        # Mostrar en tabla
        self.ui.Table_ClasificacionEquipos.setRowCount(len(clasificacion))
        self.ui.Table_ClasificacionEquipos.setColumnCount(7)
        self.ui.Table_ClasificacionEquipos.setHorizontalHeaderLabels(
            ["Equipo", "PJ", "PG", "PP", "GF", "GC", "DIF"]
        )
        
        for i, c in enumerate(clasificacion):
            self.ui.Table_ClasificacionEquipos.setItem(i, 0, QTableWidgetItem(c['equipo']))
            self.ui.Table_ClasificacionEquipos.setItem(i, 1, QTableWidgetItem(str(c['pj'])))
            self.ui.Table_ClasificacionEquipos.setItem(i, 2, QTableWidgetItem(str(c['pg'])))
            self.ui.Table_ClasificacionEquipos.setItem(i, 3, QTableWidgetItem(str(c['pp'])))
            self.ui.Table_ClasificacionEquipos.setItem(i, 4, QTableWidgetItem(str(c['gf'])))
            self.ui.Table_ClasificacionEquipos.setItem(i, 5, QTableWidgetItem(str(c['gc'])))
            self.ui.Table_ClasificacionEquipos.setItem(i, 6, QTableWidgetItem(str(c['dif'])))
        
        self.ui.Table_ClasificacionEquipos.resizeColumnsToContents()
    
    def cargar_goleadores(self):
        """Carga la tabla de máximos goleadores."""
        goleadores = Participante.obtener_goleadores(20)
        
        self.ui.Table_Goleadores.setRowCount(len(goleadores))
        self.ui.Table_Goleadores.setColumnCount(4)
        self.ui.Table_Goleadores.setHorizontalHeaderLabels(
            ["Pos.", "Jugador", "Equipo", "Goles"]
        )
        
        for i, g in enumerate(goleadores):
            equipo = Equipo.obtener_por_id(g['equipo_id']) if g['equipo_id'] else None
            equipo_nombre = equipo.nombre if equipo else "Sin equipo"
            
            self.ui.Table_Goleadores.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.ui.Table_Goleadores.setItem(i, 1, QTableWidgetItem(g['nombre']))
            self.ui.Table_Goleadores.setItem(i, 2, QTableWidgetItem(equipo_nombre))
            self.ui.Table_Goleadores.setItem(i, 3, QTableWidgetItem(str(g['goles'])))
        
        self.ui.Table_Goleadores.resizeColumnsToContents()
    
    def cargar_tabla_tarjetas(self):
        """Carga la tabla de jugadores con más tarjetas."""
        amarillas = Participante.obtener_por_tarjetas('amarillas', 10)
        rojas = Participante.obtener_por_tarjetas('rojas', 10)
        
        # Combinar y mostrar
        datos = []
        for j in amarillas[:10]:
            equipo = Equipo.obtener_por_id(j['equipo_id']) if j['equipo_id'] else None
            datos.append({
                'nombre': j['nombre'],
                'equipo': equipo.nombre if equipo else "Sin equipo",
                't_amarillas': j['tarjetas'],
                't_rojas': 0
            })
        
        # Agregar info de rojas
        for j in rojas:
            encontrado = False
            for d in datos:
                if d['nombre'] == j['nombre']:
                    d['t_rojas'] = j['tarjetas']
                    encontrado = True
                    break
            if not encontrado and len(datos) < 20:
                equipo = Equipo.obtener_por_id(j['equipo_id']) if j['equipo_id'] else None
                datos.append({
                    'nombre': j['nombre'],
                    'equipo': equipo.nombre if equipo else "Sin equipo",
                    't_amarillas': 0,
                    't_rojas': j['tarjetas']
                })
        
        self.ui.Table_Tarjetas.setRowCount(len(datos))
        self.ui.Table_Tarjetas.setColumnCount(4)
        self.ui.Table_Tarjetas.setHorizontalHeaderLabels(
            ["Jugador", "Equipo", "T. Amarillas", "T. Rojas"]
        )
        
        for i, d in enumerate(datos):
            self.ui.Table_Tarjetas.setItem(i, 0, QTableWidgetItem(d['nombre']))
            self.ui.Table_Tarjetas.setItem(i, 1, QTableWidgetItem(d['equipo']))
            self.ui.Table_Tarjetas.setItem(i, 2, QTableWidgetItem(str(d['t_amarillas'])))
            self.ui.Table_Tarjetas.setItem(i, 3, QTableWidgetItem(str(d['t_rojas'])))
        
        self.ui.Table_Tarjetas.resizeColumnsToContents()
    
    def generar_siguiente_ronda(self):
        """Genera automáticamente la siguiente ronda de eliminatorias."""
        # Orden de eliminatorias
        orden_eliminatorias = {
            'Octavos': 'Cuartos',
            'Cuartos': 'Semifinales',
            'Semifinales': 'Final'
        }
        
        # Preguntar qué eliminatoria finalizar
        from PySide6.QtWidgets import QInputDialog
        eliminatoria_actual, ok = QInputDialog.getItem(
            self, "Generar Siguiente Ronda",
            "¿De qué eliminatoria generar ganadores?",
            list(orden_eliminatorias.keys()),
            0, False
        )
        
        if not ok:
            return
        
        # Obtener ganadores
        ganadores = Partido.obtener_ganadores_eliminatoria(eliminatoria_actual)
        
        if len(ganadores) < 2:
            QMessageBox.warning(self, "Partidos pendientes",
                              "No hay suficientes partidos finalizados en esta eliminatoria")
            return
        
        if len(ganadores) % 2 != 0:
            QMessageBox.warning(self, "Número impar",
                              "El número de ganadores debe ser par para emparejarlos")
            return
        
        siguiente_eliminatoria = orden_eliminatorias[eliminatoria_actual]
        
        # Crear partidos automáticamente
        partidos_creados = 0
        for i in range(0, len(ganadores), 2):
            if i + 1 < len(ganadores):
                Partido.crear(
                    ganadores[i],
                    ganadores[i + 1],
                    QDate.currentDate().toString("yyyy-MM-dd"),
                    "18:00",
                    None,
                    siguiente_eliminatoria,
                    "Por determinar"
                )
                partidos_creados += 1
        
        QMessageBox.information(self, "Éxito",
                              f"Se crearon {partidos_creados} partidos de {siguiente_eliminatoria}")
        self.cargar_partidos()
        self.actualizar_clasificacion()
    
    def exportar_csv(self):
        """Exporta la clasificación a un archivo CSV."""
        archivo, _ = QFileDialog.getSaveFileName(
            self, "Guardar CSV",
            f"clasificacion_{datetime.now().strftime('%Y%m%d')}.csv",
            "CSV (*.csv)"
        )
        
        if archivo:
            try:
                with open(archivo, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    
                    # Escribir clasificación de equipos
                    writer.writerow(["=== CLASIFICACIÓN DE EQUIPOS ==="])
                    writer.writerow(["Pos", "Equipo", "PJ", "PG", "PE", "PP", "GF", "GC", "DIF", "PTS"])
                    
                    for i in range(self.ui.Table_ClasificacionEquipos.rowCount()):
                        fila = [str(i + 1)]
                        for j in range(self.ui.Table_ClasificacionEquipos.columnCount()):
                            item = self.ui.Table_ClasificacionEquipos.item(i, j)
                            fila.append(item.text() if item else "")
                        writer.writerow(fila)
                    
                    writer.writerow([])
                    writer.writerow(["=== MÁXIMOS GOLEADORES ==="])
                    writer.writerow(["Pos", "Jugador", "Equipo", "Goles"])
                    
                    for i in range(self.ui.Table_Goleadores.rowCount()):
                        fila = []
                        for j in range(self.ui.Table_Goleadores.columnCount()):
                            item = self.ui.Table_Goleadores.item(i, j)
                            fila.append(item.text() if item else "")
                        writer.writerow(fila)
                
                QMessageBox.information(self, "Éxito", f"Archivo guardado:\n{archivo}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo:\n{e}")
    
    # ==================== UTILIDADES ====================
    
    def cargar_combos(self):
        """Carga todos los ComboBox con datos de la base de datos."""
        # Combos de cursos - Solo cursos con letra (A, B, C, D)
        cursos = ["1ºA", "1ºB", "1ºC", "1ºD",
                 "2ºA", "2ºB", "2ºC", "2ºD",
                 "3ºA", "3ºB", "3ºC", "3ºD",
                 "4ºA", "4ºB", "4ºC", "4ºD",
                 "1ºBachA", "1ºBachB", 
                 "2ºBachA", "2ºBachB"]
        
        self.ui.Combo_CursoEquipo.clear()
        self.ui.Combo_CursoEquipo.addItems(cursos)
        self.ui.Combo_CursoEquipo.setEditable(True)  # Permitir entrada personalizada
        
        self.ui.Combo_CursoParticipante.clear()
        self.ui.Combo_CursoParticipante.addItems(cursos)
        self.ui.Combo_CursoParticipante.setEditable(True)  # Permitir entrada personalizada
        
        # Combo de equipos
        equipos = Equipo.obtener_todos()
        self.ui.Combo_EquipoAsignado.clear()
        self.ui.Combo_EquipoAsignado.addItem("Sin equipo")
        self.ui.Combo_EquipoLocal.clear()
        self.ui.Combo_EquipoVisitante.clear()
        
        for equipo in equipos:
            texto = f"{equipo.id} - {equipo.nombre}"
            self.ui.Combo_EquipoAsignado.addItem(texto)
            self.ui.Combo_EquipoLocal.addItem(texto)
            self.ui.Combo_EquipoVisitante.addItem(texto)
        
        # Combo de árbitros
        arbitros = Participante.obtener_todos('arbitros')
        self.ui.Combo_ArbitroPartido.clear()
        self.ui.Combo_ArbitroPartido.addItem("Sin árbitro")
        
        for arbitro in arbitros:
            self.ui.Combo_ArbitroPartido.addItem(f"{arbitro.id} - {arbitro.nombre}")
        
        # Combo de partidos para resultados
        partidos_pendientes = Partido.obtener_todos(solo_pendientes=True)
        self.ui.Combo_PartidosJugados.clear()
        self.ui.Combo_PartidosJugados.addItem("Seleccione un partido...")
        
        for partido in partidos_pendientes:
            detalle = Partido.obtener_detalle_completo(partido.id)
            if detalle:
                texto = f"{detalle['id']} - {detalle['equipo_local']} vs {detalle['equipo_visitante']}"
                self.ui.Combo_PartidosJugados.addItem(texto)
    
    def configurar_tooltips(self):
        """Configura los tooltips de los elementos de la interfaz."""
        self.ui.B_CrearEquipo.setToolTip("Crear un nuevo equipo con los datos ingresados")
        self.ui.B_EditarEquipo.setToolTip("Editar el equipo seleccionado en la tabla")
        self.ui.B_EliminarEquipo.setToolTip("Eliminar el equipo seleccionado")
        self.ui.B_VerJugadoresEquipo.setToolTip("Ver la lista de jugadores del equipo")
        
        self.ui.B_RegistrarParticipante.setToolTip("Registrar un nuevo jugador o árbitro")
        self.ui.B_ProgramarPartido.setToolTip("Programar un nuevo partido")
        self.ui.B_GuardarResultado.setToolTip("Guardar el resultado del partido")
        self.ui.B_GenerarSiguienteRonda.setToolTip("Generar automáticamente la siguiente eliminatoria")
        self.ui.B_ExportarCSV.setToolTip("Exportar clasificación y estadísticas a CSV")
    
    def configurar_iconos(self):
        """
        Configura los iconos de los botones de la interfaz.
        
        Los iconos deben estar en resources/iconos/ para que se carguen correctamente.
        Si no se encuentra un icono, el botón funcionará sin él.
        """
        try:
            iconos_path = os.path.join(os.path.dirname(__file__), "..", "resources", "iconos")
            
            def set_icon(boton, nombre_archivo):
                """Helper para establecer icono si existe."""
                try:
                    ruta = os.path.join(iconos_path, nombre_archivo)
                    if os.path.exists(ruta):
                        boton.setIcon(QIcon(ruta))
                    else:
                        # Si no existe el archivo, intentar con .svg
                        ruta_svg = os.path.join(iconos_path, nombre_archivo.replace('.png', '.svg'))
                        if os.path.exists(ruta_svg):
                            boton.setIcon(QIcon(ruta_svg))
                except Exception as e:
                    # Silenciar errores de iconos individuales
                    pass
            
            # Iconos del menú principal
            set_icon(self.ui.B_GestionEquipos, "equipo.png")
            set_icon(self.ui.B_GestionParticipantes, "jugador.png")
            set_icon(self.ui.B_GestionCalendario, "calendario.png")
            set_icon(self.ui.B_ActualizarResultados, "partido.png")
            set_icon(self.ui.B_Clasificacion, "trofeo.png")
            set_icon(self.ui.B_Creditos, "creditos.png")
            set_icon(self.ui.B_Ayuda, "ayuda.png")
            
            # Iconos de Equipos
            set_icon(self.ui.B_CrearEquipo, "crear.png")
            set_icon(self.ui.B_EditarEquipo, "editar.png")
            set_icon(self.ui.B_EliminarEquipo, "eliminar.png")
            set_icon(self.ui.B_LimpiarFormEquipo, "limpiar.png")
            set_icon(self.ui.B_SeleccionarColor, "color.png")
            set_icon(self.ui.B_SeleccionarEmblema, "imagen.png")
            set_icon(self.ui.B_VerJugadoresEquipo, "buscar.png")
            
            # Iconos de Participantes
            set_icon(self.ui.B_RegistrarParticipante, "crear.png")
            set_icon(self.ui.B_EditarParticipante, "editar.png")
            set_icon(self.ui.B_EliminarParticipante, "eliminar.png")
            set_icon(self.ui.B_LimpiarFormParticipante, "limpiar.png")
            
            # Iconos de Calendario
            set_icon(self.ui.B_ProgramarPartido, "crear.png")
            set_icon(self.ui.B_EditarPartido, "editar.png")
            set_icon(self.ui.B_EliminarPartido, "eliminar.png")
            set_icon(self.ui.B_LimpiarFormPartido, "limpiar.png")
            
            # Iconos de Resultados
            set_icon(self.ui.B_GuardarResultado, "guardar.png")
            set_icon(self.ui.B_LimpiarResultado, "limpiar.png")
            set_icon(self.ui.B_AgregarEstadisticaJugador, "crear.png")
            
            # Iconos de Clasificación
            set_icon(self.ui.B_GenerarSiguienteRonda, "siguiente.png")
            set_icon(self.ui.B_ActualizarClasificacion, "buscar.png")
            set_icon(self.ui.B_ExportarCSV, "exportar.png")
            
            # Iconos de botones Volver
            set_icon(self.ui.B_VolverDesdeEquipos, "volver.png")
            set_icon(self.ui.B_VolverDesdeParticipantes, "volver.png")
            set_icon(self.ui.B_VolverDesdeCalendario, "volver.png")
            set_icon(self.ui.B_VolverDesdeResultados, "volver.png")
            set_icon(self.ui.B_VolverDesdeClasificacion, "volver.png")
            set_icon(self.ui.B_VolverDesdeCreditos, "volver.png")
            set_icon(self.ui.B_VolverDesdeAyuda, "volver.png")
        except Exception as e:
            # Si falla la configuración de iconos, continuar sin ellos
            print(f"⚠ Advertencia: No se pudieron configurar iconos: {e}")
    
    def mostrar_notificaciones(self):
        """Muestra notificaciones importantes (funcionalidad opcional)."""
        notificaciones = []
        
        # Verificar partidos sin árbitro
        partidos = Partido.obtener_todos(solo_pendientes=True)
        sin_arbitro = [p for p in partidos if not p.arbitro_id]
        if sin_arbitro:
            notificaciones.append(f"⚠ {len(sin_arbitro)} partidos sin árbitro asignado")
        
        # Verificar equipos sin jugadores
        equipos = Equipo.obtener_todos()
        sin_jugadores = []
        for equipo in equipos:
            jugadores = Equipo.obtener_jugadores(equipo.id)
            if len(jugadores) < 5:
                sin_jugadores.append(equipo.nombre)
        
        if sin_jugadores:
            notificaciones.append(f"⚠ Equipos con menos de 5 jugadores: {', '.join(sin_jugadores)}")
        
        # Verificar partidos próximos (en los próximos 7 días)
        from datetime import datetime, timedelta
        hoy = datetime.now().date()
        proxima_semana = hoy + timedelta(days=7)
        
        proximos = []
        for partido in partidos:
            fecha_partido = datetime.strptime(partido.fecha, "%Y-%m-%d").date()
            if hoy <= fecha_partido <= proxima_semana:
                proximos.append(f"{partido.fecha} - ID {partido.id}")
        
        if proximos:
            notificaciones.append(f"📅 Partidos próximos:\n" + "\n".join(proximos))
        
        if not notificaciones:
            notificaciones.append("✓ No hay notificaciones pendientes")
        
        QMessageBox.information(
            self, "Notificaciones",
            "\n\n".join(notificaciones)
        )
    
    def abrir_partido_en_vivo(self):
        """Abre la página de partido en vivo con cronómetro."""
        # Cargar partidos disponibles
        self.partido_en_vivo_widget.cargar_partidos_disponibles()
        # Cambiar a la página
        self.ui.Stacked_Paginas.setCurrentIndex(self.indice_partido_vivo)
    
    def abrir_generador_informes(self):
        """Abre la ventana de generación de informes."""
        from controllers.geninformes_logica import MiApp
        import os
        
        # Crear ventana de informes
        self.ventana_informes = MiApp()
        
        # Configurar rutas por defecto
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        ruta_entrada = os.path.join(base_path, 'informesSQLite')
        ruta_salida = os.path.join(base_path, 'informesSQLite', 'pdf')
        
        # Establecer rutas en los campos de texto
        self.ventana_informes.cdrTxtRutaEntrada.setText(ruta_entrada)
        self.ventana_informes.cdrTxtRutaSalida.setText(ruta_salida)
        
        # Cargar ficheros disponibles
        try:
            ficheros = [f for f in os.listdir(ruta_entrada) if f.endswith('.jrxml')]
            self.ventana_informes.comboBoxFicheros.clear()
            self.ventana_informes.comboBoxFicheros.addItems(ficheros)
        except Exception:
            pass
        
        # Mostrar ventana
        self.ventana_informes.show()
