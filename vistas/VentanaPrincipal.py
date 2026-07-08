# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaDamas.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_VentanaDamas(object):
    def setupUi(self, VentanaDamas):
        if not VentanaDamas.objectName():
            VentanaDamas.setObjectName(u"VentanaDamas")
        VentanaDamas.resize(1280, 720)
        VentanaDamas.setMinimumSize(QSize(1280, 720))
        self.centralwidget = QWidget(VentanaDamas)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.vista_tablero = QGraphicsView(self.centralwidget)
        self.vista_tablero.setObjectName(u"vista_tablero")

        self.horizontalLayout.addWidget(self.vista_tablero)

        self.panel_lateral = QFrame(self.centralwidget)
        self.panel_lateral.setObjectName(u"panel_lateral")
        self.panel_lateral.setMinimumSize(QSize(300, 0))
        self.panel_lateral.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout = QVBoxLayout(self.panel_lateral)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titulo_panel_lateral = QLabel(self.panel_lateral)
        self.titulo_panel_lateral.setObjectName(u"titulo_panel_lateral")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.titulo_panel_lateral.setFont(font)
        self.titulo_panel_lateral.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.titulo_panel_lateral)

        self.temporizador_layout = QVBoxLayout()
        self.temporizador_layout.setSpacing(0)
        self.temporizador_layout.setObjectName(u"temporizador_layout")
        self.temporizador_layout.setContentsMargins(-1, 4, -1, 4)
        self.temporizador_tiempo = QLabel(self.panel_lateral)
        self.temporizador_tiempo.setObjectName(u"temporizador_tiempo")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.temporizador_tiempo.setFont(font1)
        self.temporizador_tiempo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.temporizador_layout.addWidget(self.temporizador_tiempo)

        self.temporizador_titulo = QLabel(self.panel_lateral)
        self.temporizador_titulo.setObjectName(u"temporizador_titulo")
        self.temporizador_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.temporizador_layout.addWidget(self.temporizador_titulo)


        self.verticalLayout.addLayout(self.temporizador_layout)

        self.jugadores_frame = QFrame(self.panel_lateral)
        self.jugadores_frame.setObjectName(u"jugadores_frame")
        self.jugadores_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.jugadores_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.jugadores_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.jugador_1 = QVBoxLayout()
        self.jugador_1.setSpacing(0)
        self.jugador_1.setObjectName(u"jugador_1")
        self.jugador_1.setContentsMargins(4, 10, 4, 10)
        self.jugador_1_top_frame = QFrame(self.jugadores_frame)
        self.jugador_1_top_frame.setObjectName(u"jugador_1_top_frame")
        self.horizontalLayout_3 = QHBoxLayout(self.jugador_1_top_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.jugador_1_titulo = QLabel(self.jugador_1_top_frame)
        self.jugador_1_titulo.setObjectName(u"jugador_1_titulo")

        self.horizontalLayout_3.addWidget(self.jugador_1_titulo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.jugador_1_tipo = QComboBox(self.jugador_1_top_frame)
        self.jugador_1_tipo.addItem("")
        self.jugador_1_tipo.addItem("")
        self.jugador_1_tipo.setObjectName(u"jugador_1_tipo")

        self.horizontalLayout_3.addWidget(self.jugador_1_tipo)


        self.jugador_1.addWidget(self.jugador_1_top_frame)

        self.jugador_1_bottom_frame = QHBoxLayout()
        self.jugador_1_bottom_frame.setSpacing(4)
        self.jugador_1_bottom_frame.setObjectName(u"jugador_1_bottom_frame")
        self.jugador_1_nombre_titulo = QLabel(self.jugadores_frame)
        self.jugador_1_nombre_titulo.setObjectName(u"jugador_1_nombre_titulo")

        self.jugador_1_bottom_frame.addWidget(self.jugador_1_nombre_titulo)

        self.jugador_1_nombre_input = QLineEdit(self.jugadores_frame)
        self.jugador_1_nombre_input.setObjectName(u"jugador_1_nombre_input")

        self.jugador_1_bottom_frame.addWidget(self.jugador_1_nombre_input)


        self.jugador_1.addLayout(self.jugador_1_bottom_frame)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_17 = QLabel(self.jugadores_frame)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_13.addWidget(self.label_17)

        self.label_18 = QLabel(self.jugadores_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_18)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_19 = QLabel(self.jugadores_frame)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_14.addWidget(self.label_19)

        self.label_20 = QLabel(self.jugadores_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_20)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.jugadores_frame)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_12.addWidget(self.label_15)

        self.label_16 = QLabel(self.jugadores_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_16)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)


        self.jugador_1.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.jugador_1)

        self.jugador_2 = QVBoxLayout()
        self.jugador_2.setSpacing(0)
        self.jugador_2.setObjectName(u"jugador_2")
        self.jugador_2.setContentsMargins(4, 10, 4, 10)
        self.jugador_2_top_frame = QFrame(self.jugadores_frame)
        self.jugador_2_top_frame.setObjectName(u"jugador_2_top_frame")
        self.horizontalLayout_4 = QHBoxLayout(self.jugador_2_top_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.jugador_2_titulo = QLabel(self.jugador_2_top_frame)
        self.jugador_2_titulo.setObjectName(u"jugador_2_titulo")

        self.horizontalLayout_4.addWidget(self.jugador_2_titulo)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.jugador_2_tipo = QComboBox(self.jugador_2_top_frame)
        self.jugador_2_tipo.addItem("")
        self.jugador_2_tipo.addItem("")
        self.jugador_2_tipo.setObjectName(u"jugador_2_tipo")

        self.horizontalLayout_4.addWidget(self.jugador_2_tipo)


        self.jugador_2.addWidget(self.jugador_2_top_frame)

        self.jugador_2_bottom_frame = QHBoxLayout()
        self.jugador_2_bottom_frame.setSpacing(4)
        self.jugador_2_bottom_frame.setObjectName(u"jugador_2_bottom_frame")
        self.jugador_2_nombre_titulo = QLabel(self.jugadores_frame)
        self.jugador_2_nombre_titulo.setObjectName(u"jugador_2_nombre_titulo")

        self.jugador_2_bottom_frame.addWidget(self.jugador_2_nombre_titulo)

        self.jugador_2_nombre_input = QLineEdit(self.jugadores_frame)
        self.jugador_2_nombre_input.setObjectName(u"jugador_2_nombre_input")

        self.jugador_2_bottom_frame.addWidget(self.jugador_2_nombre_input)


        self.jugador_2.addLayout(self.jugador_2_bottom_frame)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_21 = QLabel(self.jugadores_frame)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_15.addWidget(self.label_21)

        self.label_22 = QLabel(self.jugadores_frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_22)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_23 = QLabel(self.jugadores_frame)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_16.addWidget(self.label_23)

        self.label_24 = QLabel(self.jugadores_frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_24)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_25 = QLabel(self.jugadores_frame)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_17.addWidget(self.label_25)

        self.label_26 = QLabel(self.jugadores_frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_26)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)


        self.jugador_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.jugador_2)


        self.verticalLayout.addWidget(self.jugadores_frame)

        self.pushButton = QPushButton(self.panel_lateral)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: rgb(147, 255, 154);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.panel_lateral)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 160, 160);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 175, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.panel_lateral)

        VentanaDamas.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VentanaDamas)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 33))
        VentanaDamas.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VentanaDamas)
        self.statusbar.setObjectName(u"statusbar")
        VentanaDamas.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaDamas)

        QMetaObject.connectSlotsByName(VentanaDamas)
    # setupUi

    def retranslateUi(self, VentanaDamas):
        VentanaDamas.setWindowTitle(QCoreApplication.translate("VentanaDamas", u"MainWindow", None))
        self.titulo_panel_lateral.setText(QCoreApplication.translate("VentanaDamas", u"Damas - Tarea 2 IIA", None))
        self.temporizador_tiempo.setText(QCoreApplication.translate("VentanaDamas", u"00:00", None))
        self.temporizador_titulo.setText(QCoreApplication.translate("VentanaDamas", u"Tiempo Restante", None))
        self.jugador_1_titulo.setText(QCoreApplication.translate("VentanaDamas", u"Jugador 1", None))
        self.jugador_1_tipo.setItemText(0, QCoreApplication.translate("VentanaDamas", u"Persona", None))
        self.jugador_1_tipo.setItemText(1, QCoreApplication.translate("VentanaDamas", u"IA", None))

        self.jugador_1_nombre_titulo.setText(QCoreApplication.translate("VentanaDamas", u"Nombre", None))
        self.jugador_1_nombre_input.setText(QCoreApplication.translate("VentanaDamas", u"Nombre Jugador 1", None))
        self.label_17.setText(QCoreApplication.translate("VentanaDamas", u"Piezas Restantes", None))
        self.label_18.setText(QCoreApplication.translate("VentanaDamas", u"0", None))
        self.label_19.setText(QCoreApplication.translate("VentanaDamas", u"Piezas Comidas", None))
        self.label_20.setText(QCoreApplication.translate("VentanaDamas", u"0", None))
        self.label_15.setText(QCoreApplication.translate("VentanaDamas", u"Tiempo Jugado", None))
        self.label_16.setText(QCoreApplication.translate("VentanaDamas", u"00:00", None))
        self.jugador_2_titulo.setText(QCoreApplication.translate("VentanaDamas", u"Jugador 2", None))
        self.jugador_2_tipo.setItemText(0, QCoreApplication.translate("VentanaDamas", u"Persona", None))
        self.jugador_2_tipo.setItemText(1, QCoreApplication.translate("VentanaDamas", u"IA", None))

        self.jugador_2_nombre_titulo.setText(QCoreApplication.translate("VentanaDamas", u"Nombre", None))
        self.jugador_2_nombre_input.setText(QCoreApplication.translate("VentanaDamas", u"Nombre Jugador 2", None))
        self.label_21.setText(QCoreApplication.translate("VentanaDamas", u"Piezas Restantes", None))
        self.label_22.setText(QCoreApplication.translate("VentanaDamas", u"0", None))
        self.label_23.setText(QCoreApplication.translate("VentanaDamas", u"Piezas Comidas", None))
        self.label_24.setText(QCoreApplication.translate("VentanaDamas", u"0", None))
        self.label_25.setText(QCoreApplication.translate("VentanaDamas", u"Tiempo Jugado", None))
        self.label_26.setText(QCoreApplication.translate("VentanaDamas", u"00:00", None))
        self.pushButton.setText(QCoreApplication.translate("VentanaDamas", u"Iniciar", None))
        self.pushButton_2.setText(QCoreApplication.translate("VentanaDamas", u"Reiniciar Partida", None))
    # retranslateUi

