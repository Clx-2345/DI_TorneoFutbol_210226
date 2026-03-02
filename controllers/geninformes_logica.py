# -*- coding: utf-8 -*-
"""
════════════════════════════════════════════════════════════════════════════════
LÓGICA DEL GENERADOR DE INFORMES - TORNEO DE FÚTBOL
════════════════════════════════════════════════════════════════════════════════

Módulo con la lógica personalizada de la interfaz gráfica.
Implementa los métodos que responden a eventos de botones y campos de texto.

Importa:
  • GeneradorInformes: La clase con la lógica personalizada
  • Ui_Form: La interfaz generada por Qt Designer
  • crearinforme: Las funciones para generar PDFs

Estructura:
  └─ GeneradorInformes (clase con la lógica)
  └─ MiApp (hereda de QWidget, Ui_Form, GeneradorInformes)
     → Combina: interfaz visual + lógica personalizada + generación PDF
"""

import os
import sys
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QInputDialog
from . import crearinforme
from views.ui_geninformes import Ui_Form


class GeneradorInformes:
    """
    Clase con la LÓGICA personalizada para generar informes.
    
    Métodos:
      • aviso(): Muestra cuadros de diálogo de información
      • pedir_parametros(): Solicita parámetros al usuario
      • error(): Maneja errores de parámetros
      • generar_informe(): Genera el PDF (método principal)
      • cambiar_ruta(): Actualiza la lista de ficheros disponibles
    
    Requiere que la clase que hereda tenga estos atributos (de Ui_Form):
      • cdrTxtRutaEntrada: Campo de texto con ruta de entrada
      • cdrTxtRutaSalida: Campo de texto con ruta de salida
      • comboBoxFicheros: ComboBox con lista de ficheros
    """
    
    def aviso(self, titulo, texto):
        """
        Muestra un cuadro de diálogo de aviso al usuario.
        
        Args:
            titulo (str): Título del cuadro de diálogo
            texto (str): Mensaje a mostrar
        """
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle(titulo)
        dialogo.setText(texto)
        dialogo.exec()
    
    def pedir_parametros(self, pLista):
        """
        Solicita al usuario un parámetro.
        
        Si pLista contiene opciones: abre comboBox para elegir
        Si pLista está vacía: abre input de texto libre
        
        Args:
            pLista (list or str): Lista de opciones o string vacío para texto libre
                                  Ejemplo: ['Equipo A', 'Equipo B'] o ""
        
        Returns:
            str: La opción seleccionada o texto ingresado, o None si cancela
        """
        # CASO 1: Parámetro de lista desplegable
        if pLista and not isinstance(pLista, str):
            pTitulo = "Selecciona un parámetro"
            pTexto = "Elige una opción:"
            sel, conf = QInputDialog.getItem(self, pTitulo, pTexto, pLista)
            if conf:
                return sel
            return None
        
        # CASO 2: Parámetro de texto libre (pLista es "" o lista vacía)
        pTitulo = "Ingresa el parámetro"
        pTexto = "Valor (puede estar vacío):"
        valor, conf = QInputDialog.getText(self, pTitulo, pTexto)
        if conf:  # Usuario no canceló
            return valor  # Devuelve string (puede estar vacío "")
        return None
    
    def error(self, pLista):
        """
        Función de error que devuelve una cadena vacía.
        
        Se usa como fallback si un fichero de informe no tiene
        parámetros definidos en el diccionario sel_param.
        
        Args:
            pLista: No se utiliza (se requiere para compatibilidad)
        
        Returns:
            str: Cadena vacía
        """
        return ""
    
    def generar_informe(self):
        """
        MÉTODO PRINCIPAL: Genera el informe PDF.
        
        Flujo:
        1. Obtiene la ruta del fichero JRXML desde la interfaz
        2. Obtiene la ruta de salida
        3. Valida que el directorio de salida existe
        4. Busca los parámetros necesarios en el diccionario sel_param
        5. Si el informe necesita parámetros, solicita al usuario
        6. Llama a crearinforme.advanced_example_using_database() para generar el PDF
        7. Muestra un mensaje de éxito o error
        """
        
        # Diccionario de parámetros por informe
        # Estructura: {nombre_informe: (nombre_param, función, lista_opciones)}
        # 
        # nombre_param: Nombre del parámetro en el JRXML
        # función: Método para solicitar el parámetro (self.pedir_parametros)
        # lista_opciones: Lista de valores para elegir (si está vacía, es texto libre)
        
        sel_param = {
            # ========== INFORMES DEL TORNEO DE FÚTBOL ==========
            # Informe 1: Equipos y Jugadores
            'Informe_1_Equipos_Jugadores.jrxml':
                ('EQUIPO_FILTRO', self.pedir_parametros, ""),
            
            # Informe 2: Partidos y Resultados
            'Informe_2_Partidos_Resultados.jrxml':
                ('ELIMINATORIA_FILTRO', self.pedir_parametros,
                 ['', 'Octavos', 'Cuartos', 'Semifinal', 'Final']),
            
            # Informe 3: Clasificación y Eliminatorias
            'Informe_3_Clasificacion_Eliminatorias.jrxml':
                ('ELIMINATORIA_FILTRO', self.pedir_parametros,
                 ['', 'Octavos', 'Cuartos', 'Semifinal', 'Final']),
            
            # ========== INFORMES DE EJEMPLO ==========
            # Informe con parámetro de texto libre
            'Informe_4_1_1_1_parametro_texto':
                ('Comentario', self.pedir_parametros, ""),
            
            # Informe con parámetro de lista desplegable (ciudades)
            'Informe_4_1_1_filtrado_datos':
                ('Ciudad', self.pedir_parametros,
                 ['Almendralejo', 'Cáceres', 'Madrid', 'Salamanca', 'Santander', 'Sevilla']),
            
            # Informe con parámetro de lista desplegable (ordenamiento)
            'Informe_4_1_1_ordenar_datos':
                ('Orden', self.pedir_parametros,
                 ['Ciudad', 'Direccion', 'Nombre']),
            
            # Informe con parámetro título
            'Informe_4_7_1_Graficos':
                ('Titulo', self.pedir_parametros, ""),
            
            # Informe complejo con subinformes
            'Informe_4_5_1_InformePrincipal':
                ('Titulo', self.pedir_parametros, ""),
            
            # Subinformes con parámetros Integer (IDs)
            'Informe_4_5_2_Subinformeemails':
                ('Id_contacto', self.pedir_parametros, ""),
            
            'Informe_4_5_3_SubinformeTfnos':
                ('Id_Contacto', self.pedir_parametros, "")
        }
        
        # ─────────────────────────────────────────────────────────────────────────────
        # PASO 1: Obtener rutas de la interfaz
        # ─────────────────────────────────────────────────────────────────────────────
        
        ruta_entrada = self.cdrTxtRutaEntrada.text().strip()
        ruta_salida = self.cdrTxtRutaSalida.text().strip()
        fichero_seleccionado = self.comboBoxFicheros.currentText()
        
        # Validar que hay rutas
        if not ruta_entrada:
            self.aviso("Error", "Debe indicar la ruta de los ficheros JRXML")
            return
        
        if not ruta_salida:
            self.aviso("Error", "Debe indicar la ruta de salida para los PDFs")
            return
        
        if not fichero_seleccionado:
            self.aviso("Error", "Debe seleccionar un fichero de la lista")
            return
        
        # ─────────────────────────────────────────────────────────────────────────────
        # PASO 2: Construir RUTAS ABSOLUTAS usando os.path.join()
        # ─────────────────────────────────────────────────────────────────────────────
        # IMPORTANTE: Usar os.path.join() en lugar de concatenar con "/"
        # Esto asegura que funciona correctamente en Windows (\\) y Linux (/).
        
        ficheroEntrada = os.path.abspath(os.path.join(ruta_entrada, fichero_seleccionado))
        
        # Para la salida, quitamos la extensión .jrxml y usamos el directorio
        nombre_sin_extension = fichero_seleccionado[:-6]  # quitar .jrxml
        ficheroSalida = os.path.abspath(os.path.join(ruta_salida, nombre_sin_extension))
        
        # ✅ Convertir a string explícitamente (por si acaso)
        ficheroEntrada = str(ficheroEntrada)
        ficheroSalida = str(ficheroSalida)
        
        print(f"\n📋 Información de generación:")
        print(f"   Entrada: {ficheroEntrada}")
        print(f"   Salida:  {ficheroSalida}")
        
        # Validar que la ruta de entrada existe
        if not os.path.exists(ficheroEntrada):
            self.aviso("Error", f"El fichero JRXML no existe:\n{ficheroEntrada}")
            return
        
        # ─────────────────────────────────────────────────────────────────────────────
        # PASO 3: Validar directorio de salida (o crear si no existe)
        # ─────────────────────────────────────────────────────────────────────────────
        # ✅ IMPORTANTE: Solo validamos que el DIRECTORIO PADRE existe
        # NO creamos un directorio con el nombre del informe
        
        if not os.path.exists(ruta_salida):
            try:
                os.makedirs(ruta_salida, exist_ok=True)
                print(f"   ✅ Directorio creado: {ruta_salida}")
            except OSError as e:
                self.aviso("Error",
                          f"No se pudo crear el directorio de salida:\n{ruta_salida}\n\nError: {e}")
                return
        
        # ─────────────────────────────────────────────────────────────────────────────
        # PASO 4: Obtener parámetros necesarios
        # ─────────────────────────────────────────────────────────────────────────────
        
        # Tupla de error por defecto si el informe no está en sel_param
        mens_error = ("", self.error, "")
        
        # Obtener la configuración del informe
        config_informe = sel_param.get(nombre_sin_extension, mens_error)
        
        # Elemento 0: nombre del parámetro (ej. 'Comentario', 'Ciudad')
        # Elemento 1: función para solicitar (self.pedir_parametros)
        # Elemento 2: lista de opciones ([] o "")
        nombre_parametro = config_informe[0]
        funcion_solicitar = config_informe[1]
        lista_opciones = config_informe[2]
        
        # Construir diccionario de parámetros
        parametros = {}
        
        if nombre_parametro:  # Si el informe tiene parámetros
            valor_parametro = funcion_solicitar(lista_opciones)
            
            if valor_parametro is None:  # Usuario canceló
                self.aviso("Cancelado", "Generación de informe cancelada")
                return
            
            # ✅ IMPORTANTE: Asegurar que el valor no sea None antes de pasar a Jasper
            # Convertir a string si es necesario (para parámetros Integer)
            parametros[nombre_parametro] = str(valor_parametro)
        
        print(f"   Parámetros: {parametros}")
        
        # ─────────────────────────────────────────────────────────────────────────────
        # PASO 5: Generar el informe
        # ─────────────────────────────────────────────────────────────────────────────
        
        try:
            crearinforme.advanced_example_using_database(
                ficheroEntrada,
                ficheroSalida,
                parametros
            )
            self.aviso("Éxito",
                      f"Informe generado correctamente:\n{ficheroSalida}.pdf")
        
        except Exception as e:
            self.aviso("Error en generación",
                      f"No se pudo generar el informe:\n\n{str(e)}")
            raise
    
    def cambiar_ruta(self):
        """
        Actualiza la lista de ficheros cuando el usuario cambia la ruta.
        
        Se ejecuta cuando el usuario presiona Enter en cdrTxtRutaEntrada.
        
        Flujo:
        1. Obtiene la ruta del campo de texto
        2. Lista todos los ficheros del directorio
        3. Los ordena alfabéticamente
        4. Los carga en el comboBoxFicheros
        5. Muestra un error si la ruta no existe
        """
        try:
            ruta = self.cdrTxtRutaEntrada.text().strip()
            
            if not ruta:
                self.aviso("Ruta vacía", "Debes indicar una ruta")
                return
            
            # Obtener lista de ficheros
            self.comboBoxFicheros.clear()
            items = os.listdir(ruta)
            items.sort()  # Ordenar alfabéticamente
            
            self.comboBoxFicheros.addItems(items)
            
            print(f"✓ Ruta actualizada: {ruta}")
            print(f"  Ficheros encontrados: {len(items)}")
        
        except FileNotFoundError:
            self.aviso("Error",
                      f"El directorio no existe:\n{self.cdrTxtRutaEntrada.text()}")
        except Exception as e:
            self.aviso("Error",
                      f"Error al acceder al directorio:\n{str(e)}")


class MiApp(QWidget, Ui_Form, GeneradorInformes):
    """
    Clase principal de la aplicación.
    
    Hereda de:
      • QWidget: Clase base de widgets Qt
      • Ui_Form: La interfaz (botones, campos, etc.)
      • GeneradorInformes: La lógica personalizada
    
    Una única clase que integra todo:
      - La interfaz visual (Ui_Form)
      - La lógica de respuesta a eventos (GeneradorInformes)
    """
    
    def __init__(self):
        """
        Inicializa la aplicación.
        
        Llama a setupUi() para crear todos los componentes visuales.
        """
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    """
    Script principal. Crea la aplicación Qt y muestra la ventana.
    
    Se ejecuta cuando haces: python main.py
    
    NO se debe ejecutar este fichero directamente:
    ❌ python geninformes_logica.py
    ✅ python main.py
    """
    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec())



