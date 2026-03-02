"""
Componente RelojDigital
Widget reutilizable que puede funcionar como reloj, temporizador o cronómetro
"""
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QTimer, QTime, Signal, Property
from datetime import datetime, time
from .reloj_digital_ui import Ui_RelojDigital
from models.reloj_model import ClockMode, TimerDirection
from resources.translations import translate


class RelojDigital(QWidget):
    """
    Widget de reloj digital con múltiples modos de funcionamiento:
    - Reloj: muestra la hora actual con posibilidad de alarma
    - Timer: funciona como temporizador/cronómetro
    """
    
    # Señales personalizadas
    alarmTriggered = Signal(str)  # Se emite cuando salta la alarma (con mensaje)
    timerFinished = Signal()      # Se emite cuando el temporizador llega a 0
    
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.app = app
        self.ui = Ui_RelojDigital()
        self.ui.setupUi(self)
        
        # Variables de configuración - MODO CRONÓMETRO POR DEFECTO
        self._mode = ClockMode.TIMER
        self._format_24h = True
        self._alarm_enabled = False
        self._alarm_hour = 0
        self._alarm_minute = 0
        self._alarm_message = "¡Alarma!"
        self._alarm_triggered_today = False
        
        # Variables para temporizador - CRONÓMETRO PROGRESIVO
        self._timer_direction = TimerDirection.PROGRESSIVE
        self._timer_duration = 0  # Duración en segundos
        self._timer_current = 0   # Tiempo actual en segundos
        self._timer_running = False
        
        # Timer interno para actualizar la pantalla
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_display)
        
        # Conectar botones
        self.ui.btnStart.clicked.connect(self._on_start)
        self.ui.btnPause.clicked.connect(self._on_pause)
        self.ui.btnReset.clicked.connect(self._on_reset)
        
        # Inicializar en modo cronómetro
        self._update_button_states()
        self._update_mode_label()
        self._update_display()
    
    def tr(self, text):
        """Traduce un texto según el idioma actual"""
        return translate(text, self.app.current_language)
    
    def retranslate_ui(self):
        """Actualiza todos los textos del widget"""
        self.ui.btnStart.setText(self.tr("Iniciar"))
        self.ui.btnPause.setText(self.tr("Pausar"))
        self.ui.btnReset.setText(self.tr("Reiniciar"))
        self._update_mode_label()
        
    def _update_display(self):
        """Actualiza el display según el modo actual"""
        if self._mode == ClockMode.CLOCK:
            self._update_clock_display()
        elif self._mode == ClockMode.TIMER:
            self._update_timer_display()
    
    def _update_clock_display(self):
        """Actualiza el display en modo reloj"""
        now = datetime.now()
        
        if self._format_24h:
            time_str = now.strftime("%H:%M:%S")
        else:
            time_str = now.strftime("%I:%M:%S")
            
        self.ui.lcdDisplay.display(time_str)
        
        # Verificar alarma
        if self._alarm_enabled and not self._alarm_triggered_today:
            if now.hour == self._alarm_hour and now.minute == self._alarm_minute:
                self._trigger_alarm()
                
        # Resetear flag de alarma al cambiar de día
        if now.hour == 0 and now.minute == 0:
            self._alarm_triggered_today = False
    
    def _update_timer_display(self):
        """Actualiza el display en modo temporizador"""
        if self._timer_running:
            if self._timer_direction == TimerDirection.PROGRESSIVE:
                self._timer_current += 1
            else:  # REGRESSIVE
                self._timer_current -= 1
                if self._timer_current <= 0:
                    self._timer_current = 0
                    self._on_pause()
                    self.timerFinished.emit()
        
        # Formatear tiempo
        hours = self._timer_current // 3600
        minutes = (self._timer_current % 3600) // 60
        seconds = self._timer_current % 60
        
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.ui.lcdDisplay.display(time_str)
    
    def _trigger_alarm(self):
        """Dispara la alarma"""
        self._alarm_triggered_today = True
        self.alarmTriggered.emit(self._alarm_message)
    
    def _on_start(self):
        """Maneja el botón de inicio"""
        if self._mode == ClockMode.TIMER:
            self._timer_running = True
            if not self.timer.isActive():
                self.timer.start(1000)  # Actualizar cada segundo
        self._update_button_states()
    
    def _on_pause(self):
        """Maneja el botón de pausa"""
        if self._mode == ClockMode.TIMER:
            self._timer_running = False
        self._update_button_states()
    
    def _on_reset(self):
        """Maneja el botón de reinicio"""
        if self._mode == ClockMode.TIMER:
            self._timer_running = False
            if self._timer_direction == TimerDirection.PROGRESSIVE:
                self._timer_current = 0
            else:
                self._timer_current = self._timer_duration
            self._update_display()
        elif self._mode == ClockMode.CLOCK:
            self._alarm_triggered_today = False
        self._update_button_states()
    
    def _update_button_states(self):
        """Actualiza el estado de los botones según el modo y estado"""
        if self._mode == ClockMode.CLOCK:
            # En modo reloj, deshabilitar controles de timer
            self.ui.btnStart.setEnabled(False)
            self.ui.btnPause.setEnabled(False)
            self.ui.btnReset.setEnabled(self._alarm_enabled)
        else:  # TIMER
            self.ui.btnStart.setEnabled(not self._timer_running)
            self.ui.btnPause.setEnabled(self._timer_running)
            self.ui.btnReset.setEnabled(True)
    
    def _update_mode_label(self):
        """Actualiza la etiqueta del modo"""
        if self._mode == ClockMode.CLOCK:
            mode_text = f"{self.tr('Modo')}: {self.tr('Reloj')}"
        else:
            if self._timer_direction == TimerDirection.PROGRESSIVE:
                mode_text = f"{self.tr('Modo')}: {self.tr('Cronómetro')}"
            else:
                mode_text = f"{self.tr('Modo')}: {self.tr('Temporizador')}"
        self.ui.lblMode.setText(mode_text)
    
    # ============= PROPIEDADES PÚBLICAS =============
    
    def get_mode(self):
        """Obtiene el modo actual"""
        return self._mode
    
    def set_mode(self, mode: ClockMode):
        """Establece el modo de funcionamiento"""
        if not isinstance(mode, ClockMode):
            return
        
        self._mode = mode
        
        # Detener timer actual si estaba corriendo
        if self.timer.isActive():
            self.timer.stop()
        
        if mode == ClockMode.CLOCK:
            # Iniciar timer para actualizar reloj
            self.timer.start(1000)
        
        self._update_button_states()
        self._update_mode_label()
        self._update_display()
    
    mode = Property(ClockMode, get_mode, set_mode)
    
    def get_format_24h(self):
        """Obtiene si el formato es de 24 horas"""
        return self._format_24h
    
    def set_format_24h(self, value: bool):
        """Establece el formato de 12 o 24 horas"""
        self._format_24h = value
        if self._mode == ClockMode.CLOCK:
            self._update_display()
    
    format24h = Property(bool, get_format_24h, set_format_24h)
    
    def get_alarm_enabled(self):
        """Obtiene si la alarma está habilitada"""
        return self._alarm_enabled
    
    def set_alarm_enabled(self, value: bool):
        """Habilita o deshabilita la alarma"""
        self._alarm_enabled = value
        self._alarm_triggered_today = False
        self._update_button_states()
    
    alarmEnabled = Property(bool, get_alarm_enabled, set_alarm_enabled)
    
    def get_alarm_hour(self):
        """Obtiene la hora de la alarma"""
        return self._alarm_hour
    
    def set_alarm_hour(self, hour: int):
        """Establece la hora de la alarma (0-23)"""
        if 0 <= hour <= 23:
            self._alarm_hour = hour
            self._alarm_triggered_today = False
    
    alarmHour = Property(int, get_alarm_hour, set_alarm_hour)
    
    def get_alarm_minute(self):
        """Obtiene los minutos de la alarma"""
        return self._alarm_minute
    
    def set_alarm_minute(self, minute: int):
        """Establece los minutos de la alarma (0-59)"""
        if 0 <= minute <= 59:
            self._alarm_minute = minute
            self._alarm_triggered_today = False
    
    alarmMinute = Property(int, get_alarm_minute, set_alarm_minute)
    
    def get_alarm_message(self):
        """Obtiene el mensaje de la alarma"""
        return self._alarm_message
    
    def set_alarm_message(self, message: str):
        """Establece el mensaje de la alarma"""
        self._alarm_message = message
    
    alarmMessage = Property(str, get_alarm_message, set_alarm_message)
    
    def get_timer_duration(self):
        """Obtiene la duración del temporizador en segundos"""
        return self._timer_duration
    
    def set_timer_duration(self, seconds: int):
        """Establece la duración del temporizador en segundos"""
        if seconds >= 0:
            self._timer_duration = seconds
            if self._timer_direction == TimerDirection.REGRESSIVE:
                self._timer_current = seconds
            self._update_display()
    
    timerDuration = Property(int, get_timer_duration, set_timer_duration)
    
    def get_timer_direction(self):
        """Obtiene la dirección del temporizador"""
        return self._timer_direction
    
    def set_timer_direction(self, direction: TimerDirection):
        """Establece la dirección del temporizador"""
        if not isinstance(direction, TimerDirection):
            return
        self._timer_direction = direction
        if direction == TimerDirection.REGRESSIVE:
            self._timer_current = self._timer_duration
        else:
            self._timer_current = 0
        self._update_mode_label()
        self._update_display()
    
    timerDirection = Property(TimerDirection, get_timer_direction, set_timer_direction)
    
    # ============= MÉTODOS PÚBLICOS =============
    
    def start_timer(self):
        """Inicia el temporizador/cronómetro"""
        if self._mode == ClockMode.TIMER:
            self._on_start()
    
    def pause_timer(self):
        """Pausa el temporizador/cronómetro"""
        if self._mode == ClockMode.TIMER:
            self._on_pause()
    
    def reset_timer(self):
        """Reinicia el temporizador/cronómetro"""
        if self._mode == ClockMode.TIMER:
            self._on_reset()
    
    def get_current_time(self):
        """Obtiene el tiempo actual del temporizador en segundos"""
        return self._timer_current
    
    def set_timer_time(self, hours: int, minutes: int, seconds: int):
        """Establece un tiempo específico para el temporizador"""
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self.set_timer_duration(total_seconds)
