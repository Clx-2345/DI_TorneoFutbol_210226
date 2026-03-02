"""
Vista para jugar partidos en vivo con cronómetro integrado.

Este módulo contiene el widget PartidoEnVivoWidget que permite
jugar un partido en tiempo real, registrando eventos con timestamps.

Autor: Sistema
Versión: 1.0.0
Fecha: Febrero 2026
"""

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGroupBox,
                               QLabel, QPushButton, QComboBox, QSpinBox,
                               QTableWidget, QTableWidgetItem, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from widget.reloj_digital import RelojDigital
from models.reloj_model import ClockMode, TimerDirection
from models.partido import Partido
from models.equipo import Equipo
from models.evento_partido import EventoPartido


class PartidoEnVivoWidget(QWidget):
    """
    Widget para jugar partidos en vivo con cronómetro.
    Permite registrar eventos (goles, tarjetas) en tiempo real.
    """
    
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.app = app
        self.partido_actual_id = None
        self.setup_ui()
    
    def setup_ui(self):
        """Configura la interfaz de usuario."""
        layout_principal = QVBoxLayout(self)
        
        # Header
        header_layout = QHBoxLayout()
        self.btn_volver = QPushButton("← Volver")
        self.btn_volver.setMaximumWidth(100)
        header_layout.addWidget(self.btn_volver)
        
        titulo = QLabel("Jugar Partido en Vivo")
        font_titulo = QFont()
        font_titulo.setPointSize(16)
        font_titulo.setBold(True)
        titulo.setFont(font_titulo)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(titulo)
        
        spacer = QWidget()
        spacer.setFixedWidth(100)
        header_layout.addWidget(spacer)
        
        layout_principal.addLayout(header_layout)
        
        # Selección de partido (arriba, ancho completo)
        group_seleccion = QGroupBox("Seleccionar Partido")
        layout_seleccion = QHBoxLayout(group_seleccion)
        layout_seleccion.addWidget(QLabel("Partido:"))
        self.combo_partidos = QComboBox()
        self.combo_partidos.setMinimumHeight(30)
        self.combo_partidos.currentIndexChanged.connect(self.cargar_partido_seleccionado)
        layout_seleccion.addWidget(self.combo_partidos)
        layout_principal.addWidget(group_seleccion)
        
        # Layout de 2 columnas
        layout_dos_columnas = QHBoxLayout()
        
        # ===== COLUMNA IZQUIERDA =====
        columna_izquierda = QVBoxLayout()
        
        # Componente de Cronómetro
        group_cronometro = QGroupBox("Cronómetro del Partido")
        layout_cronometro = QVBoxLayout(group_cronometro)
        self.reloj = RelojDigital(self.app)
        self.reloj.set_mode(ClockMode.TIMER)
        self.reloj.set_timer_direction(TimerDirection.PROGRESSIVE)
        layout_cronometro.addWidget(self.reloj)
        columna_izquierda.addWidget(group_cronometro)
        
        # Marcador actual
        group_marcador = QGroupBox("Marcador Actual")
        layout_marcador = QHBoxLayout(group_marcador)
        
        # Equipo Local
        layout_local = QVBoxLayout()
        self.lbl_equipo_local = QLabel("Equipo Local")
        font_equipo = QFont()
        font_equipo.setPointSize(12)
        font_equipo.setBold(True)
        self.lbl_equipo_local.setFont(font_equipo)
        self.lbl_equipo_local.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_local.addWidget(self.lbl_equipo_local)
        
        self.lbl_goles_local = QLabel("0")
        font_goles = QFont()
        font_goles.setPointSize(36)
        font_goles.setBold(True)
        self.lbl_goles_local.setFont(font_goles)
        self.lbl_goles_local.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_local.addWidget(self.lbl_goles_local)
        layout_marcador.addLayout(layout_local)
        
        # VS
        lbl_vs = QLabel("VS")
        lbl_vs.setFont(font_equipo)
        lbl_vs.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_marcador.addWidget(lbl_vs)
        
        # Equipo Visitante
        layout_visitante = QVBoxLayout()
        self.lbl_equipo_visitante = QLabel("Equipo Visitante")
        self.lbl_equipo_visitante.setFont(font_equipo)
        self.lbl_equipo_visitante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_visitante.addWidget(self.lbl_equipo_visitante)
        
        self.lbl_goles_visitante = QLabel("0")
        self.lbl_goles_visitante.setFont(font_goles)
        self.lbl_goles_visitante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_visitante.addWidget(self.lbl_goles_visitante)
        layout_marcador.addLayout(layout_visitante)
        
        columna_izquierda.addWidget(group_marcador)
        
        # Botones finales en columna izquierda
        self.btn_finalizar = QPushButton("Finalizar y Guardar Partido")
        self.btn_finalizar.clicked.connect(self.finalizar_partido)
        columna_izquierda.addWidget(self.btn_finalizar)
        
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_cancelar.clicked.connect(self.cancelar_partido)
        columna_izquierda.addWidget(self.btn_cancelar)
        
        layout_dos_columnas.addLayout(columna_izquierda)
        
        # ===== COLUMNA DERECHA =====
        columna_derecha = QVBoxLayout()
        
        # Registrar evento
        group_evento = QGroupBox("Registrar Evento")
        layout_evento = QVBoxLayout(group_evento)
        
        # Línea 1: Jugador
        layout_jugador = QHBoxLayout()
        layout_jugador.addWidget(QLabel("Jugador:"))
        self.combo_jugador = QComboBox()
        self.combo_jugador.setMinimumHeight(30)
        layout_jugador.addWidget(self.combo_jugador)
        layout_evento.addLayout(layout_jugador)
        
        # Línea 2: Tipo de evento
        layout_tipo = QHBoxLayout()
        layout_tipo.addWidget(QLabel("Tipo de Evento:"))
        self.combo_tipo_evento = QComboBox()
        self.combo_tipo_evento.setMinimumHeight(30)
        self.combo_tipo_evento.addItems(["Gol", "Tarjeta Amarilla", "Tarjeta Roja"])
        layout_tipo.addWidget(self.combo_tipo_evento)
        layout_evento.addLayout(layout_tipo)
        
        # Botón registrar
        self.btn_registrar_evento = QPushButton("✓ Registrar Evento")
        self.btn_registrar_evento.setMinimumHeight(40)
        self.btn_registrar_evento.clicked.connect(self.registrar_evento)
        layout_evento.addWidget(self.btn_registrar_evento)
        
        columna_derecha.addWidget(group_evento)
        
        # Tabla de eventos
        group_eventos = QGroupBox("Eventos del Partido")
        layout_eventos = QVBoxLayout(group_eventos)
        self.tabla_eventos = QTableWidget()
        self.tabla_eventos.setColumnCount(4)
        self.tabla_eventos.setHorizontalHeaderLabels(["Min", "Tipo", "Jugador", "Acción"])
        layout_eventos.addWidget(self.tabla_eventos)
        columna_derecha.addWidget(group_eventos)
        
        layout_dos_columnas.addLayout(columna_derecha)
        
        # Hacer que ambas columnas tengan el mismo ancho
        layout_dos_columnas.setStretch(0, 1)
        layout_dos_columnas.setStretch(1, 1)
        
        layout_principal.addLayout(layout_dos_columnas)
    
    def cargar_partidos_disponibles(self):
        """Carga los partidos pendientes en el combo."""
        self.combo_partidos.clear()
        self.combo_partidos.addItem("Seleccione un partido...")
        
        partidos = Partido.obtener_todos(solo_pendientes=True)
        for partido in partidos:
            detalle = Partido.obtener_detalle_completo(partido.id)
            if detalle:
                texto = f"{partido.id} - {detalle['equipo_local']} vs {detalle['equipo_visitante']} - {detalle['fecha']}"
                self.combo_partidos.addItem(texto, partido.id)
    
    def cargar_partido_seleccionado(self):
        """Carga los datos del partido seleccionado."""
        if self.combo_partidos.currentIndex() == 0:
            self.partido_actual_id = None
            return
        
        self.partido_actual_id = self.combo_partidos.currentData()
        if not self.partido_actual_id:
            return
        
        # Cargar detalles del partido
        detalle = Partido.obtener_detalle_completo(self.partido_actual_id)
        if detalle:
            self.lbl_equipo_local.setText(detalle['equipo_local'])
            self.lbl_equipo_visitante.setText(detalle['equipo_visitante'])
            self.lbl_goles_local.setText(str(detalle['goles_local']))
            self.lbl_goles_visitante.setText(str(detalle['goles_visitante']))
            
            # Cargar jugadores
            self.cargar_jugadores()
            
            # Cargar eventos existentes
            self.cargar_eventos()
    
    def cargar_jugadores(self):
        """Carga los jugadores de ambos equipos."""
        self.combo_jugador.clear()
        self.combo_jugador.addItem("Seleccione un jugador...")
        
        if not self.partido_actual_id:
            return
        
        partido = Partido.obtener_por_id(self.partido_actual_id)
        if partido:
            # Jugadores del equipo local
            jugadores_local = Equipo.obtener_jugadores(partido.equipo_local_id)
            for j in jugadores_local:
                self.combo_jugador.addItem(
                    f"{j['nombre']} (Local)", j['id']
                )
            
            # Jugadores del equipo visitante
            jugadores_visitante = Equipo.obtener_jugadores(partido.equipo_visitante_id)
            for j in jugadores_visitante:
                self.combo_jugador.addItem(
                    f"{j['nombre']} (Visitante)", j['id']
                )
    
    def obtener_minuto_actual(self):
        """Obtiene el minuto actual del cronómetro."""
        # El cronómetro está en segundos, convertir a minutos
        return self.reloj._timer_current // 60
    
    def registrar_evento(self):
        """Registra un evento en el partido."""
        if not self.partido_actual_id:
            QMessageBox.warning(self, "Sin partido", "Seleccione un partido primero")
            return
        
        if self.combo_jugador.currentIndex() == 0:
            QMessageBox.warning(self, "Sin jugador", "Seleccione un jugador")
            return
        
        jugador_id = self.combo_jugador.currentData()
        tipo_evento = self.combo_tipo_evento.currentText().lower().replace(" ", "_")
        minuto = self.obtener_minuto_actual()
        jugador_nombre = self.combo_jugador.currentText()
        
        descripcion = f"{jugador_nombre} - {self.combo_tipo_evento.currentText()}"
        
        if EventoPartido.registrar(self.partido_actual_id, jugador_id, tipo_evento, minuto, descripcion):
            # Actualizar marcador si es gol
            if tipo_evento == "gol":
                self.actualizar_marcador_gol(jugador_nombre)
            
            self.cargar_eventos()
            QMessageBox.information(self, "Evento registrado", 
                                  f"Evento registrado en el minuto {minuto}")
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar el evento")
    
    def actualizar_marcador_gol(self, jugador_nombre):
        """Actualiza el marcador cuando hay un gol."""
        if "(Local)" in jugador_nombre:
            goles_actuales = int(self.lbl_goles_local.text())
            self.lbl_goles_local.setText(str(goles_actuales + 1))
        elif "(Visitante)" in jugador_nombre:
            goles_actuales = int(self.lbl_goles_visitante.text())
            self.lbl_goles_visitante.setText(str(goles_actuales + 1))
    
    def cargar_eventos(self):
        """Carga los eventos del partido en la tabla."""
        if not self.partido_actual_id:
            return
        
        eventos = EventoPartido.obtener_por_partido(self.partido_actual_id)
        
        self.tabla_eventos.setRowCount(len(eventos))
        for i, evento in enumerate(eventos):
            self.tabla_eventos.setItem(i, 0, QTableWidgetItem(f"{evento['minuto']}'"))
            
            tipo_display = evento['tipo_evento'].replace("_", " ").title()
            self.tabla_eventos.setItem(i, 1, QTableWidgetItem(tipo_display))
            self.tabla_eventos.setItem(i, 2, QTableWidgetItem(evento['jugador_nombre']))
            
            # Botón eliminar
            btn_eliminar = QPushButton("Eliminar")
            btn_eliminar.clicked.connect(lambda checked, eid=evento['id']: self.eliminar_evento(eid))
            self.tabla_eventos.setCellWidget(i, 3, btn_eliminar)
        
        self.tabla_eventos.resizeColumnsToContents()
    
    def eliminar_evento(self, evento_id):
        """Elimina un evento del partido."""
        respuesta = QMessageBox.question(
            self, "Confirmar",
            "¿Eliminar este evento?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
            if EventoPartido.eliminar_por_id(evento_id):
                self.cargar_eventos()
                # Recalcular marcador desde eventos
                self.recalcular_marcador()
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar el evento")
    
    def recalcular_marcador(self):
        """Recalcula el marcador basándose en los eventos."""
        if not self.partido_actual_id:
            return
        
        eventos = EventoPartido.obtener_por_partido(self.partido_actual_id)
        
        # Obtener partido para saber qué equipo es local/visitante
        partido = Partido.obtener_por_id(self.partido_actual_id)
        jugadores_local = Equipo.obtener_jugadores(partido.equipo_local_id)
        ids_local = [j['id'] for j in jugadores_local]
        
        goles_local = 0
        goles_visitante = 0
        
        for evento in eventos:
            if evento['tipo_evento'] == 'gol':
                if evento['jugador_id'] in ids_local:
                    goles_local += 1
                else:
                    goles_visitante += 1
        
        self.lbl_goles_local.setText(str(goles_local))
        self.lbl_goles_visitante.setText(str(goles_visitante))
    
    def finalizar_partido(self):
        """Finaliza el partido y guarda el resultado."""
        if not self.partido_actual_id:
            QMessageBox.warning(self, "Sin partido", "No hay partido seleccionado")
            return
        
        respuesta = QMessageBox.question(
            self, "Finalizar Partido",
            "¿Finalizar el partido y guardar el resultado?\n\nEsto marcará el partido como jugado.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
            goles_local = int(self.lbl_goles_local.text())
            goles_visitante = int(self.lbl_goles_visitante.text())
            
            if Partido.registrar_resultado(self.partido_actual_id, goles_local, goles_visitante):
                # Actualizar estadísticas individuales desde eventos
                self.actualizar_estadisticas_desde_eventos()
                
                QMessageBox.information(self, "Éxito", 
                                      "Partido finalizado y resultado guardado")
                self.limpiar_formulario()
                self.cargar_partidos_disponibles()
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el resultado")
    
    def actualizar_estadisticas_desde_eventos(self):
        """Actualiza las estadísticas de jugadores basándose en los eventos."""
        from models.estadistica_partido import EstadisticaPartido
        from models.participante import Participante
        
        eventos = EventoPartido.obtener_por_partido(self.partido_actual_id)
        
        # Agrupar eventos por jugador
        estadisticas_jugador = {}
        for evento in eventos:
            jid = evento['jugador_id']
            if jid not in estadisticas_jugador:
                estadisticas_jugador[jid] = {'goles': 0, 't_amarillas': 0, 't_rojas': 0}
            
            if evento['tipo_evento'] == 'gol':
                estadisticas_jugador[jid]['goles'] += 1
            elif evento['tipo_evento'] == 'tarjeta_amarilla':
                estadisticas_jugador[jid]['t_amarillas'] += 1
            elif evento['tipo_evento'] == 'tarjeta_roja':
                estadisticas_jugador[jid]['t_rojas'] += 1
        
        # Guardar estadísticas del partido y actualizar globales
        for jugador_id, stats in estadisticas_jugador.items():
            EstadisticaPartido.registrar(
                self.partido_actual_id,
                jugador_id,
                stats['goles'],
                stats['t_amarillas'],
                stats['t_rojas']
            )
            
            Participante.actualizar_estadisticas(
                jugador_id,
                stats['goles'],
                stats['t_amarillas'],
                stats['t_rojas']
            )
    
    def cancelar_partido(self):
        """Cancela la sesión actual sin guardar."""
        respuesta = QMessageBox.question(
            self, "Cancelar",
            "¿Cancelar sin guardar?\n\nSe perderán todos los eventos registrados.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
            if self.partido_actual_id:
                # Opcional: eliminar eventos del partido
                EventoPartido.limpiar_eventos_partido(self.partido_actual_id)
            self.limpiar_formulario()
    
    def limpiar_formulario(self):
        """Limpia el formulario."""
        self.partido_actual_id = None
        self.combo_partidos.setCurrentIndex(0)
        self.lbl_equipo_local.setText("Equipo Local")
        self.lbl_equipo_visitante.setText("Equipo Visitante")
        self.lbl_goles_local.setText("0")
        self.lbl_goles_visitante.setText("0")
        self.combo_jugador.clear()
        self.tabla_eventos.setRowCount(0)
