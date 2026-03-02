# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reloj_digital.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_RelojDigital(object):
    def setupUi(self, RelojDigital):
        if not RelojDigital.objectName():
            RelojDigital.setObjectName(u"RelojDigital")
        RelojDigital.resize(400, 200)
        self.verticalLayout = QVBoxLayout(RelojDigital)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lcdDisplay = QLCDNumber(RelojDigital)
        self.lcdDisplay.setObjectName(u"lcdDisplay")
        self.lcdDisplay.setMinimumSize(QSize(0, 80))
        self.lcdDisplay.setFrameShape(QFrame.Box)
        self.lcdDisplay.setFrameShadow(QFrame.Raised)
        self.lcdDisplay.setDigitCount(8)
        self.lcdDisplay.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout.addWidget(self.lcdDisplay)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnStart = QPushButton(RelojDigital)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout.addWidget(self.btnStart)

        self.btnPause = QPushButton(RelojDigital)
        self.btnPause.setObjectName(u"btnPause")
        self.btnPause.setEnabled(False)

        self.horizontalLayout.addWidget(self.btnPause)

        self.btnReset = QPushButton(RelojDigital)
        self.btnReset.setObjectName(u"btnReset")

        self.horizontalLayout.addWidget(self.btnReset)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lblMode = QLabel(RelojDigital)
        self.lblMode.setObjectName(u"lblMode")
        self.lblMode.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblMode)


        self.retranslateUi(RelojDigital)

        QMetaObject.connectSlotsByName(RelojDigital)
    # setupUi

    def retranslateUi(self, RelojDigital):
        RelojDigital.setWindowTitle(QCoreApplication.translate("RelojDigital", u"Reloj Digital", None))
        self.btnStart.setText(QCoreApplication.translate("RelojDigital", u"Iniciar", None))
        self.btnPause.setText(QCoreApplication.translate("RelojDigital", u"Pausar", None))
        self.btnReset.setText(QCoreApplication.translate("RelojDigital", u"Reiniciar", None))
        self.lblMode.setText(QCoreApplication.translate("RelojDigital", u"Modo: Reloj", None))
    # retranslateUi

