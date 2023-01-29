# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 629)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(False)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_pendientes = QLabel(self.centralwidget)
        self.lb_pendientes.setObjectName(u"lb_pendientes")
        self.lb_pendientes.setEnabled(False)
        self.lb_pendientes.setLayoutDirection(Qt.LeftToRight)
        self.lb_pendientes.setAutoFillBackground(False)
        self.lb_pendientes.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_pendientes, 0, 0, 1, 1)

        self.lb_terminados = QLabel(self.centralwidget)
        self.lb_terminados.setObjectName(u"lb_terminados")
        self.lb_terminados.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_terminados, 0, 2, 1, 1)

        self.tb_pendientes = QTableView(self.centralwidget)
        self.tb_pendientes.setObjectName(u"tb_pendientes")

        self.gridLayout.addWidget(self.tb_pendientes, 1, 0, 3, 1)

        self.tb_terminados = QTableView(self.centralwidget)
        self.tb_terminados.setObjectName(u"tb_terminados")
        self.tb_terminados.setShowGrid(True)
        self.tb_terminados.setGridStyle(Qt.DashLine)

        self.gridLayout.addWidget(self.tb_terminados, 1, 2, 3, 1)

        self.btn_procesos = QPushButton(self.centralwidget)
        self.btn_procesos.setObjectName(u"btn_procesos")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_procesos.sizePolicy().hasHeightForWidth())
        self.btn_procesos.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_procesos, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.tb_procesados = QTableView(self.centralwidget)
        self.tb_procesados.setObjectName(u"tb_procesados")
        self.tb_procesados.setEnabled(False)

        self.gridLayout.addWidget(self.tb_procesados, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 772, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Planificador", None))
        self.lb_pendientes.setText(QCoreApplication.translate("MainWindow", u"Procesos Pendientes: ", None))
        self.lb_terminados.setText(QCoreApplication.translate("MainWindow", u"Procesos Terminados", None))
        self.btn_procesos.setText(QCoreApplication.translate("MainWindow", u"Iniciar Procesos", None))
    # retranslateUi

