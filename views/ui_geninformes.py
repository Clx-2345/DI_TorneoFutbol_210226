# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geninformesfhjOBq.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from PySide6.QtCore import (QCoreApplication, QRect)
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QPushButton,
    QWidget, QMessageBox,QInputDialog)

class Ui_Form(object):
        
   
    
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.btnGenInforme = QPushButton(Form)
        self.btnGenInforme.setObjectName(u"btnGenInforme")
        self.btnGenInforme.setGeometry(QRect(270, 100, 111, 23))
        self.comboBoxFicheros = QComboBox(Form)
        self.comboBoxFicheros.setObjectName(u"comboBoxFicheros")
        self.comboBoxFicheros.setGeometry(QRect(20, 100, 231, 23))
        self.cdrTxtRutaSalida = QLineEdit(Form)
        self.cdrTxtRutaSalida.setObjectName(u"cdrTxtRuta")
        self.cdrTxtRutaSalida.setGeometry(QRect(40, 180, 281, 23))
        self.cdrTxtRutaEntrada = QLineEdit(Form)
        self.cdrTxtRutaEntrada.setObjectName(u"cdrTxtRuta_2")
        self.cdrTxtRutaEntrada.setGeometry(QRect(20, 40, 281, 23))
        """self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 40, 111, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 180, 111, 20))
      """
        self.retranslateUi(Form)

        self.cdrTxtRutaEntrada.returnPressed.connect(self.cambiar_ruta)
        self.btnGenInforme.clicked.connect(self.generar_informe)
        try:
            self.comboBoxFicheros.addItems(os.listdir(self.cdrTxtRutaEntrada.text()))
        except FileNotFoundError:
            self.aviso("Aviso ruta de entrada","Indica la ruta de los ficheros jrxml")
            
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Generar Informes F\u00e1brica", None))
        self.btnGenInforme.setText(QCoreApplication.translate("Form", u"Generar Informe", None))
        #self.cdrTxtRutaSalida.setText(QCoreApplication.translate("Form", u"/home/luis/Dropbox/Instituto/VirtualShared/DI/EjemploTema7/informes/pdf", None))
        self.cdrTxtRutaSalida.setPlaceholderText(QCoreApplication.translate("Form", u"Ruta ficheros generados", None))
        self.cdrTxtRutaEntrada.setPlaceholderText(QCoreApplication.translate("Form", u"Ruta ficheros jrxml", None))
        self.cdrTxtRutaEntrada.setToolTip(QCoreApplication.translate("Form", u"Pulsar enter para actualizar la lista de ficherps", None))
        #self.cdrTxtRutaEntrada.setText(QCoreApplication.translate("Form", u"/home/luis/Dropbox/Instituto/VirtualShared/DI/EjemploTema7/informes", None))
    # retranslateUi

