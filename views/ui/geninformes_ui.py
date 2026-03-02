# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geninformes.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(425, 300)
        self.btnGenInforme = QPushButton(Form)
        self.btnGenInforme.setObjectName(u"btnGenInforme")
        self.btnGenInforme.setGeometry(QRect(270, 100, 111, 23))
        self.comboBoxFicheros = QComboBox(Form)
        self.comboBoxFicheros.setObjectName(u"comboBoxFicheros")
        self.comboBoxFicheros.setGeometry(QRect(20, 100, 231, 23))
        self.cdrTxtRutaSalida = QLineEdit(Form)
        self.cdrTxtRutaSalida.setObjectName(u"cdrTxtRutaSalida")
        self.cdrTxtRutaSalida.setGeometry(QRect(130, 180, 281, 23))
        self.cdrTxtRutaEntrada = QLineEdit(Form)
        self.cdrTxtRutaEntrada.setObjectName(u"cdrTxtRutaEntrada")
        self.cdrTxtRutaEntrada.setGeometry(QRect(120, 40, 281, 23))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 40, 111, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 180, 111, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Generar Informes F\u00e1brica", None))
        self.btnGenInforme.setText(QCoreApplication.translate("Form", u"Generar Informe", None))
        self.cdrTxtRutaSalida.setText("")
        self.cdrTxtRutaSalida.setPlaceholderText(QCoreApplication.translate("Form", u"Ruta ficheros generados", None))
#if QT_CONFIG(tooltip)
        self.cdrTxtRutaEntrada.setToolTip(QCoreApplication.translate("Form", u"Pulsar enter para actualizar la lista de ficherps", None))
#endif // QT_CONFIG(tooltip)
        self.cdrTxtRutaEntrada.setText(QCoreApplication.translate("Form", u"Ruta ficheros jrxml", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ruta fichero jrxml", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Ruta informes PDF", None))
    # retranslateUi

