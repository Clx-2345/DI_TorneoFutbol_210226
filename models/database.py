"""
Módulo de gestión de base de datos SQLite para el Torneo de Fútbol.

Este módulo maneja la conexión a SQLite y la creación de todas las tablas
necesarias para gestionar equipos, participantes, partidos y estadísticas.

Autor: [Tu Nombre]
Versión: 1.0.0
Fecha: Enero 2026
"""

import os
import sys
import shutil
from pathlib import Path
from PySide6.QtSql import QSqlDatabase, QSqlQuery


def obtener_ruta_base():
    """
    Obtiene la ruta base donde está el ejecutable o el script.
    
    Returns:
        str: Ruta base de la aplicación
    """
    if getattr(sys, 'frozen', False):
        # Si estamos en un ejecutable empaquetado con PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Si estamos en modo desarrollo
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def obtener_ruta_datos():
    """
    Obtiene la ruta donde se guardarán los datos persistentes.
    
    Returns:
        str: Ruta del directorio de datos
    """
    if getattr(sys, 'frozen', False):
        # En ejecutable: guardar en AppData del usuario
        appdata = os.getenv('APPDATA')
        ruta_datos = os.path.join(appdata, 'TorneoFutbol')
    else:
        # En desarrollo: usar el directorio actual
        ruta_datos = obtener_ruta_base()
    
    # Crear el directorio si no existe
    os.makedirs(ruta_datos, exist_ok=True)
    return ruta_datos


def obtener_ruta_db():
    """
    Obtiene la ruta completa del archivo de base de datos.
    
    Returns:
        str: Ruta completa del archivo de base de datos
    """
    ruta_datos = obtener_ruta_datos()
    ruta_db = os.path.join(ruta_datos, 'torneoFutbol_sqlite.db')
    
    # Si estamos en ejecutable y la BD no existe, copiar la plantilla
    if getattr(sys, 'frozen', False) and not os.path.exists(ruta_db):
        # Buscar la BD plantilla en el directorio del ejecutable
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller crea un directorio temporal en _MEIPASS
            plantilla_db = os.path.join(sys._MEIPASS, 'torneoFutbol_sqlite.db')
        else:
            plantilla_db = os.path.join(obtener_ruta_base(), 'torneoFutbol_sqlite.db')
        
        # Copiar la plantilla si existe
        if os.path.exists(plantilla_db):
            print(f"Copiando base de datos inicial a: {ruta_db}")
            shutil.copy2(plantilla_db, ruta_db)
    
    return ruta_db


def obtener_db():
    """
    Obtiene la conexión actual a la base de datos.
    
    Returns:
        QSqlDatabase: Objeto de conexión a la base de datos
    """
    return QSqlDatabase.database()


def conectar():
    """
    Establece la conexión con la base de datos SQLite.
    
    Crea el archivo torneoFutbol_sqlite.db si no existe, activa las foreign keys
    y crea todas las tablas necesarias.
    
    Returns:
        QSqlDatabase: Objeto de conexión a la base de datos
        
    Raises:
        Exception: Si no se puede abrir la base de datos
    """
    # Obtener la ruta de la base de datos
    ruta_db = obtener_ruta_db()
    print(f"Usando base de datos en: {ruta_db}")
    
    # Crear la conexión a la base de datos
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(ruta_db)
    
    if not db.open():
        raise Exception("No se pudo abrir la BD")
    
    print("✓ BBDD abierta correctamente")
    
    # Crear un objeto query
    query = QSqlQuery()
    
    # Activar foreign keys ya que no las activa por defecto
    query.exec("PRAGMA foreign_keys = ON;")
    
    # Crear todas las tablas
    crear_tablas(query)
    
    return db


def crear_tablas(query):
    """
    Crea todas las tablas necesarias para el sistema de torneo.
    
    Tablas creadas:
    - equipos: Datos de los equipos participantes
    - participantes: Jugadores y árbitros
    - partidos: Información de los partidos
    - estadisticas_partido: Estadísticas detalladas por jugador y partido
    
    Args:
        query (QSqlQuery): Objeto query para ejecutar comandos SQL
    """
    
    # Tabla EQUIPOS
    query.exec("""
        CREATE TABLE IF NOT EXISTS equipos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            curso TEXT NOT NULL,
            color_camiseta TEXT NOT NULL,
            emblema_path TEXT,
            emblema_blob BLOB,
            info_adicional TEXT,
            fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("✓ Tabla 'equipos' verificada/creada")
    
    # Agregar columna emblema_blob si no existe (para bases de datos existentes)
    query.exec("""
        SELECT COUNT(*) as cnt FROM pragma_table_info('equipos') WHERE name='emblema_blob'
    """)
    if query.next() and query.value(0) == 0:
        query.exec("ALTER TABLE equipos ADD COLUMN emblema_blob BLOB")
        print("✓ Columna 'emblema_blob' agregada a tabla 'equipos'")
    
    # Tabla PARTICIPANTES (Jugadores y Árbitros)
    query.exec("""
        CREATE TABLE IF NOT EXISTS participantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            fecha_nacimiento TEXT NOT NULL,
            curso TEXT NOT NULL,
            es_jugador INTEGER DEFAULT 0,
            es_arbitro INTEGER DEFAULT 0,
            posicion TEXT,
            equipo_id INTEGER,
            goles INTEGER DEFAULT 0,
            t_amarillas INTEGER DEFAULT 0,
            t_rojas INTEGER DEFAULT 0,
            fecha_registro TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE SET NULL,
            CHECK (es_jugador = 1 OR es_arbitro = 1)
        )
    """)
    print("✓ Tabla 'participantes' verificada/creada")
    
    # Tabla PARTIDOS
    query.exec("""
        CREATE TABLE IF NOT EXISTS partidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipo_local_id INTEGER NOT NULL,
            equipo_visitante_id INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL,
            arbitro_id INTEGER,
            eliminatoria TEXT NOT NULL,
            lugar TEXT,
            goles_local INTEGER DEFAULT 0,
            goles_visitante INTEGER DEFAULT 0,
            jugado INTEGER DEFAULT 0,
            fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (equipo_local_id) REFERENCES equipos(id) ON DELETE CASCADE,
            FOREIGN KEY (equipo_visitante_id) REFERENCES equipos(id) ON DELETE CASCADE,
            FOREIGN KEY (arbitro_id) REFERENCES participantes(id) ON DELETE SET NULL,
            CHECK (equipo_local_id != equipo_visitante_id),
            CHECK (eliminatoria IN ('Previa', 'Dieciseisavos', 'Octavos', 'Cuartos', 'Semifinales', 'Final'))
        )
    """)
    print("✓ Tabla 'partidos' verificada/creada")
    
    # Tabla ESTADISTICAS_PARTIDO (Goles y tarjetas por jugador en cada partido)
    query.exec("""
        CREATE TABLE IF NOT EXISTS estadisticas_partido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            partido_id INTEGER NOT NULL,
            jugador_id INTEGER NOT NULL,
            goles INTEGER DEFAULT 0,
            t_amarillas INTEGER DEFAULT 0,
            t_rojas INTEGER DEFAULT 0,
            FOREIGN KEY (partido_id) REFERENCES partidos(id) ON DELETE CASCADE,
            FOREIGN KEY (jugador_id) REFERENCES participantes(id) ON DELETE CASCADE,
            UNIQUE(partido_id, jugador_id)
        )
    """)
    print("✓ Tabla 'estadisticas_partido' verificada/creada")
    
    # Crear índices para mejorar el rendimiento
    crear_indices(query)


def crear_indices(query):
    # Índice en el nombre de equipos (búsquedas frecuentes)
    query.exec("""
        CREATE INDEX IF NOT EXISTS idx_equipos_nombre 
        ON equipos(nombre)
    """)
    
    # Índice en participantes por equipo
    query.exec("""
        CREATE INDEX IF NOT EXISTS idx_participantes_equipo 
        ON participantes(equipo_id)
    """)
    
    # Índice en partidos por eliminatoria
    query.exec("""
        CREATE INDEX IF NOT EXISTS idx_partidos_eliminatoria 
        ON partidos(eliminatoria)
    """)
    
    # Índice en partidos por fecha
    query.exec("""
        CREATE INDEX IF NOT EXISTS idx_partidos_fecha 
        ON partidos(fecha)
    """)
    
    # Índice en estadísticas por partido
    query.exec("""
        CREATE INDEX IF NOT EXISTS idx_estadisticas_partido 
        ON estadisticas_partido(partido_id)
    """)
    
    print("✓ Índices creados/verificados")


def cerrar_conexion():
    db = QSqlDatabase.database()
    if db.isOpen():
        db.close()
        print("✓ BBDD cerrada correctamente")


def verificar_conexion():
    db = QSqlDatabase.database()
    return db.isOpen()


def obtener_info_bd():
    db = QSqlDatabase.database()
    query = QSqlQuery()
    
    info = {
        "nombre": db.databaseName(),
        "driver": db.driverName(),
        "abierta": db.isOpen(),
        "tablas": db.tables()
    }
    
    # Contar registros en cada tabla
    info["registros"] = {}
    for tabla in info["tablas"]:
        query.exec(f"SELECT COUNT(*) FROM {tabla}")
        if query.next():
            info["registros"][tabla] = query.value(0)
    
    return info


# Función auxiliar para ejecutar consultas con manejo de errores
def ejecutar_query(sql, parametros=None):
    query = QSqlQuery()
    
    if parametros:
        query.prepare(sql)
        for parametro in parametros:
            query.addBindValue(parametro)
        if not query.exec():
            raise Exception(f"Error ejecutando query: {query.lastError().text()}")
    else:
        if not query.exec(sql):
            raise Exception(f"Error ejecutando query: {query.lastError().text()}")
    
    return query


if __name__ == "__main__":
    try:
        print("\n=== PRUEBA DE CONEXIÓN A BASE DE DATOS ===\n")
        
        # Conectar a la base de datos
        db = conectar()
        
        # Obtener información
        print("\n=== INFORMACIÓN DE LA BASE DE DATOS ===\n")
        info = obtener_info_bd()
        print(f"Nombre: {info['nombre']}")
        print(f"Driver: {info['driver']}")
        print(f"Estado: {'Abierta' if info['abierta'] else 'Cerrada'}")
        print(f"\nTablas creadas: {', '.join(info['tablas'])}")
        print("\nRegistros por tabla:")
        for tabla, cantidad in info["registros"].items():
            print(f"  - {tabla}: {cantidad} registros")
        
        # Cerrar conexión
        print("\n" + "="*40 + "\n")
        cerrar_conexion()
        
        print("\n✓ Prueba completada exitosamente\n")
        
    except Exception as e:
        print(f"\n✗ Error: {e}\n")
