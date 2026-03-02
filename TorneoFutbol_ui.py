# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TorneoFutbol.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateEdit, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTextEdit, QTimeEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 700)
        self.Action_Salir = QAction(MainWindow)
        self.Action_Salir.setObjectName(u"Action_Salir")
        self.Action_MenuPrincipal = QAction(MainWindow)
        self.Action_MenuPrincipal.setObjectName(u"Action_MenuPrincipal")
        self.Action_Notificaciones = QAction(MainWindow)
        self.Action_Notificaciones.setObjectName(u"Action_Notificaciones")
        self.Action_VerAyuda = QAction(MainWindow)
        self.Action_VerAyuda.setObjectName(u"Action_VerAyuda")
        self.Action_Creditos = QAction(MainWindow)
        self.Action_Creditos.setObjectName(u"Action_Creditos")
        self.Centralwidget = QWidget(MainWindow)
        self.Centralwidget.setObjectName(u"Centralwidget")
        self.Layout_Principal = QVBoxLayout(self.Centralwidget)
        self.Layout_Principal.setSpacing(0)
        self.Layout_Principal.setObjectName(u"Layout_Principal")
        self.Layout_Principal.setContentsMargins(0, 0, 0, 0)
        self.Stacked_Paginas = QStackedWidget(self.Centralwidget)
        self.Stacked_Paginas.setObjectName(u"Stacked_Paginas")
        self.Page_MenuPrincipal = QWidget()
        self.Page_MenuPrincipal.setObjectName(u"Page_MenuPrincipal")
        self.Layout_MenuPrincipal = QVBoxLayout(self.Page_MenuPrincipal)
        self.Layout_MenuPrincipal.setObjectName(u"Layout_MenuPrincipal")
        self.L_TituloApp = QLabel(self.Page_MenuPrincipal)
        self.L_TituloApp.setObjectName(u"L_TituloApp")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.L_TituloApp.setFont(font)
        self.L_TituloApp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_MenuPrincipal.addWidget(self.L_TituloApp)

        self.Spacer_MenuTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Layout_MenuPrincipal.addItem(self.Spacer_MenuTop)

        self.Layout_BotonesMenu = QGridLayout()
        self.Layout_BotonesMenu.setObjectName(u"Layout_BotonesMenu")
        self.B_GestionEquipos = QPushButton(self.Page_MenuPrincipal)
        self.B_GestionEquipos.setObjectName(u"B_GestionEquipos")
        self.B_GestionEquipos.setMinimumSize(QSize(250, 80))

        self.Layout_BotonesMenu.addWidget(self.B_GestionEquipos, 0, 0, 1, 1)

        self.B_GestionParticipantes = QPushButton(self.Page_MenuPrincipal)
        self.B_GestionParticipantes.setObjectName(u"B_GestionParticipantes")
        self.B_GestionParticipantes.setMinimumSize(QSize(250, 80))

        self.Layout_BotonesMenu.addWidget(self.B_GestionParticipantes, 0, 1, 1, 1)

        self.B_GestionCalendario = QPushButton(self.Page_MenuPrincipal)
        self.B_GestionCalendario.setObjectName(u"B_GestionCalendario")
        self.B_GestionCalendario.setMinimumSize(QSize(250, 80))

        self.Layout_BotonesMenu.addWidget(self.B_GestionCalendario, 1, 0, 1, 1)

        self.B_ActualizarResultados = QPushButton(self.Page_MenuPrincipal)
        self.B_ActualizarResultados.setObjectName(u"B_ActualizarResultados")
        self.B_ActualizarResultados.setMinimumSize(QSize(250, 80))

        self.Layout_BotonesMenu.addWidget(self.B_ActualizarResultados, 1, 1, 1, 1)

        self.B_Clasificacion = QPushButton(self.Page_MenuPrincipal)
        self.B_Clasificacion.setObjectName(u"B_Clasificacion")
        self.B_Clasificacion.setMinimumSize(QSize(250, 80))

        self.Layout_BotonesMenu.addWidget(self.B_Clasificacion, 2, 0, 1, 1)

        self.B_Creditos = QPushButton(self.Page_MenuPrincipal)
        self.B_Creditos.setObjectName(u"B_Creditos")
        self.B_Creditos.setMinimumSize(QSize(250, 80))

        self.Layout_BotonesMenu.addWidget(self.B_Creditos, 2, 1, 1, 1)

        self.B_Ayuda = QPushButton(self.Page_MenuPrincipal)
        self.B_Ayuda.setObjectName(u"B_Ayuda")
        self.B_Ayuda.setMinimumSize(QSize(250, 80))

        self.Layout_BotonesMenu.addWidget(self.B_Ayuda, 3, 0, 1, 2)


        self.Layout_MenuPrincipal.addLayout(self.Layout_BotonesMenu)

        self.Spacer_MenuBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Layout_MenuPrincipal.addItem(self.Spacer_MenuBottom)

        self.Stacked_Paginas.addWidget(self.Page_MenuPrincipal)
        self.Page_GestionEquipos = QWidget()
        self.Page_GestionEquipos.setObjectName(u"Page_GestionEquipos")
        self.Layout_GestionEquipos = QVBoxLayout(self.Page_GestionEquipos)
        self.Layout_GestionEquipos.setObjectName(u"Layout_GestionEquipos")
        self.Layout_HeaderEquipos = QHBoxLayout()
        self.Layout_HeaderEquipos.setObjectName(u"Layout_HeaderEquipos")
        self.B_VolverDesdeEquipos = QPushButton(self.Page_GestionEquipos)
        self.B_VolverDesdeEquipos.setObjectName(u"B_VolverDesdeEquipos")
        self.B_VolverDesdeEquipos.setMaximumSize(QSize(100, 16777215))

        self.Layout_HeaderEquipos.addWidget(self.B_VolverDesdeEquipos)

        self.L_TituloEquipos = QLabel(self.Page_GestionEquipos)
        self.L_TituloEquipos.setObjectName(u"L_TituloEquipos")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.L_TituloEquipos.setFont(font1)
        self.L_TituloEquipos.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_HeaderEquipos.addWidget(self.L_TituloEquipos)

        self.Spacer_HeaderEquipos = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_HeaderEquipos.addItem(self.Spacer_HeaderEquipos)


        self.Layout_GestionEquipos.addLayout(self.Layout_HeaderEquipos)

        self.Group_DatosEquipo = QGroupBox(self.Page_GestionEquipos)
        self.Group_DatosEquipo.setObjectName(u"Group_DatosEquipo")
        self.Layout_FormEquipo = QFormLayout(self.Group_DatosEquipo)
        self.Layout_FormEquipo.setObjectName(u"Layout_FormEquipo")
        self.L_NombreEquipo = QLabel(self.Group_DatosEquipo)
        self.L_NombreEquipo.setObjectName(u"L_NombreEquipo")

        self.Layout_FormEquipo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.L_NombreEquipo)

        self.Lineedit_NombreEquipo = QLineEdit(self.Group_DatosEquipo)
        self.Lineedit_NombreEquipo.setObjectName(u"Lineedit_NombreEquipo")

        self.Layout_FormEquipo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.Lineedit_NombreEquipo)

        self.L_CursoEquipo = QLabel(self.Group_DatosEquipo)
        self.L_CursoEquipo.setObjectName(u"L_CursoEquipo")

        self.Layout_FormEquipo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.L_CursoEquipo)

        self.Combo_CursoEquipo = QComboBox(self.Group_DatosEquipo)
        self.Combo_CursoEquipo.setObjectName(u"Combo_CursoEquipo")

        self.Layout_FormEquipo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.Combo_CursoEquipo)

        self.L_ColorEquipo = QLabel(self.Group_DatosEquipo)
        self.L_ColorEquipo.setObjectName(u"L_ColorEquipo")

        self.Layout_FormEquipo.setWidget(2, QFormLayout.ItemRole.LabelRole, self.L_ColorEquipo)

        self.Layout_ColorEquipo = QHBoxLayout()
        self.Layout_ColorEquipo.setObjectName(u"Layout_ColorEquipo")
        self.Lineedit_ColorEquipo = QLineEdit(self.Group_DatosEquipo)
        self.Lineedit_ColorEquipo.setObjectName(u"Lineedit_ColorEquipo")

        self.Layout_ColorEquipo.addWidget(self.Lineedit_ColorEquipo)

        self.B_SeleccionarColor = QPushButton(self.Group_DatosEquipo)
        self.B_SeleccionarColor.setObjectName(u"B_SeleccionarColor")

        self.Layout_ColorEquipo.addWidget(self.B_SeleccionarColor)


        self.Layout_FormEquipo.setLayout(2, QFormLayout.ItemRole.FieldRole, self.Layout_ColorEquipo)

        self.L_EmblemaEquipo = QLabel(self.Group_DatosEquipo)
        self.L_EmblemaEquipo.setObjectName(u"L_EmblemaEquipo")

        self.Layout_FormEquipo.setWidget(3, QFormLayout.ItemRole.LabelRole, self.L_EmblemaEquipo)

        self.Layout_EmblemaEquipo = QHBoxLayout()
        self.Layout_EmblemaEquipo.setObjectName(u"Layout_EmblemaEquipo")
        self.Lineedit_RutaEmblema = QLineEdit(self.Group_DatosEquipo)
        self.Lineedit_RutaEmblema.setObjectName(u"Lineedit_RutaEmblema")
        self.Lineedit_RutaEmblema.setReadOnly(True)

        self.Layout_EmblemaEquipo.addWidget(self.Lineedit_RutaEmblema)

        self.B_SeleccionarEmblema = QPushButton(self.Group_DatosEquipo)
        self.B_SeleccionarEmblema.setObjectName(u"B_SeleccionarEmblema")

        self.Layout_EmblemaEquipo.addWidget(self.B_SeleccionarEmblema)


        self.Layout_FormEquipo.setLayout(3, QFormLayout.ItemRole.FieldRole, self.Layout_EmblemaEquipo)

        self.L_InfoAdicional = QLabel(self.Group_DatosEquipo)
        self.L_InfoAdicional.setObjectName(u"L_InfoAdicional")

        self.Layout_FormEquipo.setWidget(4, QFormLayout.ItemRole.LabelRole, self.L_InfoAdicional)

        self.Textedit_InfoEquipo = QTextEdit(self.Group_DatosEquipo)
        self.Textedit_InfoEquipo.setObjectName(u"Textedit_InfoEquipo")
        self.Textedit_InfoEquipo.setMaximumSize(QSize(16777215, 60))

        self.Layout_FormEquipo.setWidget(4, QFormLayout.ItemRole.FieldRole, self.Textedit_InfoEquipo)


        self.Layout_GestionEquipos.addWidget(self.Group_DatosEquipo)

        self.Layout_BotonesEquipo = QHBoxLayout()
        self.Layout_BotonesEquipo.setObjectName(u"Layout_BotonesEquipo")
        self.B_CrearEquipo = QPushButton(self.Page_GestionEquipos)
        self.B_CrearEquipo.setObjectName(u"B_CrearEquipo")

        self.Layout_BotonesEquipo.addWidget(self.B_CrearEquipo)

        self.B_EditarEquipo = QPushButton(self.Page_GestionEquipos)
        self.B_EditarEquipo.setObjectName(u"B_EditarEquipo")

        self.Layout_BotonesEquipo.addWidget(self.B_EditarEquipo)

        self.B_EliminarEquipo = QPushButton(self.Page_GestionEquipos)
        self.B_EliminarEquipo.setObjectName(u"B_EliminarEquipo")

        self.Layout_BotonesEquipo.addWidget(self.B_EliminarEquipo)

        self.B_LimpiarFormEquipo = QPushButton(self.Page_GestionEquipos)
        self.B_LimpiarFormEquipo.setObjectName(u"B_LimpiarFormEquipo")

        self.Layout_BotonesEquipo.addWidget(self.B_LimpiarFormEquipo)


        self.Layout_GestionEquipos.addLayout(self.Layout_BotonesEquipo)

        self.Group_ListaEquipos = QGroupBox(self.Page_GestionEquipos)
        self.Group_ListaEquipos.setObjectName(u"Group_ListaEquipos")
        self.Layout_ListaEquipos = QVBoxLayout(self.Group_ListaEquipos)
        self.Layout_ListaEquipos.setObjectName(u"Layout_ListaEquipos")
        self.Table_Equipos = QTableWidget(self.Group_ListaEquipos)
        self.Table_Equipos.setObjectName(u"Table_Equipos")
        self.Table_Equipos.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.Table_Equipos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.Layout_ListaEquipos.addWidget(self.Table_Equipos)

        self.B_VerJugadoresEquipo = QPushButton(self.Group_ListaEquipos)
        self.B_VerJugadoresEquipo.setObjectName(u"B_VerJugadoresEquipo")

        self.Layout_ListaEquipos.addWidget(self.B_VerJugadoresEquipo)


        self.Layout_GestionEquipos.addWidget(self.Group_ListaEquipos)

        self.Stacked_Paginas.addWidget(self.Page_GestionEquipos)
        self.Page_GestionParticipantes = QWidget()
        self.Page_GestionParticipantes.setObjectName(u"Page_GestionParticipantes")
        self.Layout_GestionParticipantes = QVBoxLayout(self.Page_GestionParticipantes)
        self.Layout_GestionParticipantes.setObjectName(u"Layout_GestionParticipantes")
        self.Layout_HeaderParticipantes = QHBoxLayout()
        self.Layout_HeaderParticipantes.setObjectName(u"Layout_HeaderParticipantes")
        self.B_VolverDesdeParticipantes = QPushButton(self.Page_GestionParticipantes)
        self.B_VolverDesdeParticipantes.setObjectName(u"B_VolverDesdeParticipantes")
        self.B_VolverDesdeParticipantes.setMaximumSize(QSize(100, 16777215))

        self.Layout_HeaderParticipantes.addWidget(self.B_VolverDesdeParticipantes)

        self.L_TituloParticipantes = QLabel(self.Page_GestionParticipantes)
        self.L_TituloParticipantes.setObjectName(u"L_TituloParticipantes")
        self.L_TituloParticipantes.setFont(font1)
        self.L_TituloParticipantes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_HeaderParticipantes.addWidget(self.L_TituloParticipantes)

        self.Spacer_HeaderParticipantes = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_HeaderParticipantes.addItem(self.Spacer_HeaderParticipantes)


        self.Layout_GestionParticipantes.addLayout(self.Layout_HeaderParticipantes)

        self.Group_DatosParticipante = QGroupBox(self.Page_GestionParticipantes)
        self.Group_DatosParticipante.setObjectName(u"Group_DatosParticipante")
        self.Layout_FormParticipante = QFormLayout(self.Group_DatosParticipante)
        self.Layout_FormParticipante.setObjectName(u"Layout_FormParticipante")
        self.L_NombreParticipante = QLabel(self.Group_DatosParticipante)
        self.L_NombreParticipante.setObjectName(u"L_NombreParticipante")

        self.Layout_FormParticipante.setWidget(0, QFormLayout.ItemRole.LabelRole, self.L_NombreParticipante)

        self.Lineedit_NombreParticipante = QLineEdit(self.Group_DatosParticipante)
        self.Lineedit_NombreParticipante.setObjectName(u"Lineedit_NombreParticipante")

        self.Layout_FormParticipante.setWidget(0, QFormLayout.ItemRole.FieldRole, self.Lineedit_NombreParticipante)

        self.L_FechaNacimiento = QLabel(self.Group_DatosParticipante)
        self.L_FechaNacimiento.setObjectName(u"L_FechaNacimiento")

        self.Layout_FormParticipante.setWidget(1, QFormLayout.ItemRole.LabelRole, self.L_FechaNacimiento)

        self.Dateedit_FechaNacimiento = QDateEdit(self.Group_DatosParticipante)
        self.Dateedit_FechaNacimiento.setObjectName(u"Dateedit_FechaNacimiento")
        self.Dateedit_FechaNacimiento.setCalendarPopup(True)

        self.Layout_FormParticipante.setWidget(1, QFormLayout.ItemRole.FieldRole, self.Dateedit_FechaNacimiento)

        self.L_CursoParticipante = QLabel(self.Group_DatosParticipante)
        self.L_CursoParticipante.setObjectName(u"L_CursoParticipante")

        self.Layout_FormParticipante.setWidget(2, QFormLayout.ItemRole.LabelRole, self.L_CursoParticipante)

        self.Combo_CursoParticipante = QComboBox(self.Group_DatosParticipante)
        self.Combo_CursoParticipante.setObjectName(u"Combo_CursoParticipante")

        self.Layout_FormParticipante.setWidget(2, QFormLayout.ItemRole.FieldRole, self.Combo_CursoParticipante)

        self.L_TipoParticipante = QLabel(self.Group_DatosParticipante)
        self.L_TipoParticipante.setObjectName(u"L_TipoParticipante")

        self.Layout_FormParticipante.setWidget(3, QFormLayout.ItemRole.LabelRole, self.L_TipoParticipante)

        self.Layout_TipoParticipante = QHBoxLayout()
        self.Layout_TipoParticipante.setObjectName(u"Layout_TipoParticipante")
        self.Check_EsJugador = QCheckBox(self.Group_DatosParticipante)
        self.Check_EsJugador.setObjectName(u"Check_EsJugador")

        self.Layout_TipoParticipante.addWidget(self.Check_EsJugador)

        self.Check_EsArbitro = QCheckBox(self.Group_DatosParticipante)
        self.Check_EsArbitro.setObjectName(u"Check_EsArbitro")

        self.Layout_TipoParticipante.addWidget(self.Check_EsArbitro)


        self.Layout_FormParticipante.setLayout(3, QFormLayout.ItemRole.FieldRole, self.Layout_TipoParticipante)

        self.L_PosicionJugador = QLabel(self.Group_DatosParticipante)
        self.L_PosicionJugador.setObjectName(u"L_PosicionJugador")

        self.Layout_FormParticipante.setWidget(4, QFormLayout.ItemRole.LabelRole, self.L_PosicionJugador)

        self.Combo_PosicionJugador = QComboBox(self.Group_DatosParticipante)
        self.Combo_PosicionJugador.addItem("")
        self.Combo_PosicionJugador.addItem("")
        self.Combo_PosicionJugador.addItem("")
        self.Combo_PosicionJugador.addItem("")
        self.Combo_PosicionJugador.setObjectName(u"Combo_PosicionJugador")

        self.Layout_FormParticipante.setWidget(4, QFormLayout.ItemRole.FieldRole, self.Combo_PosicionJugador)

        self.L_EquipoAsignado = QLabel(self.Group_DatosParticipante)
        self.L_EquipoAsignado.setObjectName(u"L_EquipoAsignado")

        self.Layout_FormParticipante.setWidget(5, QFormLayout.ItemRole.LabelRole, self.L_EquipoAsignado)

        self.Combo_EquipoAsignado = QComboBox(self.Group_DatosParticipante)
        self.Combo_EquipoAsignado.setObjectName(u"Combo_EquipoAsignado")

        self.Layout_FormParticipante.setWidget(5, QFormLayout.ItemRole.FieldRole, self.Combo_EquipoAsignado)

        self.L_EstadisticasJugador = QLabel(self.Group_DatosParticipante)
        self.L_EstadisticasJugador.setObjectName(u"L_EstadisticasJugador")

        self.Layout_FormParticipante.setWidget(6, QFormLayout.ItemRole.LabelRole, self.L_EstadisticasJugador)

        self.Layout_Estadisticas = QHBoxLayout()
        self.Layout_Estadisticas.setObjectName(u"Layout_Estadisticas")
        self.L_Goles = QLabel(self.Group_DatosParticipante)
        self.L_Goles.setObjectName(u"L_Goles")

        self.Layout_Estadisticas.addWidget(self.L_Goles)

        self.Spin_Goles = QSpinBox(self.Group_DatosParticipante)
        self.Spin_Goles.setObjectName(u"Spin_Goles")

        self.Layout_Estadisticas.addWidget(self.Spin_Goles)

        self.L_TarjetasAmarillas = QLabel(self.Group_DatosParticipante)
        self.L_TarjetasAmarillas.setObjectName(u"L_TarjetasAmarillas")

        self.Layout_Estadisticas.addWidget(self.L_TarjetasAmarillas)

        self.Spin_TarjetasAmarillas = QSpinBox(self.Group_DatosParticipante)
        self.Spin_TarjetasAmarillas.setObjectName(u"Spin_TarjetasAmarillas")

        self.Layout_Estadisticas.addWidget(self.Spin_TarjetasAmarillas)

        self.L_TarjetasRojas = QLabel(self.Group_DatosParticipante)
        self.L_TarjetasRojas.setObjectName(u"L_TarjetasRojas")

        self.Layout_Estadisticas.addWidget(self.L_TarjetasRojas)

        self.Spin_TarjetasRojas = QSpinBox(self.Group_DatosParticipante)
        self.Spin_TarjetasRojas.setObjectName(u"Spin_TarjetasRojas")

        self.Layout_Estadisticas.addWidget(self.Spin_TarjetasRojas)


        self.Layout_FormParticipante.setLayout(6, QFormLayout.ItemRole.FieldRole, self.Layout_Estadisticas)


        self.Layout_GestionParticipantes.addWidget(self.Group_DatosParticipante)

        self.Layout_BotonesParticipante = QHBoxLayout()
        self.Layout_BotonesParticipante.setObjectName(u"Layout_BotonesParticipante")
        self.B_RegistrarParticipante = QPushButton(self.Page_GestionParticipantes)
        self.B_RegistrarParticipante.setObjectName(u"B_RegistrarParticipante")

        self.Layout_BotonesParticipante.addWidget(self.B_RegistrarParticipante)

        self.B_EditarParticipante = QPushButton(self.Page_GestionParticipantes)
        self.B_EditarParticipante.setObjectName(u"B_EditarParticipante")

        self.Layout_BotonesParticipante.addWidget(self.B_EditarParticipante)

        self.B_EliminarParticipante = QPushButton(self.Page_GestionParticipantes)
        self.B_EliminarParticipante.setObjectName(u"B_EliminarParticipante")

        self.Layout_BotonesParticipante.addWidget(self.B_EliminarParticipante)

        self.B_LimpiarFormParticipante = QPushButton(self.Page_GestionParticipantes)
        self.B_LimpiarFormParticipante.setObjectName(u"B_LimpiarFormParticipante")

        self.Layout_BotonesParticipante.addWidget(self.B_LimpiarFormParticipante)


        self.Layout_GestionParticipantes.addLayout(self.Layout_BotonesParticipante)

        self.Group_ListaParticipantes = QGroupBox(self.Page_GestionParticipantes)
        self.Group_ListaParticipantes.setObjectName(u"Group_ListaParticipantes")
        self.Layout_ListaParticipantes = QVBoxLayout(self.Group_ListaParticipantes)
        self.Layout_ListaParticipantes.setObjectName(u"Layout_ListaParticipantes")
        self.Layout_FiltrosParticipantes = QHBoxLayout()
        self.Layout_FiltrosParticipantes.setObjectName(u"Layout_FiltrosParticipantes")
        self.L_FiltrarPor = QLabel(self.Group_ListaParticipantes)
        self.L_FiltrarPor.setObjectName(u"L_FiltrarPor")

        self.Layout_FiltrosParticipantes.addWidget(self.L_FiltrarPor)

        self.Combo_FiltroParticipantes = QComboBox(self.Group_ListaParticipantes)
        self.Combo_FiltroParticipantes.addItem("")
        self.Combo_FiltroParticipantes.addItem("")
        self.Combo_FiltroParticipantes.addItem("")
        self.Combo_FiltroParticipantes.setObjectName(u"Combo_FiltroParticipantes")

        self.Layout_FiltrosParticipantes.addWidget(self.Combo_FiltroParticipantes)

        self.L_OrdenarPor = QLabel(self.Group_ListaParticipantes)
        self.L_OrdenarPor.setObjectName(u"L_OrdenarPor")

        self.Layout_FiltrosParticipantes.addWidget(self.L_OrdenarPor)

        self.Combo_OrdenParticipantes = QComboBox(self.Group_ListaParticipantes)
        self.Combo_OrdenParticipantes.addItem("")
        self.Combo_OrdenParticipantes.addItem("")
        self.Combo_OrdenParticipantes.addItem("")
        self.Combo_OrdenParticipantes.addItem("")
        self.Combo_OrdenParticipantes.setObjectName(u"Combo_OrdenParticipantes")

        self.Layout_FiltrosParticipantes.addWidget(self.Combo_OrdenParticipantes)

        self.Spacer_FiltrosParticipantes = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_FiltrosParticipantes.addItem(self.Spacer_FiltrosParticipantes)


        self.Layout_ListaParticipantes.addLayout(self.Layout_FiltrosParticipantes)

        self.Table_Participantes = QTableWidget(self.Group_ListaParticipantes)
        self.Table_Participantes.setObjectName(u"Table_Participantes")
        self.Table_Participantes.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.Table_Participantes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.Layout_ListaParticipantes.addWidget(self.Table_Participantes)


        self.Layout_GestionParticipantes.addWidget(self.Group_ListaParticipantes)

        self.Stacked_Paginas.addWidget(self.Page_GestionParticipantes)
        self.Page_GestionCalendario = QWidget()
        self.Page_GestionCalendario.setObjectName(u"Page_GestionCalendario")
        self.Layout_GestionCalendario = QVBoxLayout(self.Page_GestionCalendario)
        self.Layout_GestionCalendario.setObjectName(u"Layout_GestionCalendario")
        self.Layout_HeaderCalendario = QHBoxLayout()
        self.Layout_HeaderCalendario.setObjectName(u"Layout_HeaderCalendario")
        self.B_VolverDesdeCalendario = QPushButton(self.Page_GestionCalendario)
        self.B_VolverDesdeCalendario.setObjectName(u"B_VolverDesdeCalendario")
        self.B_VolverDesdeCalendario.setMaximumSize(QSize(100, 16777215))

        self.Layout_HeaderCalendario.addWidget(self.B_VolverDesdeCalendario)

        self.L_TituloCalendario = QLabel(self.Page_GestionCalendario)
        self.L_TituloCalendario.setObjectName(u"L_TituloCalendario")
        self.L_TituloCalendario.setFont(font1)
        self.L_TituloCalendario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_HeaderCalendario.addWidget(self.L_TituloCalendario)

        self.Spacer_HeaderCalendario = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_HeaderCalendario.addItem(self.Spacer_HeaderCalendario)

        self.B_ReiniciarTorneo = QPushButton(self.Page_GestionCalendario)
        self.B_ReiniciarTorneo.setObjectName(u"B_ReiniciarTorneo")
        self.B_ReiniciarTorneo.setMaximumSize(QSize(150, 16777215))

        self.Layout_HeaderCalendario.addWidget(self.B_ReiniciarTorneo)


        self.Layout_GestionCalendario.addLayout(self.Layout_HeaderCalendario)

        self.Group_DatosPartido = QGroupBox(self.Page_GestionCalendario)
        self.Group_DatosPartido.setObjectName(u"Group_DatosPartido")
        self.Group_DatosPartido.setMaximumSize(QSize(16777215, 250))
        self.Layout_FormPartido = QFormLayout(self.Group_DatosPartido)
        self.Layout_FormPartido.setObjectName(u"Layout_FormPartido")
        self.L_EquipoLocal = QLabel(self.Group_DatosPartido)
        self.L_EquipoLocal.setObjectName(u"L_EquipoLocal")

        self.Layout_FormPartido.setWidget(0, QFormLayout.ItemRole.LabelRole, self.L_EquipoLocal)

        self.Combo_EquipoLocal = QComboBox(self.Group_DatosPartido)
        self.Combo_EquipoLocal.setObjectName(u"Combo_EquipoLocal")

        self.Layout_FormPartido.setWidget(0, QFormLayout.ItemRole.FieldRole, self.Combo_EquipoLocal)

        self.L_EquipoVisitante = QLabel(self.Group_DatosPartido)
        self.L_EquipoVisitante.setObjectName(u"L_EquipoVisitante")

        self.Layout_FormPartido.setWidget(1, QFormLayout.ItemRole.LabelRole, self.L_EquipoVisitante)

        self.Combo_EquipoVisitante = QComboBox(self.Group_DatosPartido)
        self.Combo_EquipoVisitante.setObjectName(u"Combo_EquipoVisitante")

        self.Layout_FormPartido.setWidget(1, QFormLayout.ItemRole.FieldRole, self.Combo_EquipoVisitante)

        self.L_FechaPartido = QLabel(self.Group_DatosPartido)
        self.L_FechaPartido.setObjectName(u"L_FechaPartido")

        self.Layout_FormPartido.setWidget(2, QFormLayout.ItemRole.LabelRole, self.L_FechaPartido)

        self.Dateedit_FechaPartido = QDateEdit(self.Group_DatosPartido)
        self.Dateedit_FechaPartido.setObjectName(u"Dateedit_FechaPartido")
        self.Dateedit_FechaPartido.setCalendarPopup(True)

        self.Layout_FormPartido.setWidget(2, QFormLayout.ItemRole.FieldRole, self.Dateedit_FechaPartido)

        self.L_HoraPartido = QLabel(self.Group_DatosPartido)
        self.L_HoraPartido.setObjectName(u"L_HoraPartido")

        self.Layout_FormPartido.setWidget(3, QFormLayout.ItemRole.LabelRole, self.L_HoraPartido)

        self.Timeedit_HoraPartido = QTimeEdit(self.Group_DatosPartido)
        self.Timeedit_HoraPartido.setObjectName(u"Timeedit_HoraPartido")

        self.Layout_FormPartido.setWidget(3, QFormLayout.ItemRole.FieldRole, self.Timeedit_HoraPartido)

        self.L_ArbitroPartido = QLabel(self.Group_DatosPartido)
        self.L_ArbitroPartido.setObjectName(u"L_ArbitroPartido")

        self.Layout_FormPartido.setWidget(4, QFormLayout.ItemRole.LabelRole, self.L_ArbitroPartido)

        self.Combo_ArbitroPartido = QComboBox(self.Group_DatosPartido)
        self.Combo_ArbitroPartido.setObjectName(u"Combo_ArbitroPartido")

        self.Layout_FormPartido.setWidget(4, QFormLayout.ItemRole.FieldRole, self.Combo_ArbitroPartido)

        self.L_Eliminatoria = QLabel(self.Group_DatosPartido)
        self.L_Eliminatoria.setObjectName(u"L_Eliminatoria")

        self.Layout_FormPartido.setWidget(5, QFormLayout.ItemRole.LabelRole, self.L_Eliminatoria)

        self.Combo_Eliminatoria = QComboBox(self.Group_DatosPartido)
        self.Combo_Eliminatoria.addItem("")
        self.Combo_Eliminatoria.addItem("")
        self.Combo_Eliminatoria.addItem("")
        self.Combo_Eliminatoria.addItem("")
        self.Combo_Eliminatoria.addItem("")
        self.Combo_Eliminatoria.addItem("")
        self.Combo_Eliminatoria.setObjectName(u"Combo_Eliminatoria")

        self.Layout_FormPartido.setWidget(5, QFormLayout.ItemRole.FieldRole, self.Combo_Eliminatoria)

        self.L_LugarPartido = QLabel(self.Group_DatosPartido)
        self.L_LugarPartido.setObjectName(u"L_LugarPartido")

        self.Layout_FormPartido.setWidget(6, QFormLayout.ItemRole.LabelRole, self.L_LugarPartido)

        self.Lineedit_LugarPartido = QLineEdit(self.Group_DatosPartido)
        self.Lineedit_LugarPartido.setObjectName(u"Lineedit_LugarPartido")

        self.Layout_FormPartido.setWidget(6, QFormLayout.ItemRole.FieldRole, self.Lineedit_LugarPartido)


        self.Layout_GestionCalendario.addWidget(self.Group_DatosPartido)

        self.Layout_BotonesPartido = QHBoxLayout()
        self.Layout_BotonesPartido.setObjectName(u"Layout_BotonesPartido")
        self.B_ProgramarPartido = QPushButton(self.Page_GestionCalendario)
        self.B_ProgramarPartido.setObjectName(u"B_ProgramarPartido")

        self.Layout_BotonesPartido.addWidget(self.B_ProgramarPartido)

        self.B_EditarPartido = QPushButton(self.Page_GestionCalendario)
        self.B_EditarPartido.setObjectName(u"B_EditarPartido")

        self.Layout_BotonesPartido.addWidget(self.B_EditarPartido)

        self.B_EliminarPartido = QPushButton(self.Page_GestionCalendario)
        self.B_EliminarPartido.setObjectName(u"B_EliminarPartido")

        self.Layout_BotonesPartido.addWidget(self.B_EliminarPartido)

        self.B_LimpiarFormPartido = QPushButton(self.Page_GestionCalendario)
        self.B_LimpiarFormPartido.setObjectName(u"B_LimpiarFormPartido")

        self.Layout_BotonesPartido.addWidget(self.B_LimpiarFormPartido)


        self.Layout_GestionCalendario.addLayout(self.Layout_BotonesPartido)

        self.Group_ListaPartidos = QGroupBox(self.Page_GestionCalendario)
        self.Group_ListaPartidos.setObjectName(u"Group_ListaPartidos")
        self.Layout_ListaPartidos = QVBoxLayout(self.Group_ListaPartidos)
        self.Layout_ListaPartidos.setObjectName(u"Layout_ListaPartidos")
        self.Layout_FiltrosPartidos = QHBoxLayout()
        self.Layout_FiltrosPartidos.setObjectName(u"Layout_FiltrosPartidos")
        self.L_FiltrarEliminatoria = QLabel(self.Group_ListaPartidos)
        self.L_FiltrarEliminatoria.setObjectName(u"L_FiltrarEliminatoria")

        self.Layout_FiltrosPartidos.addWidget(self.L_FiltrarEliminatoria)

        self.Combo_FiltroEliminatoria = QComboBox(self.Group_ListaPartidos)
        self.Combo_FiltroEliminatoria.addItem("")
        self.Combo_FiltroEliminatoria.addItem("")
        self.Combo_FiltroEliminatoria.addItem("")
        self.Combo_FiltroEliminatoria.addItem("")
        self.Combo_FiltroEliminatoria.addItem("")
        self.Combo_FiltroEliminatoria.addItem("")
        self.Combo_FiltroEliminatoria.addItem("")
        self.Combo_FiltroEliminatoria.setObjectName(u"Combo_FiltroEliminatoria")

        self.Layout_FiltrosPartidos.addWidget(self.Combo_FiltroEliminatoria)

        self.Spacer_FiltrosPartidos = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_FiltrosPartidos.addItem(self.Spacer_FiltrosPartidos)


        self.Layout_ListaPartidos.addLayout(self.Layout_FiltrosPartidos)

        self.Tree_Partidos = QTreeWidget(self.Group_ListaPartidos)
        self.Tree_Partidos.setObjectName(u"Tree_Partidos")

        self.Layout_ListaPartidos.addWidget(self.Tree_Partidos)


        self.Layout_GestionCalendario.addWidget(self.Group_ListaPartidos)

        self.Stacked_Paginas.addWidget(self.Page_GestionCalendario)
        self.Page_ActualizacionResultados = QWidget()
        self.Page_ActualizacionResultados.setObjectName(u"Page_ActualizacionResultados")
        self.Layout_ActualizacionResultados = QVBoxLayout(self.Page_ActualizacionResultados)
        self.Layout_ActualizacionResultados.setObjectName(u"Layout_ActualizacionResultados")
        self.Layout_HeaderResultados = QHBoxLayout()
        self.Layout_HeaderResultados.setObjectName(u"Layout_HeaderResultados")
        self.B_VolverDesdeResultados = QPushButton(self.Page_ActualizacionResultados)
        self.B_VolverDesdeResultados.setObjectName(u"B_VolverDesdeResultados")
        self.B_VolverDesdeResultados.setMaximumSize(QSize(100, 16777215))

        self.Layout_HeaderResultados.addWidget(self.B_VolverDesdeResultados)

        self.L_TituloResultados = QLabel(self.Page_ActualizacionResultados)
        self.L_TituloResultados.setObjectName(u"L_TituloResultados")
        self.L_TituloResultados.setFont(font1)
        self.L_TituloResultados.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_HeaderResultados.addWidget(self.L_TituloResultados)

        self.Spacer_HeaderResultados = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_HeaderResultados.addItem(self.Spacer_HeaderResultados)


        self.Layout_ActualizacionResultados.addLayout(self.Layout_HeaderResultados)

        self.Group_SeleccionarPartido = QGroupBox(self.Page_ActualizacionResultados)
        self.Group_SeleccionarPartido.setObjectName(u"Group_SeleccionarPartido")
        self.Layout_SeleccionPartido = QVBoxLayout(self.Group_SeleccionarPartido)
        self.Layout_SeleccionPartido.setObjectName(u"Layout_SeleccionPartido")
        self.Combo_PartidosJugados = QComboBox(self.Group_SeleccionarPartido)
        self.Combo_PartidosJugados.setObjectName(u"Combo_PartidosJugados")
        self.Combo_PartidosJugados.setMinimumSize(QSize(0, 30))

        self.Layout_SeleccionPartido.addWidget(self.Combo_PartidosJugados)


        self.Layout_ActualizacionResultados.addWidget(self.Group_SeleccionarPartido)

        self.Group_ResultadoPartido = QGroupBox(self.Page_ActualizacionResultados)
        self.Group_ResultadoPartido.setObjectName(u"Group_ResultadoPartido")
        self.Layout_ResultadoPartido = QHBoxLayout(self.Group_ResultadoPartido)
        self.Layout_ResultadoPartido.setObjectName(u"Layout_ResultadoPartido")
        self.Layout_EquipoLocalResultado = QVBoxLayout()
        self.Layout_EquipoLocalResultado.setObjectName(u"Layout_EquipoLocalResultado")
        self.L_NombreEquipoLocal = QLabel(self.Group_ResultadoPartido)
        self.L_NombreEquipoLocal.setObjectName(u"L_NombreEquipoLocal")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.L_NombreEquipoLocal.setFont(font2)
        self.L_NombreEquipoLocal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_EquipoLocalResultado.addWidget(self.L_NombreEquipoLocal)

        self.L_GolesLocal = QLabel(self.Group_ResultadoPartido)
        self.L_GolesLocal.setObjectName(u"L_GolesLocal")

        self.Layout_EquipoLocalResultado.addWidget(self.L_GolesLocal)

        self.Spin_GolesLocal = QSpinBox(self.Group_ResultadoPartido)
        self.Spin_GolesLocal.setObjectName(u"Spin_GolesLocal")
        self.Spin_GolesLocal.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(16)
        self.Spin_GolesLocal.setFont(font3)

        self.Layout_EquipoLocalResultado.addWidget(self.Spin_GolesLocal)


        self.Layout_ResultadoPartido.addLayout(self.Layout_EquipoLocalResultado)

        self.L_VS = QLabel(self.Group_ResultadoPartido)
        self.L_VS.setObjectName(u"L_VS")
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        self.L_VS.setFont(font4)
        self.L_VS.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_ResultadoPartido.addWidget(self.L_VS)

        self.Layout_EquipoVisitanteResultado = QVBoxLayout()
        self.Layout_EquipoVisitanteResultado.setObjectName(u"Layout_EquipoVisitanteResultado")
        self.L_NombreEquipoVisitante = QLabel(self.Group_ResultadoPartido)
        self.L_NombreEquipoVisitante.setObjectName(u"L_NombreEquipoVisitante")
        self.L_NombreEquipoVisitante.setFont(font2)
        self.L_NombreEquipoVisitante.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_EquipoVisitanteResultado.addWidget(self.L_NombreEquipoVisitante)

        self.L_GolesVisitante = QLabel(self.Group_ResultadoPartido)
        self.L_GolesVisitante.setObjectName(u"L_GolesVisitante")

        self.Layout_EquipoVisitanteResultado.addWidget(self.L_GolesVisitante)

        self.Spin_GolesVisitante = QSpinBox(self.Group_ResultadoPartido)
        self.Spin_GolesVisitante.setObjectName(u"Spin_GolesVisitante")
        self.Spin_GolesVisitante.setMinimumSize(QSize(0, 40))
        self.Spin_GolesVisitante.setFont(font3)

        self.Layout_EquipoVisitanteResultado.addWidget(self.Spin_GolesVisitante)


        self.Layout_ResultadoPartido.addLayout(self.Layout_EquipoVisitanteResultado)


        self.Layout_ActualizacionResultados.addWidget(self.Group_ResultadoPartido)

        self.Group_DetallesJugadores = QGroupBox(self.Page_ActualizacionResultados)
        self.Group_DetallesJugadores.setObjectName(u"Group_DetallesJugadores")
        self.Layout_DetallesJugadores = QVBoxLayout(self.Group_DetallesJugadores)
        self.Layout_DetallesJugadores.setObjectName(u"Layout_DetallesJugadores")
        self.Layout_SelectorJugador = QHBoxLayout()
        self.Layout_SelectorJugador.setObjectName(u"Layout_SelectorJugador")
        self.L_SeleccionarJugador = QLabel(self.Group_DetallesJugadores)
        self.L_SeleccionarJugador.setObjectName(u"L_SeleccionarJugador")

        self.Layout_SelectorJugador.addWidget(self.L_SeleccionarJugador)

        self.Combo_JugadoresPartido = QComboBox(self.Group_DetallesJugadores)
        self.Combo_JugadoresPartido.setObjectName(u"Combo_JugadoresPartido")
        self.Combo_JugadoresPartido.setMinimumSize(QSize(300, 0))

        self.Layout_SelectorJugador.addWidget(self.Combo_JugadoresPartido)

        self.L_GolesJugador = QLabel(self.Group_DetallesJugadores)
        self.L_GolesJugador.setObjectName(u"L_GolesJugador")

        self.Layout_SelectorJugador.addWidget(self.L_GolesJugador)

        self.Spin_GolesJugador = QSpinBox(self.Group_DetallesJugadores)
        self.Spin_GolesJugador.setObjectName(u"Spin_GolesJugador")

        self.Layout_SelectorJugador.addWidget(self.Spin_GolesJugador)

        self.L_TarjetasAmarillasJugador = QLabel(self.Group_DetallesJugadores)
        self.L_TarjetasAmarillasJugador.setObjectName(u"L_TarjetasAmarillasJugador")

        self.Layout_SelectorJugador.addWidget(self.L_TarjetasAmarillasJugador)

        self.Spin_TarjetasAmarillasJugador = QSpinBox(self.Group_DetallesJugadores)
        self.Spin_TarjetasAmarillasJugador.setObjectName(u"Spin_TarjetasAmarillasJugador")

        self.Layout_SelectorJugador.addWidget(self.Spin_TarjetasAmarillasJugador)

        self.L_TarjetasRojasJugador = QLabel(self.Group_DetallesJugadores)
        self.L_TarjetasRojasJugador.setObjectName(u"L_TarjetasRojasJugador")

        self.Layout_SelectorJugador.addWidget(self.L_TarjetasRojasJugador)

        self.Spin_TarjetasRojasJugador = QSpinBox(self.Group_DetallesJugadores)
        self.Spin_TarjetasRojasJugador.setObjectName(u"Spin_TarjetasRojasJugador")

        self.Layout_SelectorJugador.addWidget(self.Spin_TarjetasRojasJugador)

        self.B_AgregarEstadisticaJugador = QPushButton(self.Group_DetallesJugadores)
        self.B_AgregarEstadisticaJugador.setObjectName(u"B_AgregarEstadisticaJugador")

        self.Layout_SelectorJugador.addWidget(self.B_AgregarEstadisticaJugador)


        self.Layout_DetallesJugadores.addLayout(self.Layout_SelectorJugador)

        self.Table_EstadisticasPartido = QTableWidget(self.Group_DetallesJugadores)
        self.Table_EstadisticasPartido.setObjectName(u"Table_EstadisticasPartido")
        self.Table_EstadisticasPartido.setMaximumSize(QSize(16777215, 150))

        self.Layout_DetallesJugadores.addWidget(self.Table_EstadisticasPartido)


        self.Layout_ActualizacionResultados.addWidget(self.Group_DetallesJugadores)

        self.Layout_BotonesResultados = QHBoxLayout()
        self.Layout_BotonesResultados.setObjectName(u"Layout_BotonesResultados")
        self.B_GuardarResultado = QPushButton(self.Page_ActualizacionResultados)
        self.B_GuardarResultado.setObjectName(u"B_GuardarResultado")

        self.Layout_BotonesResultados.addWidget(self.B_GuardarResultado)

        self.B_LimpiarResultado = QPushButton(self.Page_ActualizacionResultados)
        self.B_LimpiarResultado.setObjectName(u"B_LimpiarResultado")

        self.Layout_BotonesResultados.addWidget(self.B_LimpiarResultado)


        self.Layout_ActualizacionResultados.addLayout(self.Layout_BotonesResultados)

        self.Group_PartidosJugados = QGroupBox(self.Page_ActualizacionResultados)
        self.Group_PartidosJugados.setObjectName(u"Group_PartidosJugados")
        self.Layout_PartidosJugados = QVBoxLayout(self.Group_PartidosJugados)
        self.Layout_PartidosJugados.setObjectName(u"Layout_PartidosJugados")
        self.Table_PartidosJugados = QTableWidget(self.Group_PartidosJugados)
        self.Table_PartidosJugados.setObjectName(u"Table_PartidosJugados")
        self.Table_PartidosJugados.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.Layout_PartidosJugados.addWidget(self.Table_PartidosJugados)


        self.Layout_ActualizacionResultados.addWidget(self.Group_PartidosJugados)

        self.Stacked_Paginas.addWidget(self.Page_ActualizacionResultados)
        self.Page_Clasificacion = QWidget()
        self.Page_Clasificacion.setObjectName(u"Page_Clasificacion")
        self.Layout_Clasificacion = QVBoxLayout(self.Page_Clasificacion)
        self.Layout_Clasificacion.setObjectName(u"Layout_Clasificacion")
        self.Layout_HeaderClasificacion = QHBoxLayout()
        self.Layout_HeaderClasificacion.setObjectName(u"Layout_HeaderClasificacion")
        self.B_VolverDesdeClasificacion = QPushButton(self.Page_Clasificacion)
        self.B_VolverDesdeClasificacion.setObjectName(u"B_VolverDesdeClasificacion")
        self.B_VolverDesdeClasificacion.setMaximumSize(QSize(100, 16777215))

        self.Layout_HeaderClasificacion.addWidget(self.B_VolverDesdeClasificacion)

        self.L_TituloClasificacion = QLabel(self.Page_Clasificacion)
        self.L_TituloClasificacion.setObjectName(u"L_TituloClasificacion")
        self.L_TituloClasificacion.setFont(font1)
        self.L_TituloClasificacion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_HeaderClasificacion.addWidget(self.L_TituloClasificacion)

        self.Spacer_HeaderClasificacion = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_HeaderClasificacion.addItem(self.Spacer_HeaderClasificacion)


        self.Layout_Clasificacion.addLayout(self.Layout_HeaderClasificacion)

        self.Layout_OpcionesClasificacion = QHBoxLayout()
        self.Layout_OpcionesClasificacion.setObjectName(u"Layout_OpcionesClasificacion")
        self.B_GenerarSiguienteRonda = QPushButton(self.Page_Clasificacion)
        self.B_GenerarSiguienteRonda.setObjectName(u"B_GenerarSiguienteRonda")

        self.Layout_OpcionesClasificacion.addWidget(self.B_GenerarSiguienteRonda)

        self.B_ActualizarClasificacion = QPushButton(self.Page_Clasificacion)
        self.B_ActualizarClasificacion.setObjectName(u"B_ActualizarClasificacion")

        self.Layout_OpcionesClasificacion.addWidget(self.B_ActualizarClasificacion)

        self.B_ExportarCSV = QPushButton(self.Page_Clasificacion)
        self.B_ExportarCSV.setObjectName(u"B_ExportarCSV")

        self.Layout_OpcionesClasificacion.addWidget(self.B_ExportarCSV)

        self.Spacer_OpcionesClasificacion = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_OpcionesClasificacion.addItem(self.Spacer_OpcionesClasificacion)


        self.Layout_Clasificacion.addLayout(self.Layout_OpcionesClasificacion)

        self.Tab_Clasificacion = QTabWidget(self.Page_Clasificacion)
        self.Tab_Clasificacion.setObjectName(u"Tab_Clasificacion")
        self.Tab_CuadroEliminatorias = QWidget()
        self.Tab_CuadroEliminatorias.setObjectName(u"Tab_CuadroEliminatorias")
        self.Layout_CuadroEliminatorias = QVBoxLayout(self.Tab_CuadroEliminatorias)
        self.Layout_CuadroEliminatorias.setObjectName(u"Layout_CuadroEliminatorias")
        self.Tree_Eliminatorias = QTreeWidget(self.Tab_CuadroEliminatorias)
        self.Tree_Eliminatorias.setObjectName(u"Tree_Eliminatorias")

        self.Layout_CuadroEliminatorias.addWidget(self.Tree_Eliminatorias)

        self.Tab_Clasificacion.addTab(self.Tab_CuadroEliminatorias, "")
        self.Tab_ClasificacionGeneral = QWidget()
        self.Tab_ClasificacionGeneral.setObjectName(u"Tab_ClasificacionGeneral")
        self.Layout_ClasificacionGeneral = QVBoxLayout(self.Tab_ClasificacionGeneral)
        self.Layout_ClasificacionGeneral.setObjectName(u"Layout_ClasificacionGeneral")
        self.Table_ClasificacionEquipos = QTableWidget(self.Tab_ClasificacionGeneral)
        self.Table_ClasificacionEquipos.setObjectName(u"Table_ClasificacionEquipos")
        self.Table_ClasificacionEquipos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.Layout_ClasificacionGeneral.addWidget(self.Table_ClasificacionEquipos)

        self.Tab_Clasificacion.addTab(self.Tab_ClasificacionGeneral, "")
        self.Tab_Goleadores = QWidget()
        self.Tab_Goleadores.setObjectName(u"Tab_Goleadores")
        self.Layout_Goleadores = QVBoxLayout(self.Tab_Goleadores)
        self.Layout_Goleadores.setObjectName(u"Layout_Goleadores")
        self.Table_Goleadores = QTableWidget(self.Tab_Goleadores)
        self.Table_Goleadores.setObjectName(u"Table_Goleadores")
        self.Table_Goleadores.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.Layout_Goleadores.addWidget(self.Table_Goleadores)

        self.Tab_Clasificacion.addTab(self.Tab_Goleadores, "")
        self.Tab_Tarjetas = QWidget()
        self.Tab_Tarjetas.setObjectName(u"Tab_Tarjetas")
        self.Layout_Tarjetas = QVBoxLayout(self.Tab_Tarjetas)
        self.Layout_Tarjetas.setObjectName(u"Layout_Tarjetas")
        self.Table_Tarjetas = QTableWidget(self.Tab_Tarjetas)
        self.Table_Tarjetas.setObjectName(u"Table_Tarjetas")
        self.Table_Tarjetas.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.Layout_Tarjetas.addWidget(self.Table_Tarjetas)

        self.Tab_Clasificacion.addTab(self.Tab_Tarjetas, "")

        self.Layout_Clasificacion.addWidget(self.Tab_Clasificacion)

        self.Stacked_Paginas.addWidget(self.Page_Clasificacion)
        self.Page_Creditos = QWidget()
        self.Page_Creditos.setObjectName(u"Page_Creditos")
        self.Layout_Creditos = QVBoxLayout(self.Page_Creditos)
        self.Layout_Creditos.setObjectName(u"Layout_Creditos")
        self.Layout_HeaderCreditos = QHBoxLayout()
        self.Layout_HeaderCreditos.setObjectName(u"Layout_HeaderCreditos")
        self.B_VolverDesdeCreditos = QPushButton(self.Page_Creditos)
        self.B_VolverDesdeCreditos.setObjectName(u"B_VolverDesdeCreditos")
        self.B_VolverDesdeCreditos.setMaximumSize(QSize(100, 16777215))

        self.Layout_HeaderCreditos.addWidget(self.B_VolverDesdeCreditos)

        self.Spacer_HeaderCreditos = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_HeaderCreditos.addItem(self.Spacer_HeaderCreditos)


        self.Layout_Creditos.addLayout(self.Layout_HeaderCreditos)

        self.Spacer_CreditosTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Layout_Creditos.addItem(self.Spacer_CreditosTop)

        self.L_TituloCreditos = QLabel(self.Page_Creditos)
        self.L_TituloCreditos.setObjectName(u"L_TituloCreditos")
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(True)
        self.L_TituloCreditos.setFont(font5)
        self.L_TituloCreditos.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_Creditos.addWidget(self.L_TituloCreditos)

        self.L_NombreApp = QLabel(self.Page_Creditos)
        self.L_NombreApp.setObjectName(u"L_NombreApp")
        font6 = QFont()
        font6.setPointSize(14)
        self.L_NombreApp.setFont(font6)
        self.L_NombreApp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_Creditos.addWidget(self.L_NombreApp)

        self.Spacer_CreditosMid1 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Layout_Creditos.addItem(self.Spacer_CreditosMid1)

        self.L_Autor = QLabel(self.Page_Creditos)
        self.L_Autor.setObjectName(u"L_Autor")
        font7 = QFont()
        font7.setPointSize(12)
        self.L_Autor.setFont(font7)
        self.L_Autor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_Creditos.addWidget(self.L_Autor)

        self.L_Version = QLabel(self.Page_Creditos)
        self.L_Version.setObjectName(u"L_Version")
        font8 = QFont()
        font8.setPointSize(11)
        self.L_Version.setFont(font8)
        self.L_Version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_Creditos.addWidget(self.L_Version)

        self.L_FechaActualizacion = QLabel(self.Page_Creditos)
        self.L_FechaActualizacion.setObjectName(u"L_FechaActualizacion")
        self.L_FechaActualizacion.setFont(font8)
        self.L_FechaActualizacion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_Creditos.addWidget(self.L_FechaActualizacion)

        self.Spacer_CreditosMid2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Layout_Creditos.addItem(self.Spacer_CreditosMid2)

        self.Spacer_CreditosBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Layout_Creditos.addItem(self.Spacer_CreditosBottom)

        self.Stacked_Paginas.addWidget(self.Page_Creditos)
        self.Page_Ayuda = QWidget()
        self.Page_Ayuda.setObjectName(u"Page_Ayuda")
        self.Layout_Ayuda = QVBoxLayout(self.Page_Ayuda)
        self.Layout_Ayuda.setObjectName(u"Layout_Ayuda")
        self.Layout_HeaderAyuda = QHBoxLayout()
        self.Layout_HeaderAyuda.setObjectName(u"Layout_HeaderAyuda")
        self.B_VolverDesdeAyuda = QPushButton(self.Page_Ayuda)
        self.B_VolverDesdeAyuda.setObjectName(u"B_VolverDesdeAyuda")
        self.B_VolverDesdeAyuda.setMaximumSize(QSize(100, 16777215))

        self.Layout_HeaderAyuda.addWidget(self.B_VolverDesdeAyuda)

        self.L_TituloAyuda = QLabel(self.Page_Ayuda)
        self.L_TituloAyuda.setObjectName(u"L_TituloAyuda")
        self.L_TituloAyuda.setFont(font1)
        self.L_TituloAyuda.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Layout_HeaderAyuda.addWidget(self.L_TituloAyuda)

        self.Spacer_HeaderAyuda = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Layout_HeaderAyuda.addItem(self.Spacer_HeaderAyuda)


        self.Layout_Ayuda.addLayout(self.Layout_HeaderAyuda)

        self.Textbrowser_Ayuda = QTextBrowser(self.Page_Ayuda)
        self.Textbrowser_Ayuda.setObjectName(u"Textbrowser_Ayuda")

        self.Layout_Ayuda.addWidget(self.Textbrowser_Ayuda)

        self.Stacked_Paginas.addWidget(self.Page_Ayuda)

        self.Layout_Principal.addWidget(self.Stacked_Paginas)

        MainWindow.setCentralWidget(self.Centralwidget)
        self.Menubar = QMenuBar(MainWindow)
        self.Menubar.setObjectName(u"Menubar")
        self.Menubar.setGeometry(QRect(0, 0, 1200, 33))
        self.Menu_Archivo = QMenu(self.Menubar)
        self.Menu_Archivo.setObjectName(u"Menu_Archivo")
        self.Menu_Ver = QMenu(self.Menubar)
        self.Menu_Ver.setObjectName(u"Menu_Ver")
        self.Menu_Herramientas = QMenu(self.Menubar)
        self.Menu_Herramientas.setObjectName(u"Menu_Herramientas")
        self.Menu_Ayuda = QMenu(self.Menubar)
        self.Menu_Ayuda.setObjectName(u"Menu_Ayuda")
        MainWindow.setMenuBar(self.Menubar)
        self.Statusbar = QStatusBar(MainWindow)
        self.Statusbar.setObjectName(u"Statusbar")
        MainWindow.setStatusBar(self.Statusbar)

        self.Menubar.addAction(self.Menu_Archivo.menuAction())
        self.Menubar.addAction(self.Menu_Ver.menuAction())
        self.Menubar.addAction(self.Menu_Herramientas.menuAction())
        self.Menubar.addAction(self.Menu_Ayuda.menuAction())
        self.Menu_Archivo.addAction(self.Action_Salir)
        self.Menu_Ver.addAction(self.Action_MenuPrincipal)
        self.Menu_Herramientas.addAction(self.Action_Notificaciones)
        self.Menu_Ayuda.addAction(self.Action_VerAyuda)
        self.Menu_Ayuda.addAction(self.Action_Creditos)

        self.retranslateUi(MainWindow)

        self.Stacked_Paginas.setCurrentIndex(0)
        self.Tab_Clasificacion.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Torneo de F\u00fatbol - Gesti\u00f3n Completa", None))
        self.Action_Salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.Action_MenuPrincipal.setText(QCoreApplication.translate("MainWindow", u"Ir al Men\u00fa Principal", None))
        self.Action_Notificaciones.setText(QCoreApplication.translate("MainWindow", u"Ver Notificaciones", None))
        self.Action_VerAyuda.setText(QCoreApplication.translate("MainWindow", u"Ver Ayuda", None))
        self.Action_Creditos.setText(QCoreApplication.translate("MainWindow", u"Acerca de...", None))
        self.L_TituloApp.setText(QCoreApplication.translate("MainWindow", u"TORNEO DE F\u00daTBOL", None))
        self.B_GestionEquipos.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Equipos", None))
        self.B_GestionParticipantes.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Participantes", None))
        self.B_GestionCalendario.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n del Calendario", None))
        self.B_ActualizarResultados.setText(QCoreApplication.translate("MainWindow", u"Actualizar Resultados", None))
        self.B_Clasificacion.setText(QCoreApplication.translate("MainWindow", u"Clasificaci\u00f3n y Eliminatorias", None))
        self.B_Creditos.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9ditos", None))
        self.B_Ayuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.B_VolverDesdeEquipos.setText(QCoreApplication.translate("MainWindow", u"\u2190 Volver", None))
        self.L_TituloEquipos.setText(QCoreApplication.translate("MainWindow", u"GESTI\u00d3N DE EQUIPOS", None))
        self.Group_DatosEquipo.setTitle(QCoreApplication.translate("MainWindow", u"Datos del Equipo", None))
        self.L_NombreEquipo.setText(QCoreApplication.translate("MainWindow", u"Nombre del Equipo:", None))
        self.L_CursoEquipo.setText(QCoreApplication.translate("MainWindow", u"Curso:", None))
        self.L_ColorEquipo.setText(QCoreApplication.translate("MainWindow", u"Color de Camiseta:", None))
        self.B_SeleccionarColor.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Color", None))
        self.L_EmblemaEquipo.setText(QCoreApplication.translate("MainWindow", u"Emblema/Logo:", None))
        self.B_SeleccionarEmblema.setText(QCoreApplication.translate("MainWindow", u"Examinar...", None))
        self.L_InfoAdicional.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n Adicional:", None))
        self.B_CrearEquipo.setText(QCoreApplication.translate("MainWindow", u"Crear Equipo", None))
        self.B_EditarEquipo.setText(QCoreApplication.translate("MainWindow", u"Editar Equipo", None))
        self.B_EliminarEquipo.setText(QCoreApplication.translate("MainWindow", u"Eliminar Equipo", None))
        self.B_LimpiarFormEquipo.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.Group_ListaEquipos.setTitle(QCoreApplication.translate("MainWindow", u"Lista de Equipos", None))
        self.B_VerJugadoresEquipo.setText(QCoreApplication.translate("MainWindow", u"Ver Jugadores del Equipo Seleccionado", None))
        self.B_VolverDesdeParticipantes.setText(QCoreApplication.translate("MainWindow", u"\u2190 Volver", None))
        self.L_TituloParticipantes.setText(QCoreApplication.translate("MainWindow", u"GESTI\u00d3N DE PARTICIPANTES", None))
        self.Group_DatosParticipante.setTitle(QCoreApplication.translate("MainWindow", u"Datos del Participante", None))
        self.L_NombreParticipante.setText(QCoreApplication.translate("MainWindow", u"Nombre Completo:", None))
        self.L_FechaNacimiento.setText(QCoreApplication.translate("MainWindow", u"Fecha de Nacimiento:", None))
        self.L_CursoParticipante.setText(QCoreApplication.translate("MainWindow", u"Curso:", None))
        self.L_TipoParticipante.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.Check_EsJugador.setText(QCoreApplication.translate("MainWindow", u"Jugador", None))
        self.Check_EsArbitro.setText(QCoreApplication.translate("MainWindow", u"\u00c1rbitro", None))
        self.L_PosicionJugador.setText(QCoreApplication.translate("MainWindow", u"Posici\u00f3n (si jugador):", None))
        self.Combo_PosicionJugador.setItemText(0, QCoreApplication.translate("MainWindow", u"Portero", None))
        self.Combo_PosicionJugador.setItemText(1, QCoreApplication.translate("MainWindow", u"Defensa", None))
        self.Combo_PosicionJugador.setItemText(2, QCoreApplication.translate("MainWindow", u"Centrocampista", None))
        self.Combo_PosicionJugador.setItemText(3, QCoreApplication.translate("MainWindow", u"Delantero", None))

        self.L_EquipoAsignado.setText(QCoreApplication.translate("MainWindow", u"Equipo Asignado:", None))
        self.L_EstadisticasJugador.setText(QCoreApplication.translate("MainWindow", u"Estad\u00edsticas:", None))
        self.L_Goles.setText(QCoreApplication.translate("MainWindow", u"Goles:", None))
        self.L_TarjetasAmarillas.setText(QCoreApplication.translate("MainWindow", u"T. Amarillas:", None))
        self.L_TarjetasRojas.setText(QCoreApplication.translate("MainWindow", u"T. Rojas:", None))
        self.B_RegistrarParticipante.setText(QCoreApplication.translate("MainWindow", u"Registrar Participante", None))
        self.B_EditarParticipante.setText(QCoreApplication.translate("MainWindow", u"Editar Participante", None))
        self.B_EliminarParticipante.setText(QCoreApplication.translate("MainWindow", u"Eliminar Participante", None))
        self.B_LimpiarFormParticipante.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.Group_ListaParticipantes.setTitle(QCoreApplication.translate("MainWindow", u"Lista de Participantes", None))
        self.L_FiltrarPor.setText(QCoreApplication.translate("MainWindow", u"Filtrar por:", None))
        self.Combo_FiltroParticipantes.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.Combo_FiltroParticipantes.setItemText(1, QCoreApplication.translate("MainWindow", u"Solo Jugadores", None))
        self.Combo_FiltroParticipantes.setItemText(2, QCoreApplication.translate("MainWindow", u"Solo \u00c1rbitros", None))

        self.L_OrdenarPor.setText(QCoreApplication.translate("MainWindow", u"Ordenar por:", None))
        self.Combo_OrdenParticipantes.setItemText(0, QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.Combo_OrdenParticipantes.setItemText(1, QCoreApplication.translate("MainWindow", u"Goles", None))
        self.Combo_OrdenParticipantes.setItemText(2, QCoreApplication.translate("MainWindow", u"Tarjetas Amarillas", None))
        self.Combo_OrdenParticipantes.setItemText(3, QCoreApplication.translate("MainWindow", u"Tarjetas Rojas", None))

        self.B_VolverDesdeCalendario.setText(QCoreApplication.translate("MainWindow", u"\u2190 Volver", None))
        self.L_TituloCalendario.setText(QCoreApplication.translate("MainWindow", u"GESTI\u00d3N DEL CALENDARIO", None))
        self.B_ReiniciarTorneo.setText(QCoreApplication.translate("MainWindow", u"Reiniciar Torneo", None))
        self.Group_DatosPartido.setTitle(QCoreApplication.translate("MainWindow", u"Programar Partido", None))
        self.L_EquipoLocal.setText(QCoreApplication.translate("MainWindow", u"Equipo Local:", None))
        self.L_EquipoVisitante.setText(QCoreApplication.translate("MainWindow", u"Equipo Visitante:", None))
        self.L_FechaPartido.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.L_HoraPartido.setText(QCoreApplication.translate("MainWindow", u"Hora:", None))
        self.L_ArbitroPartido.setText(QCoreApplication.translate("MainWindow", u"\u00c1rbitro Asignado:", None))
        self.L_Eliminatoria.setText(QCoreApplication.translate("MainWindow", u"Eliminatoria:", None))
        self.Combo_Eliminatoria.setItemText(0, QCoreApplication.translate("MainWindow", u"Previa", None))
        self.Combo_Eliminatoria.setItemText(1, QCoreApplication.translate("MainWindow", u"Dieciseisavos", None))
        self.Combo_Eliminatoria.setItemText(2, QCoreApplication.translate("MainWindow", u"Octavos", None))
        self.Combo_Eliminatoria.setItemText(3, QCoreApplication.translate("MainWindow", u"Cuartos", None))
        self.Combo_Eliminatoria.setItemText(4, QCoreApplication.translate("MainWindow", u"Semifinales", None))
        self.Combo_Eliminatoria.setItemText(5, QCoreApplication.translate("MainWindow", u"Final", None))

        self.L_LugarPartido.setText(QCoreApplication.translate("MainWindow", u"Lugar:", None))
        self.B_ProgramarPartido.setText(QCoreApplication.translate("MainWindow", u"Programar Partido", None))
        self.B_EditarPartido.setText(QCoreApplication.translate("MainWindow", u"Editar Partido", None))
        self.B_EliminarPartido.setText(QCoreApplication.translate("MainWindow", u"Eliminar Partido", None))
        self.B_LimpiarFormPartido.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.Group_ListaPartidos.setTitle(QCoreApplication.translate("MainWindow", u"Partidos Programados", None))
        self.L_FiltrarEliminatoria.setText(QCoreApplication.translate("MainWindow", u"Filtrar por eliminatoria:", None))
        self.Combo_FiltroEliminatoria.setItemText(0, QCoreApplication.translate("MainWindow", u"Todas", None))
        self.Combo_FiltroEliminatoria.setItemText(1, QCoreApplication.translate("MainWindow", u"Previa", None))
        self.Combo_FiltroEliminatoria.setItemText(2, QCoreApplication.translate("MainWindow", u"Dieciseisavos", None))
        self.Combo_FiltroEliminatoria.setItemText(3, QCoreApplication.translate("MainWindow", u"Octavos", None))
        self.Combo_FiltroEliminatoria.setItemText(4, QCoreApplication.translate("MainWindow", u"Cuartos", None))
        self.Combo_FiltroEliminatoria.setItemText(5, QCoreApplication.translate("MainWindow", u"Semifinales", None))
        self.Combo_FiltroEliminatoria.setItemText(6, QCoreApplication.translate("MainWindow", u"Final", None))

        ___qtreewidgetitem = self.Tree_Partidos.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Lugar", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Eliminatoria", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"\u00c1rbitro", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Visitante", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Local", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Fecha/Hora", None));
        self.B_VolverDesdeResultados.setText(QCoreApplication.translate("MainWindow", u"\u2190 Volver", None))
        self.L_TituloResultados.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZACI\u00d3N DE RESULTADOS", None))
        self.Group_SeleccionarPartido.setTitle(QCoreApplication.translate("MainWindow", u"Seleccionar Partido", None))
        self.Group_ResultadoPartido.setTitle(QCoreApplication.translate("MainWindow", u"Resultado del Partido", None))
        self.L_NombreEquipoLocal.setText(QCoreApplication.translate("MainWindow", u"Equipo Local", None))
        self.L_GolesLocal.setText(QCoreApplication.translate("MainWindow", u"Goles:", None))
        self.L_VS.setText(QCoreApplication.translate("MainWindow", u"VS", None))
        self.L_NombreEquipoVisitante.setText(QCoreApplication.translate("MainWindow", u"Equipo Visitante", None))
        self.L_GolesVisitante.setText(QCoreApplication.translate("MainWindow", u"Goles:", None))
        self.Group_DetallesJugadores.setTitle(QCoreApplication.translate("MainWindow", u"Registrar Goles y Tarjetas por Jugador", None))
        self.L_SeleccionarJugador.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Jugador:", None))
        self.L_GolesJugador.setText(QCoreApplication.translate("MainWindow", u"Goles:", None))
        self.L_TarjetasAmarillasJugador.setText(QCoreApplication.translate("MainWindow", u"T. Amarillas:", None))
        self.L_TarjetasRojasJugador.setText(QCoreApplication.translate("MainWindow", u"T. Rojas:", None))
        self.B_AgregarEstadisticaJugador.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.B_GuardarResultado.setText(QCoreApplication.translate("MainWindow", u"Guardar Resultado", None))
        self.B_LimpiarResultado.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.Group_PartidosJugados.setTitle(QCoreApplication.translate("MainWindow", u"Partidos Jugados", None))
        self.B_VolverDesdeClasificacion.setText(QCoreApplication.translate("MainWindow", u"\u2190 Volver", None))
        self.L_TituloClasificacion.setText(QCoreApplication.translate("MainWindow", u"CLASIFICACI\u00d3N Y ELIMINATORIAS", None))
        self.B_GenerarSiguienteRonda.setText(QCoreApplication.translate("MainWindow", u"Generar Siguiente Ronda", None))
        self.B_ActualizarClasificacion.setText(QCoreApplication.translate("MainWindow", u"Actualizar Clasificaci\u00f3n", None))
        self.B_ExportarCSV.setText(QCoreApplication.translate("MainWindow", u"Exportar a CSV", None))
        ___qtreewidgetitem1 = self.Tree_Eliminatorias.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Ganador", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Resultado", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Partido", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Eliminatoria", None));
        self.Tab_Clasificacion.setTabText(self.Tab_Clasificacion.indexOf(self.Tab_CuadroEliminatorias), QCoreApplication.translate("MainWindow", u"Cuadro de Eliminatorias", None))
        self.Tab_Clasificacion.setTabText(self.Tab_Clasificacion.indexOf(self.Tab_ClasificacionGeneral), QCoreApplication.translate("MainWindow", u"Clasificaci\u00f3n General", None))
        self.Tab_Clasificacion.setTabText(self.Tab_Clasificacion.indexOf(self.Tab_Goleadores), QCoreApplication.translate("MainWindow", u"M\u00e1ximos Goleadores", None))
        self.Tab_Clasificacion.setTabText(self.Tab_Clasificacion.indexOf(self.Tab_Tarjetas), QCoreApplication.translate("MainWindow", u"Tarjetas", None))
        self.B_VolverDesdeCreditos.setText(QCoreApplication.translate("MainWindow", u"\u2190 Volver", None))
        self.L_TituloCreditos.setText(QCoreApplication.translate("MainWindow", u"CR\u00c9DITOS", None))
        self.L_NombreApp.setText(QCoreApplication.translate("MainWindow", u"Gestor de Torneo de F\u00fatbol", None))
        self.L_Autor.setText(QCoreApplication.translate("MainWindow", u"Autor: Samuel Polanco Mart\u00ednez", None))
        self.L_Version.setText(QCoreApplication.translate("MainWindow", u"Versi\u00f3n: 1.0.0", None))
        self.L_FechaActualizacion.setText(QCoreApplication.translate("MainWindow", u"Fecha: Enero 2026", None))
        self.B_VolverDesdeAyuda.setText(QCoreApplication.translate("MainWindow", u"\u2190 Volver", None))
        self.L_TituloAyuda.setText(QCoreApplication.translate("MainWindow", u"AYUDA", None))
        self.Textbrowser_Ayuda.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700;\">Gestor de Torneo de F\u00fatbol</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sistema para gestionar torneos de eliminatorias.</p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Equipos</span></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Crea equipos con nombre, curso, color y emblema.</p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Participantes</span></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Registra jugadores y \u00e1rbitros. As\u00edgnalos a equipos.</p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Calendario</span></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Programa partidos por eliminatoria. Solo los ganadores avanzan.</p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Resultados</span></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actualiza goles y estad\u00edsticas de cada partido jugado.</p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Clasificaci\u00f3n</span></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ve eliminatorias, clasificaci\u00f3n, goleadores y tarjetas.</p></body></html>", None))
        self.Menu_Archivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.Menu_Ver.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.Menu_Herramientas.setTitle(QCoreApplication.translate("MainWindow", u"Herramientas", None))
        self.Menu_Ayuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

