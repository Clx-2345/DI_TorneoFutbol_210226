"""
Modelo para el componente RelojDigital
Define los enumerados y constantes necesarias
"""
from enum import Enum


class ClockMode(Enum):
    """
    Enumerado para definir los modos de funcionamiento del reloj
    """
    CLOCK = "clock"  # Modo reloj digital con hora actual
    TIMER = "timer"  # Modo temporizador/cronómetro


class TimerDirection(Enum):
    """
    Enumerado para definir la dirección del temporizador
    """
    PROGRESSIVE = "progressive"  # Cuenta hacia adelante (cronómetro)
    REGRESSIVE = "regressive"    # Cuenta hacia atrás (temporizador)
