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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QListView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.procesos_pushButton = QPushButton(self.centralwidget)
        self.procesos_pushButton.setObjectName(u"procesos_pushButton")

        self.gridLayout.addWidget(self.procesos_pushButton, 1, 1, 1, 1)

        self.procesados_listView = QListView(self.centralwidget)
        self.procesados_listView.setObjectName(u"procesados_listView")

        self.gridLayout.addWidget(self.procesados_listView, 0, 1, 1, 1)

        self.terminados_listView = QListView(self.centralwidget)
        self.terminados_listView.setObjectName(u"terminados_listView")

        self.gridLayout.addWidget(self.terminados_listView, 0, 2, 1, 1)

        self.pendientes_tableWidget = QTableWidget(self.centralwidget)
        if (self.pendientes_tableWidget.columnCount() < 2):
            self.pendientes_tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.pendientes_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.pendientes_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.pendientes_tableWidget.setObjectName(u"pendientes_tableWidget")

        self.gridLayout.addWidget(self.pendientes_tableWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.procesos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar Procesos", None))
        ___qtablewidgetitem = self.pendientes_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.pendientes_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
    # retranslateUi

