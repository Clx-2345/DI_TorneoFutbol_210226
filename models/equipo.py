"""
Modelo para la gestión de Equipos en el torneo.

Este módulo contiene la clase Equipo que maneja todas las operaciones
CRUD (Crear, Leer, Actualizar, Eliminar) para la tabla equipos.

Autor: [Tu Nombre]
Versión: 1.0.0
Fecha: Enero 2026
"""

from PySide6.QtSql import QSqlQuery
from datetime import datetime
from models.database import obtener_db


class Equipo:
    """
    Clase para gestionar operaciones de equipos en la base de datos.
    
    Attributes:
        id (int): Identificador único del equipo
        nombre (str): Nombre del equipo
        curso (str): Curso al que pertenece el equipo
        color_camiseta (str): Color de la camiseta del equipo
        emblema_path (str): Ruta al archivo del emblema/logo
        emblema_blob (bytes): Imagen del emblema en formato binario
        info_adicional (str): Información adicional del equipo
    """
    
    def __init__(self, id=None, nombre="", curso="", color_camiseta="", 
                 emblema_path="", emblema_blob=None, info_adicional=""):
        """
        Inicializa un objeto Equipo.
        
        Args:
            id (int, optional): ID del equipo
            nombre (str): Nombre del equipo
            curso (str): Curso del equipo
            color_camiseta (str): Color de camiseta
            emblema_path (str): Ruta del emblema
            emblema_blob (bytes): Imagen del emblema en bytes
            info_adicional (str): Información adicional
        """
        self.id = id
        self.nombre = nombre
        self.curso = curso
        self.color_camiseta = color_camiseta
        self.emblema_path = emblema_path
        self.emblema_blob = emblema_blob
        self.info_adicional = info_adicional
    
    @staticmethod
    def crear(nombre, curso, color_camiseta, emblema_path="", emblema_blob=None, info_adicional=""):
        """
        Crea un nuevo equipo en la base de datos.
        
        Args:
            nombre (str): Nombre del equipo
            curso (str): Curso del equipo
            color_camiseta (str): Color de camiseta
            emblema_path (str, optional): Ruta del emblema
            emblema_blob (bytes, optional): Imagen del emblema en bytes
            info_adicional (str, optional): Información adicional
            
        Returns:
            bool: True si se creó correctamente, False en caso contrario
        """
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO equipos (nombre, curso, color_camiseta, emblema_path, emblema_blob, info_adicional)
            VALUES (?, ?, ?, ?, ?, ?)
        """)
        query.addBindValue(nombre)
        query.addBindValue(curso)
        query.addBindValue(color_camiseta)
        query.addBindValue(emblema_path)
        query.addBindValue(emblema_blob)
        query.addBindValue(info_adicional)
        
        if query.exec():
            obtener_db().commit()
            return True
        else:
            print(f"Error al crear equipo: {query.lastError().text()}")
            return False
    
    @staticmethod
    def obtener_todos():
        """
        Obtiene todos los equipos de la base de datos.
        
        Returns:
            list: Lista de objetos Equipo
        """
        equipos = []
        query = QSqlQuery()
        query.exec("SELECT * FROM equipos ORDER BY nombre")
        
        while query.next():
            equipo = Equipo(
                id=query.value(0),
                nombre=query.value(1),
                curso=query.value(2),
                color_camiseta=query.value(3),
                emblema_path=query.value(4),
                emblema_blob=query.value(5),
                info_adicional=query.value(6)
            )
            equipos.append(equipo)
        
        return equipos
    
    @staticmethod
    def obtener_por_id(equipo_id):
        """
        Obtiene un equipo por su ID.
        
        Args:
            equipo_id (int): ID del equipo
            
        Returns:
            Equipo: Objeto Equipo o None si no existe
        """
        query = QSqlQuery()
        query.prepare("SELECT * FROM equipos WHERE id = ?")
        query.addBindValue(equipo_id)
        
        if query.exec() and query.next():
            return Equipo(
                id=query.value(0),
                nombre=query.value(1),
                curso=query.value(2),
                color_camiseta=query.value(3),
                emblema_path=query.value(4),
                emblema_blob=query.value(5),
                info_adicional=query.value(6)
            )
        return None
    
    @staticmethod
    def actualizar(equipo_id, nombre, curso, color_camiseta, emblema_path="", emblema_blob=None, info_adicional=""):
        """
        Actualiza los datos de un equipo existente.
        
        Args:
            equipo_id (int): ID del equipo a actualizar
            nombre (str): Nuevo nombre
            curso (str): Nuevo curso
            color_camiseta (str): Nuevo color
            emblema_path (str, optional): Nueva ruta del emblema (legacy)
            emblema_blob (bytes, optional): Nueva imagen del emblema en formato BLOB
            info_adicional (str, optional): Nueva información adicional
            
        Returns:
            bool: True si se actualizó correctamente
        """
        query = QSqlQuery()
        query.prepare("""
            UPDATE equipos 
            SET nombre = ?, curso = ?, color_camiseta = ?, emblema_path = ?, emblema_blob = ?, info_adicional = ?
            WHERE id = ?
        """)
        query.addBindValue(nombre)
        query.addBindValue(curso)
        query.addBindValue(color_camiseta)
        query.addBindValue(emblema_path)
        query.addBindValue(emblema_blob)
        query.addBindValue(info_adicional)
        query.addBindValue(equipo_id)
        
        if query.exec():
            obtener_db().commit()
            return True
        else:
            print(f"Error al actualizar equipo: {query.lastError().text()}")
            return False
    
    @staticmethod
    def eliminar(equipo_id):
        """
        Elimina un equipo de la base de datos.
        
        Args:
            equipo_id (int): ID del equipo a eliminar
            
        Returns:
            bool: True si se eliminó correctamente
        """
        query = QSqlQuery()
        query.prepare("DELETE FROM equipos WHERE id = ?")
        query.addBindValue(equipo_id)
        
        if query.exec():
            obtener_db().commit()
            return True
        else:
            print(f"Error al eliminar equipo: {query.lastError().text()}")
            return False
    
    @staticmethod
    def obtener_jugadores(equipo_id):
        """
        Obtiene todos los jugadores de un equipo.
        
        Args:
            equipo_id (int): ID del equipo
            
        Returns:
            list: Lista de diccionarios con datos de jugadores
        """
        jugadores = []
        query = QSqlQuery()
        query.prepare("""
            SELECT id, nombre, posicion, goles, t_amarillas, t_rojas
            FROM participantes
            WHERE equipo_id = ? AND es_jugador = 1
            ORDER BY nombre
        """)
        query.addBindValue(equipo_id)
        
        if query.exec():
            while query.next():
                jugadores.append({
                    'id': query.value(0),
                    'nombre': query.value(1),
                    'posicion': query.value(2),
                    'goles': query.value(3),
                    't_amarillas': query.value(4),
                    't_rojas': query.value(5)
                })
        
        return jugadores
    
    def __str__(self):
        """Representación en string del equipo."""
        return f"Equipo: {self.nombre} - {self.curso}"
    
    def __repr__(self):
        """Representación para debugging."""
        return f"Equipo(id={self.id}, nombre='{self.nombre}', curso='{self.curso}')"
