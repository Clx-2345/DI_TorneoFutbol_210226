"""
Modelo para la gestión de Eventos de Partido en tiempo real.

Este módulo registra eventos (goles, tarjetas) con su timestamp durante el partido.

Autor: Sistema
Versión: 1.0.0
Fecha: Febrero 2026
"""

from PySide6.QtSql import QSqlQuery
from models.database import obtener_db


class EventoPartido:
    """
    Clase para gestionar eventos en tiempo real durante un partido.
    
    Attributes:
        id (int): Identificador único
        partido_id (int): ID del partido
        jugador_id (int): ID del jugador (si aplica)
        tipo_evento (str): Tipo de evento ('gol', 'amarilla', 'roja')
        minuto (int): Minuto del partido cuando ocurrió el evento
        descripcion (str): Descripción adicional del evento
    """
    
    def __init__(self, id=None, partido_id=None, jugador_id=None,
                 tipo_evento="", minuto=0, descripcion=""):
        """Inicializa un objeto EventoPartido."""
        self.id = id
        self.partido_id = partido_id
        self.jugador_id = jugador_id
        self.tipo_evento = tipo_evento
        self.minuto = minuto
        self.descripcion = descripcion
    
    @staticmethod
    def crear_tabla():
        """Crea la tabla de eventos si no existe."""
        query = QSqlQuery()
        query.exec("""
            CREATE TABLE IF NOT EXISTS eventos_partido (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                partido_id INTEGER NOT NULL,
                jugador_id INTEGER,
                tipo_evento TEXT NOT NULL,
                minuto INTEGER NOT NULL,
                descripcion TEXT,
                FOREIGN KEY (partido_id) REFERENCES partidos(id),
                FOREIGN KEY (jugador_id) REFERENCES participantes(id)
            )
        """)
        obtener_db().commit()
    
    @staticmethod
    def registrar(partido_id, jugador_id, tipo_evento, minuto, descripcion=""):
        """
        Registra un evento en un partido.
        
        Args:
            partido_id (int): ID del partido
            jugador_id (int): ID del jugador (puede ser None)
            tipo_evento (str): Tipo ('gol', 'amarilla', 'roja')
            minuto (int): Minuto del partido
            descripcion (str): Descripción adicional
            
        Returns:
            int: ID del evento creado o None si hay error
        """
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO eventos_partido 
            (partido_id, jugador_id, tipo_evento, minuto, descripcion)
            VALUES (?, ?, ?, ?, ?)
        """)
        query.addBindValue(partido_id)
        query.addBindValue(jugador_id if jugador_id else None)
        query.addBindValue(tipo_evento)
        query.addBindValue(minuto)
        query.addBindValue(descripcion)
        
        if query.exec():
            obtener_db().commit()
            return query.lastInsertId()
        else:
            print(f"Error al registrar evento: {query.lastError().text()}")
            return None
    
    @staticmethod
    def obtener_por_partido(partido_id):
        """
        Obtiene todos los eventos de un partido ordenados por minuto.
        
        Args:
            partido_id (int): ID del partido
            
        Returns:
            list: Lista de diccionarios con eventos
        """
        eventos = []
        query = QSqlQuery()
        query.prepare("""
            SELECT 
                e.id, e.partido_id, e.jugador_id, e.tipo_evento, 
                e.minuto, e.descripcion,
                p.nombre as jugador_nombre
            FROM eventos_partido e
            LEFT JOIN participantes p ON e.jugador_id = p.id
            WHERE e.partido_id = ?
            ORDER BY e.minuto ASC
        """)
        query.addBindValue(partido_id)
        
        if query.exec():
            while query.next():
                eventos.append({
                    'id': query.value(0),
                    'partido_id': query.value(1),
                    'jugador_id': query.value(2),
                    'tipo_evento': query.value(3),
                    'minuto': query.value(4),
                    'descripcion': query.value(5),
                    'jugador_nombre': query.value(6) or "N/A"
                })
        
        return eventos
    
    @staticmethod
    def eliminar_por_id(evento_id):
        """
        Elimina un evento específico.
        
        Args:
            evento_id (int): ID del evento a eliminar
            
        Returns:
            bool: True si se eliminó correctamente
        """
        query = QSqlQuery()
        query.prepare("DELETE FROM eventos_partido WHERE id = ?")
        query.addBindValue(evento_id)
        
        if query.exec():
            obtener_db().commit()
            return True
        return False
    
    @staticmethod
    def limpiar_eventos_partido(partido_id):
        """
        Elimina todos los eventos de un partido.
        
        Args:
            partido_id (int): ID del partido
            
        Returns:
            bool: True si se eliminaron correctamente
        """
        query = QSqlQuery()
        query.prepare("DELETE FROM eventos_partido WHERE partido_id = ?")
        query.addBindValue(partido_id)
        
        if query.exec():
            obtener_db().commit()
            return True
        return False
