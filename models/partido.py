"""
Modelo para la gestión de Partidos en el torneo.

Este módulo contiene la clase Partido que maneja todas las operaciones
CRUD para la tabla partidos.

Autor: [Tu Nombre]
Versión: 1.0.0
Fecha: Enero 2026
"""

from PySide6.QtSql import QSqlQuery
from models.database import obtener_db


class Partido:
    """
    Clase para gestionar operaciones de partidos en la base de datos.
    
    Attributes:
        id (int): Identificador único del partido
        equipo_local_id (int): ID del equipo local
        equipo_visitante_id (int): ID del equipo visitante
        fecha (str): Fecha del partido
        hora (str): Hora del partido
        arbitro_id (int): ID del árbitro
        eliminatoria (str): Fase eliminatoria
        lugar (str): Lugar del partido
        goles_local (int): Goles del equipo local
        goles_visitante (int): Goles del equipo visitante
        jugado (bool): Si el partido ya se jugó
    """
    
    def __init__(self, id=None, equipo_local_id=None, equipo_visitante_id=None,
                 fecha="", hora="", arbitro_id=None, eliminatoria="", lugar="",
                 goles_local=0, goles_visitante=0, jugado=False):
        """Inicializa un objeto Partido."""
        self.id = id
        self.equipo_local_id = equipo_local_id
        self.equipo_visitante_id = equipo_visitante_id
        self.fecha = fecha
        self.hora = hora
        self.arbitro_id = arbitro_id
        self.eliminatoria = eliminatoria
        self.lugar = lugar
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante
        self.jugado = jugado
    
    @staticmethod
    def crear(equipo_local_id, equipo_visitante_id, fecha, hora, arbitro_id,
              eliminatoria, lugar=""):
        """
        Crea un nuevo partido en la base de datos.
        
        Returns:
            int: ID del partido creado o None si hay error
        """
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO partidos 
            (equipo_local_id, equipo_visitante_id, fecha, hora, arbitro_id, 
             eliminatoria, lugar)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """)
        query.addBindValue(equipo_local_id)
        query.addBindValue(equipo_visitante_id)
        query.addBindValue(fecha)
        query.addBindValue(hora)
        query.addBindValue(arbitro_id if arbitro_id else None)
        query.addBindValue(eliminatoria)
        query.addBindValue(lugar)
        
        if query.exec():
            obtener_db().commit()
            return query.lastInsertId()
        else:
            print(f"Error al crear partido: {query.lastError().text()}")
            return None
    
    @staticmethod
    def obtener_todos(solo_jugados=False, solo_pendientes=False):
        """
        Obtiene todos los partidos.
        
        Args:
            solo_jugados (bool): Solo partidos jugados
            solo_pendientes (bool): Solo partidos pendientes
            
        Returns:
            list: Lista de objetos Partido
        """
        partidos = []
        query = QSqlQuery()
        
        sql = "SELECT * FROM partidos"
        if solo_jugados:
            sql += " WHERE jugado = 1"
        elif solo_pendientes:
            sql += " WHERE jugado = 0"
        sql += " ORDER BY fecha, hora"
        
        query.exec(sql)
        
        while query.next():
            partido = Partido(
                id=query.value(0),
                equipo_local_id=query.value(1),
                equipo_visitante_id=query.value(2),
                fecha=query.value(3),
                hora=query.value(4),
                arbitro_id=query.value(5),
                eliminatoria=query.value(6),
                lugar=query.value(7),
                goles_local=query.value(8),
                goles_visitante=query.value(9),
                jugado=bool(query.value(10))
            )
            partidos.append(partido)
        
        return partidos
    
    @staticmethod
    def obtener_por_eliminatoria(eliminatoria):
        """
        Obtiene partidos de una eliminatoria específica.
        
        Args:
            eliminatoria (str): Nombre de la eliminatoria
            
        Returns:
            list: Lista de objetos Partido
        """
        partidos = []
        query = QSqlQuery()
        query.prepare("""
            SELECT * FROM partidos 
            WHERE eliminatoria = ?
            ORDER BY fecha, hora
        """)
        query.addBindValue(eliminatoria)
        
        if query.exec():
            while query.next():
                partido = Partido(
                    id=query.value(0),
                    equipo_local_id=query.value(1),
                    equipo_visitante_id=query.value(2),
                    fecha=query.value(3),
                    hora=query.value(4),
                    arbitro_id=query.value(5),
                    eliminatoria=query.value(6),
                    lugar=query.value(7),
                    goles_local=query.value(8),
                    goles_visitante=query.value(9),
                    jugado=bool(query.value(10))
                )
                partidos.append(partido)
        
        return partidos
    
    @staticmethod
    def obtener_por_id(partido_id):
        """
        Obtiene un partido por su ID.
        
        Args:
            partido_id (int): ID del partido
            
        Returns:
            Partido: Objeto Partido o None
        """
        query = QSqlQuery()
        query.prepare("SELECT * FROM partidos WHERE id = ?")
        query.addBindValue(partido_id)
        
        if query.exec() and query.next():
            return Partido(
                id=query.value(0),
                equipo_local_id=query.value(1),
                equipo_visitante_id=query.value(2),
                fecha=query.value(3),
                hora=query.value(4),
                arbitro_id=query.value(5),
                eliminatoria=query.value(6),
                lugar=query.value(7),
                goles_local=query.value(8),
                goles_visitante=query.value(9),
                jugado=bool(query.value(10))
            )
        return None
    
    @staticmethod
    def actualizar(partido_id, equipo_local_id, equipo_visitante_id, fecha, hora,
                   arbitro_id, eliminatoria, lugar=""):
        """
        Actualiza los datos de un partido.
        
        Returns:
            bool: True si se actualizó correctamente
        """
        query = QSqlQuery()
        query.prepare("""
            UPDATE partidos 
            SET equipo_local_id = ?, equipo_visitante_id = ?, fecha = ?, hora = ?,
                arbitro_id = ?, eliminatoria = ?, lugar = ?
            WHERE id = ?
        """)
        query.addBindValue(equipo_local_id)
        query.addBindValue(equipo_visitante_id)
        query.addBindValue(fecha)
        query.addBindValue(hora)
        query.addBindValue(arbitro_id if arbitro_id else None)
        query.addBindValue(eliminatoria)
        query.addBindValue(lugar)
        query.addBindValue(partido_id)
        
        if query.exec():
            obtener_db().commit()
            return True
        else:
            print(f"Error al actualizar partido: {query.lastError().text()}")
            return False
    
    @staticmethod
    def eliminar(partido_id):
        """
        Elimina un partido de la base de datos.
        
        Returns:
            bool: True si se eliminó correctamente
        """
        query = QSqlQuery()
        query.prepare("DELETE FROM partidos WHERE id = ?")
        query.addBindValue(partido_id)
        
        if query.exec():
            obtener_db().commit()
            return True
        else:
            print(f"Error al eliminar partido: {query.lastError().text()}")
            return False
    
    @staticmethod
    def registrar_resultado(partido_id, goles_local, goles_visitante):
        """
        Registra el resultado de un partido.
        
        Args:
            partido_id (int): ID del partido
            goles_local (int): Goles del equipo local
            goles_visitante (int): Goles del equipo visitante
            
        Returns:
            bool: True si se registró correctamente
        """
        query = QSqlQuery()
        query.prepare("""
            UPDATE partidos 
            SET goles_local = ?, goles_visitante = ?, jugado = 1
            WHERE id = ?
        """)
        query.addBindValue(goles_local)
        query.addBindValue(goles_visitante)
        query.addBindValue(partido_id)
        
        if query.exec():
            return True
        else:
            print(f"Error al registrar resultado: {query.lastError().text()}")
            return False
    
    @staticmethod
    def obtener_ganadores_eliminatoria(eliminatoria):
        """
        Obtiene los equipos ganadores de una eliminatoria.
        
        Args:
            eliminatoria (str): Nombre de la eliminatoria
            
        Returns:
            list: Lista de IDs de equipos ganadores
        """
        ganadores = []
        query = QSqlQuery()
        query.prepare("""
            SELECT 
                CASE 
                    WHEN goles_local > goles_visitante THEN equipo_local_id
                    WHEN goles_visitante > goles_local THEN equipo_visitante_id
                    ELSE NULL
                END as ganador
            FROM partidos
            WHERE eliminatoria = ? AND jugado = 1
        """)
        query.addBindValue(eliminatoria)
        
        if query.exec():
            while query.next():
                ganador_id = query.value(0)
                if ganador_id is not None:
                    ganadores.append(ganador_id)
        
        return ganadores
    
    @staticmethod
    def obtener_detalle_completo(partido_id):
        """
        Obtiene información completa de un partido con nombres de equipos y árbitro.
        
        Args:
            partido_id (int): ID del partido
            
        Returns:
            dict: Diccionario con toda la información del partido
        """
        query = QSqlQuery()
        query.prepare("""
            SELECT 
                p.id, p.fecha, p.hora, p.eliminatoria, p.lugar,
                p.goles_local, p.goles_visitante, p.jugado,
                el.nombre as equipo_local, ev.nombre as equipo_visitante,
                a.nombre as arbitro
            FROM partidos p
            LEFT JOIN equipos el ON p.equipo_local_id = el.id
            LEFT JOIN equipos ev ON p.equipo_visitante_id = ev.id
            LEFT JOIN participantes a ON p.arbitro_id = a.id
            WHERE p.id = ?
        """)
        query.addBindValue(partido_id)
        
        if query.exec() and query.next():
            return {
                'id': query.value(0),
                'fecha': query.value(1),
                'hora': query.value(2),
                'eliminatoria': query.value(3),
                'lugar': query.value(4),
                'goles_local': query.value(5),
                'goles_visitante': query.value(6),
                'jugado': bool(query.value(7)),
                'equipo_local': query.value(8),
                'equipo_visitante': query.value(9),
                'arbitro': query.value(10)
            }
        return None
    
    def __str__(self):
        """Representación en string del partido."""
        return f"Partido: {self.equipo_local_id} vs {self.equipo_visitante_id} - {self.eliminatoria}"
