"""
Sistema de traducciones para el componente RelojDigital
Traducciones integradas sin necesidad de archivos .qm
"""

TRANSLATIONS = {
    'es': {
        # Ventana principal
        'Prueba de Reloj Digital': 'Prueba de Reloj Digital',
        'Configuración': 'Configuración',
        'Idioma': 'Idioma',
        
        # Modos
        'Modo:': 'Modo:',
        'Reloj': 'Reloj',
        'Cronómetro': 'Cronómetro',
        'Temporizador': 'Temporizador',
        
        # Opciones
        'Formato 24 horas': 'Formato 24 horas',
        'Habilitar alarma': 'Habilitar alarma',
        'Hora de alarma:': 'Hora de alarma:',
        'Minuto de alarma:': 'Minuto de alarma:',
        'Mensaje de alarma:': 'Mensaje de alarma:',
        'Duración del temporizador (segundos):': 'Duración del temporizador (segundos):',
        
        # Idiomas
        'Español': 'Español',
        'Inglés': 'Inglés',
        
        # Mensajes
        'Alarma': 'Alarma',
        '¡Alarma!': '¡Alarma!',
        '¡Tiempo finalizado!': '¡Tiempo finalizado!',
        
        # Etiquetas del reloj
        'Modo: Reloj': 'Modo: Reloj',
        'Modo: Cronómetro': 'Modo: Cronómetro',
        'Modo: Temporizador': 'Modo: Temporizador',
    },
    'en': {
        # Main window
        'Prueba de Reloj Digital': 'Digital Clock Test',
        'Configuración': 'Settings',
        'Idioma': 'Language',
        
        # Modes
        'Modo:': 'Mode:',
        'Reloj': 'Clock',
        'Cronómetro': 'Stopwatch',
        'Temporizador': 'Timer',
        
        # Options
        'Formato 24 horas': '24-hour format',
        'Habilitar alarma': 'Enable alarm',
        'Hora de alarma:': 'Alarm hour:',
        'Minuto de alarma:': 'Alarm minute:',
        'Mensaje de alarma:': 'Alarm message:',
        'Duración del temporizador (segundos):': 'Timer duration (seconds):',
        
        # Languages
        'Español': 'Spanish',
        'Inglés': 'English',
        
        # Messages
        'Alarma': 'Alarm',
        '¡Alarma!': 'Alarm!',
        '¡Tiempo finalizado!': 'Time\'s up!',
        
        # Clock labels
        'Modo: Reloj': 'Mode: Clock',
        'Modo: Cronómetro': 'Mode: Stopwatch',
        'Modo: Temporizador': 'Mode: Timer',
    }
}


def translate(text, language='es'):
    """
    Traduce un texto al idioma especificado
    
    Args:
        text: Texto a traducir
        language: Código del idioma ('es' o 'en')
        
    Returns:
        Texto traducido
    """
    if language not in TRANSLATIONS:
        return text
    
    return TRANSLATIONS[language].get(text, text)
