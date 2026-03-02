"""
Modelo para la gestión de Participantes (Jugadores y Árbitros) en el torneo.

Este módulo contiene la clase Participante que maneja todas las operaciones
CRUD para la tabla participantes.

Autor: [Tu Nombre]
Versión: 1.0.0
Fecha: Enero 2026
"""

from PySide6.QtSql import QSqlQuery
from models.database import obtener_db


class Participante:
    """
    Clase para gestionar operaciones de participantes en la base de datos.
    
    Attributes:
        id (int): Identificador único del participante
        nombre (str): Nombre completo
        fecha_nacimiento (str): Fecha de nacimiento
        curso (str): Curso del participante
        es_jugador (bool): Si es jugador
        es_arbitro (bool): Si es árbitro
        posicion (str): Posición si es jugador
        equipo_id (int): ID del equipo asignado
        goles (int): Goles totales
        t_amarillas (int): Tarjetas amarillas totales
        t_rojas (int): Tarjetas rojas totales
    """
    
    def __init__(self, id=None, nombre="", fecha_nacimiento="", curso="",
                 es_jugador=False, es_arbitro=False, posicion="", equipo_id=None,
                 goles=0, t_amarillas=0, t_rojas=0):
        """Inicializa un objeto Participante."""
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.curso = curso
        self.es_jugador = es_jugador
        self.es_arbitro = es_arbitro
        self.posicion = posicion
        self.equipo_id = equipo_id
        self.goles = goles
        self.t_amarillas = t_amarillas
        self.t_rojas = t_rojas
    
    @staticmethod
    def crear(nombre, fecha_nacimiento, curso, es_jugador, es_arbitro,
              posicion="", equipo_id=None, goles=0, t_amarillas=0, t_rojas=0):
        """
        Crea un nuevo participante en la base de datos.
        
        Returns:
            bool: True si se creó correctamente
        """
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO participantes 
            (nombre, fecha_nacimiento, curso, es_jugador, es_arbitro, posicion, 
             equipo_id, goles, t_amarillas, t_rojas)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """)
        query.addBindValue(nombre)
        query.addBindValue(fecha_nacimiento)
        query.addBindValue(curso)
        query.addBindValue(1 if es_jugador else 0)
        query.addBindValue(1 if es_arbitro else 0)
        query.addBindValue(posicion if posicion else None)
        query.addBindValue(equipo_id if equipo_id else None)
        query.addBindValue(goles)
        query.addBindValue(t_amarillas)
        query.addBindValue(t_rojas)
        
        if query.exec():
            obtener_db().commit()
            return True
        else:
            print(f"Error al crear participante: {query.lastError().text()}")
            return False
    
    @staticmethod
    def obtener_todos(filtro=None):
        """
        Obtiene todos los participantes con filtro opcional.
        
        Args:
            filtro (str, optional): 'jugadores', 'arbitros' o None para todos
            
        Returns:
            list: Lista de objetos Participante
        """
        participantes = []
        query = QSqlQuery()
        
        if filtro == 'jugadores':
            sql = "SELECT * FROM participantes WHERE es_jugador = 1 ORDER BY nombre"
        elif filtro == 'arbitros':
            sql = "SELECT * FROM participantes WHERE es_arbitro = 1 ORDER BY nombre"
        else:
            sql = "SELECT * FROM participantes ORDER BY nombre"
        
        query.exec(sql)
        
        while query.next():
            participante = Participante(
                id=query.value(0),
                nombre=query.value(1),
                fecha_nacimiento=query.value(2),
                curso=query.value(3),
                es_jugador=bool(query.value(4)),
                es_arbitro=bool(query.value(5)),
                posicion=query.value(6),
                equipo_id=query.value(7),
                goles=query.value(8),
                t_amarillas=query.value(9),
                t_rojas=query.value(10)
            )
            participantes.append(participante)
        
        return participantes
    
    @staticmethod
    def obtener_por_id(participante_id):
        """
        Obtiene un participante por su ID.
        
        Args:
            participante_id (int): ID del participante
            
        Returns:
            Participante: Objeto Participante o None
        """
        query = QSqlQuery()
        query.prepare("SELECT * FROM participantes WHERE id = ?")
        query.addBindValue(participante_id)
        
        if query.exec() and query.next():
            return Participante(
                id=query.value(0),
                nombre=query.value(1),
                fecha_nacimiento=query.value(2),
                curso=query.value(3),
                es_jugador=bool(query.value(4)),
                es_arbitro=bool(query.value(5)),
                posicion=query.value(6),
                equipo_id=query.value(7),
                goles=query.value(8),
                t_amarillas=query.value(9),
                t_rojas=query.value(10)
            )
        return None
    
    @staticmethod
    def actualizar(participante_id, nombre, fecha_nacimiento, curso, es_jugador,
                   es_arbitro, posicion="", equipo_id=None):
        """
        Actualiza los datos de un participante.
        
        Returns:
            bool: True si se actualizó correctamente
        """
        query = QSqlQuery()
        query.prepare("""
            UPDATE participantes 
            SET nombre = ?, fecha_nacimiento = ?, curso = ?, es_jugador = ?,
                es_arbitro = ?, posicion = ?, equipo_id = ?
            WHERE id = ?
        """)
        query.addBindValue(nombre)
        query.addBindValue(fecha_nacimiento)
        query.addBindValue(curso)
        query.addBindValue(1 if es_jugador else 0)
        query.addBindValue(1 if es_arbitro else 0)
        query.addBindValue(posicion if posicion else None)
        query.addBindValue(equipo_id if equipo_id else None)
        query.addBindValue(participante_id)
        
        if query.exec():
            obtener_db().commit()
            return True
        else:
            print(f"Error al actualizar participante: {query.lastError().text()}")
            return False
    
    @staticmethod
    def eliminar(participante_id):
        """
        Elimina un participante de la base de datos.
        
        Returns:
            bool: True si se eliminó correctamente
        """
        query = QSqlQuery()
        query.prepare("DELETE FROM participantes WHERE id = ?")
        query.addBindValue(participante_id)
        
        if query.exec():
            obtener_db().commit()
            return True
        else:
            print(f"Error al eliminar participante: {query.lastError().text()}")
            return False
    
    @staticmethod
    def actualizar_estadisticas(participante_id, goles, t_amarillas, t_rojas, sumar=False):
        """
        Actualiza las estadísticas de un participante.
        
        Args:
            sumar: Si True, suma los valores. Si False, establece los valores directamente.
        
        Returns:
            bool: True si se actualizó correctamente
        """
        query = QSqlQuery()
        if sumar:
            query.prepare("""
                UPDATE participantes 
                SET goles = goles + ?, t_amarillas = t_amarillas + ?, t_rojas = t_rojas + ?
                WHERE id = ?
            """)
        else:
            query.prepare("""
                UPDATE participantes 
                SET goles = ?, t_amarillas = ?, t_rojas = ?
                WHERE id = ?
            """)
        query.addBindValue(goles)
        query.addBindValue(t_amarillas)
        query.addBindValue(t_rojas)
        query.addBindValue(participante_id)
        
        if query.exec():
            obtener_db().commit()
            return True
        else:
            print(f"Error al actualizar estadísticas: {query.lastError().text()}")
            return False
    
    @staticmethod
    def obtener_goleadores(limite=10):
        """
        Obtiene los máximos goleadores.
        
        Args:
            limite (int): Número máximo de resultados
            
        Returns:
            list: Lista de diccionarios con datos de goleadores
        """
        goleadores = []
        query = QSqlQuery()
        query.prepare("""
            SELECT id, nombre, goles, equipo_id
            FROM participantes
            WHERE es_jugador = 1
            ORDER BY goles DESC
            LIMIT ?
        """)
        query.addBindValue(limite)
        
        if query.exec():
            while query.next():
                goleadores.append({
                    'id': query.value(0),
                    'nombre': query.value(1),
                    'goles': query.value(2),
                    'equipo_id': query.value(3)
                })
        
        return goleadores
    
    @staticmethod
    def obtener_por_tarjetas(tipo='amarillas', limite=10):
        """
        Obtiene jugadores ordenados por tarjetas.
        
        Args:
            tipo (str): 'amarillas' o 'rojas'
            limite (int): Número máximo de resultados
            
        Returns:
            list: Lista de diccionarios con datos de jugadores
        """
        jugadores = []
        query = QSqlQuery()
        
        campo = 't_amarillas' if tipo == 'amarillas' else 't_rojas'
        query.prepare(f"""
            SELECT id, nombre, {campo}, equipo_id
            FROM participantes
            WHERE es_jugador = 1
            ORDER BY {campo} DESC
            LIMIT ?
        """)
        query.addBindValue(limite)
        
        if query.exec():
            while query.next():
                jugadores.append({
                    'id': query.value(0),
                    'nombre': query.value(1),
                    'tarjetas': query.value(2),
                    'equipo_id': query.value(3)
                })
        
        return jugadores
    
    def __str__(self):
        """Representación en string del participante."""
        tipo = []
        if self.es_jugador:
            tipo.append("Jugador")
        if self.es_arbitro:
            tipo.append("Árbitro")
        return f"{self.nombre} - {'/'.join(tipo)}"
