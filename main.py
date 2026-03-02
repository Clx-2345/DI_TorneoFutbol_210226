import sys
import os
import traceback
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt
from models.database import conectar, cerrar_conexion
from controllers.main_controller import MainController
from models.evento_partido import EventoPartido


def configurar_java():
    """
    Configura JAVA_HOME automáticamente si es necesario para pyreportjasper.
    pyreportjasper requiere Java 9+ (class file version 53.0 o superior).
    """
    java_home = os.environ.get('JAVA_HOME', '')
    
    # Si JAVA_HOME apunta a Java 8, buscar JDK más reciente
    if 'jdk1.8' in java_home.lower() or 'jre1.8' in java_home.lower() or not java_home:
        # Buscar JDK 21, 17, o cualquier JDK moderno
        posibles_jdk = [
            r"C:\Program Files\Java\jdk-21",
            r"C:\Program Files\Java\jdk-17",
            r"C:\Program Files\Java\jdk-11",
        ]
        
        for jdk_path in posibles_jdk:
            if os.path.exists(jdk_path):
                os.environ['JAVA_HOME'] = jdk_path
                os.environ['PATH'] = f"{jdk_path}\\bin;{os.environ.get('PATH', '')}"
                print(f"✅ JAVA_HOME configurado automáticamente a: {jdk_path}")
                return True
        
        print("⚠️  Advertencia: No se encontró JDK 11+ instalado")
        print("   Se requiere Java 11 o superior para generar informes")
        print("   Descarga desde: https://www.oracle.com/java/technologies/downloads/")
        return False
    
    return True


def obtener_ruta_recurso(ruta_relativa):
    """
    Obtiene la ruta absoluta de un recurso, funciona tanto en desarrollo como en ejecutable.
    
    Args:
        ruta_relativa: Ruta relativa del recurso
        
    Returns:
        str: Ruta absoluta del recurso
    """
    if getattr(sys, 'frozen', False):
        # Si estamos en un ejecutable empaquetado
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller crea un directorio temporal
            ruta_base = sys._MEIPASS
        else:
            ruta_base = os.path.dirname(sys.executable)
    else:
        # Si estamos en modo desarrollo
        ruta_base = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(ruta_base, ruta_relativa)


def load_stylesheet(path):
    try:
        ruta_completa = obtener_ruta_recurso(path)
        with open(ruta_completa, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"⚠ Advertencia: No se encontró el archivo de estilos: {path}")
        return ""
    except Exception as e:
        print(f"⚠ Error al cargar estilos: {e}")
        return ""


def main():
    """
    Función principal que inicializa y ejecuta la aplicación.
    """
    # Configurar Java automáticamente si es necesario
    configurar_java()
    
    # Crear la aplicación con soporte de idiomas
    class TorneoFutbolApp(QApplication):
        def __init__(self, argv):
            super().__init__(argv)
            self.current_language = 'es'  # Idioma por defecto
        
        def set_language(self, language):
            """Cambia el idioma de la aplicación."""
            self.current_language = language
    
    app = TorneoFutbolApp(sys.argv)
    
    # Configurar información de la aplicación
    app.setApplicationName("Torneo de Fútbol")
    app.setOrganizationName("[Tu Nombre/Institución]")
    app.setApplicationVersion("1.0.0")
    
    print("\n" + "="*50)
    print("  TORNEO DE FÚTBOL - Sistema de Gestión")
    print("  Versión 1.0.0")
    print("="*50 + "\n")
    
    # Conectar a la base de datos
    try:
        print("Conectando a la base de datos...")
        db = conectar()
        print("✓ Base de datos conectada correctamente\n")
        
        # Crear tabla de eventos si no existe
        print("Inicializando tablas adicionales...")
        EventoPartido.crear_tabla()
        print("✓ Tablas verificadas\n")
    except Exception as e:
        QMessageBox.critical(
            None, "Error de Base de Datos",
            f"No se pudo conectar a la base de datos:\n{e}\n\nLa aplicación se cerrará."
        )
        return 1
    
    # Cargar archivo QSS de estilos
    print("Cargando estilos...")
    qss = load_stylesheet("resources/style.qss")
    if qss:
        app.setStyleSheet(qss)
        print("✓ Estilos cargados correctamente\n")
    else:
        print("⚠ Continuando sin estilos personalizados\n")
    
    # Crear y mostrar la ventana principal
    try:
        print("Iniciando interfaz gráfica...")
        window = MainController(app)
        window.show()
        print("✓ Interfaz inicializada correctamente\n")
        print("="*50)
        print("  Aplicación lista para usar")
        print("="*50 + "\n")
    except Exception as e:
        print(f"\n❌ ERROR al inicializar la interfaz:")
        print(traceback.format_exc())
        QMessageBox.critical(
            None, "Error de Inicialización",
            f"No se pudo inicializar la aplicación:\n{e}"
        )
        cerrar_conexion()
        return 1
    
    # Ejecutar el bucle de eventos
    try:
        exit_code = app.exec()
    except KeyboardInterrupt:
        print("\n\n⚠ Aplicación interrumpida por el usuario")
        exit_code = 0
    
    # Limpiar recursos
    print("\nCerrando aplicación...")
    cerrar_conexion()
    print("✓ Recursos liberados\n")
    print("="*50)
    print("  ¡Hasta pronto!")
    print("="*50 + "\n")
    
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
