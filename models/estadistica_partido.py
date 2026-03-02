"""
Modelo para la gestión de Estadísticas de Partidos.

Este módulo contiene la clase EstadisticaPartido que maneja las estadísticas
individuales de jugadores por partido.

Autor: [Tu Nombre]
Versión: 1.0.0
Fecha: Enero 2026
"""

from PySide6.QtSql import QSqlQuery
from models.database import obtener_db
from models.database import obtener_db


class EstadisticaPartido:
    """
    Clase para gestionar estadísticas individuales por partido.
    
    Attributes:
        id (int): Identificador único
        partido_id (int): ID del partido
        jugador_id (int): ID del jugador
        goles (int): Goles marcados
        t_amarillas (int): Tarjetas amarillas recibidas
        t_rojas (int): Tarjetas rojas recibidas
    """
    
    def __init__(self, id=None, partido_id=None, jugador_id=None,
                 goles=0, t_amarillas=0, t_rojas=0):
        """Inicializa un objeto EstadisticaPartido."""
        self.id = id
        self.partido_id = partido_id
        self.jugador_id = jugador_id
        self.goles = goles
        self.t_amarillas = t_amarillas
        self.t_rojas = t_rojas
    
    @staticmethod
    def registrar(partido_id, jugador_id, goles, t_amarillas, t_rojas):
        """
        Registra o actualiza estadísticas de un jugador en un partido.
        
        Returns:
            bool: True si se registró correctamente
        """
        # Primero verificar si ya existe
        query = QSqlQuery()
        query.prepare("""
            SELECT id FROM estadisticas_partido 
            WHERE partido_id = ? AND jugador_id = ?
        """)
        query.addBindValue(partido_id)
        query.addBindValue(jugador_id)
        
        existe = False
        if query.exec() and query.next():
            existe = True
            estadistica_id = query.value(0)
        
        if existe:
            # Actualizar existente
            query.prepare("""
                UPDATE estadisticas_partido 
                SET goles = ?, t_amarillas = ?, t_rojas = ?
                WHERE id = ?
            """)
            query.addBindValue(goles)
            query.addBindValue(t_amarillas)
            query.addBindValue(t_rojas)
            query.addBindValue(estadistica_id)
        else:
            # Crear nueva
            query.prepare("""
                INSERT INTO estadisticas_partido 
                (partido_id, jugador_id, goles, t_amarillas, t_rojas)
                VALUES (?, ?, ?, ?, ?)
            """)
            query.addBindValue(partido_id)
            query.addBindValue(jugador_id)
            query.addBindValue(goles)
            query.addBindValue(t_amarillas)
            query.addBindValue(t_rojas)
        
        if query.exec():
            obtener_db().commit()
            return True
        else:
            print(f"Error al registrar estadística: {query.lastError().text()}")
            return False
    
    @staticmethod
    def obtener_por_partido(partido_id):
        """
        Obtiene todas las estadísticas de un partido.
        
        Args:
            partido_id (int): ID del partido
            
        Returns:
            list: Lista de diccionarios con estadísticas
        """
        estadisticas = []
        query = QSqlQuery()
        query.prepare("""
            SELECT 
                ep.id, ep.jugador_id, ep.goles, ep.t_amarillas, ep.t_rojas,
                p.nombre as jugador_nombre
            FROM estadisticas_partido ep
            LEFT JOIN participantes p ON ep.jugador_id = p.id
            WHERE ep.partido_id = ?
        """)
        query.addBindValue(partido_id)
        
        if query.exec():
            while query.next():
                estadisticas.append({
                    'id': query.value(0),
                    'jugador_id': query.value(1),
                    'goles': query.value(2),
                    't_amarillas': query.value(3),
                    't_rojas': query.value(4),
                    'jugador_nombre': query.value(5)
                })
        
        return estadisticas
    
    @staticmethod
    def obtener_por_jugador(jugador_id):
        """
        Obtiene todas las estadísticas de un jugador.
        
        Args:
            jugador_id (int): ID del jugador
            
        Returns:
            list: Lista de diccionarios con estadísticas por partido
        """
        estadisticas = []
        query = QSqlQuery()
        query.prepare("""
            SELECT 
                ep.id, ep.partido_id, ep.goles, ep.t_amarillas, ep.t_rojas,
                p.fecha, p.eliminatoria
            FROM estadisticas_partido ep
            LEFT JOIN partidos p ON ep.partido_id = p.id
            WHERE ep.jugador_id = ?
            ORDER BY p.fecha DESC
        """)
        query.addBindValue(jugador_id)
        
        if query.exec():
            while query.next():
                estadisticas.append({
                    'id': query.value(0),
                    'partido_id': query.value(1),
                    'goles': query.value(2),
                    't_amarillas': query.value(3),
                    't_rojas': query.value(4),
                    'fecha': query.value(5),
                    'eliminatoria': query.value(6)
                })
        
        return estadisticas
    
    @staticmethod
    def eliminar(estadistica_id):
        """
        Elimina una estadística.
        
        Returns:
            bool: True si se eliminó correctamente
        """
        query = QSqlQuery()
        query.prepare("DELETE FROM estadisticas_partido WHERE id = ?")
        query.addBindValue(estadistica_id)
        
        if query.exec():
            obtener_db().commit()
            return True
        return False
    
    @staticmethod
    def eliminar_por_partido(partido_id):
        """
        Elimina todas las estadísticas de un partido.
        
        Returns:
            bool: True si se eliminaron correctamente
        """
        query = QSqlQuery()
        query.prepare("DELETE FROM estadisticas_partido WHERE partido_id = ?")
        query.addBindValue(partido_id)
        
        if query.exec():
            obtener_db().commit()
            return True
        return False
