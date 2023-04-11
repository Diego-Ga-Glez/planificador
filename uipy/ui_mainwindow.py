# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1137, 635)
        palette = QPalette()
        brush = QBrush(QColor(241, 228, 232, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"background-color: #f1e4e8;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.proceso_tableWidget = QTableWidget(self.groupBox)
        if (self.proceso_tableWidget.columnCount() < 1):
            self.proceso_tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.proceso_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.proceso_tableWidget.rowCount() < 7):
            self.proceso_tableWidget.setRowCount(7)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.proceso_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.proceso_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.proceso_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.proceso_tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.proceso_tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.proceso_tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.proceso_tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem7)
        self.proceso_tableWidget.setObjectName(u"proceso_tableWidget")
        self.proceso_tableWidget.setEnabled(True)
        self.proceso_tableWidget.setFocusPolicy(Qt.NoFocus)
        self.proceso_tableWidget.setStyleSheet(u"background-color: white;")
        self.proceso_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.proceso_tableWidget.horizontalHeader().setDefaultSectionSize(110)
        self.proceso_tableWidget.verticalHeader().setDefaultSectionSize(29)

        self.gridLayout.addWidget(self.proceso_tableWidget, 0, 0, 1, 1)

        self.quantum_label = QLabel(self.groupBox)
        self.quantum_label.setObjectName(u"quantum_label")
        self.quantum_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.quantum_label, 2, 0, 1, 1)

        self.contador_label = QLabel(self.groupBox)
        self.contador_label.setObjectName(u"contador_label")
        self.contador_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.contador_label, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pendientes_tableWidget = QTableWidget(self.groupBox_2)
        if (self.pendientes_tableWidget.columnCount() < 4):
            self.pendientes_tableWidget.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.pendientes_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.pendientes_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.pendientes_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.pendientes_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.pendientes_tableWidget.setObjectName(u"pendientes_tableWidget")
        self.pendientes_tableWidget.setEnabled(True)
        self.pendientes_tableWidget.setFocusPolicy(Qt.NoFocus)
        self.pendientes_tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.pendientes_tableWidget.setAutoFillBackground(False)
        self.pendientes_tableWidget.setStyleSheet(u"background-color: white;")
        self.pendientes_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pendientes_tableWidget.horizontalHeader().setVisible(True)
        self.pendientes_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.pendientes_tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.pendientes_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.pendientes_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.pendientes_tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.pendientes_tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.pendientes_tableWidget, 0, 0, 1, 3)

        self.pendientes_label = QLabel(self.groupBox_2)
        self.pendientes_label.setObjectName(u"pendientes_label")
        self.pendientes_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.pendientes_label, 1, 0, 1, 3)

        self.sig_label = QLabel(self.groupBox_2)
        self.sig_label.setObjectName(u"sig_label")
        self.sig_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.sig_label, 2, 0, 1, 1)

        self.idSig_label = QLabel(self.groupBox_2)
        self.idSig_label.setObjectName(u"idSig_label")
        self.idSig_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.idSig_label, 2, 1, 1, 1)

        self.tamSig_label = QLabel(self.groupBox_2)
        self.tamSig_label.setObjectName(u"tamSig_label")
        self.tamSig_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.tamSig_label, 2, 2, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.bloqueados_tableWidget = QTableWidget(self.groupBox_5)
        if (self.bloqueados_tableWidget.columnCount() < 3):
            self.bloqueados_tableWidget.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.bloqueados_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.bloqueados_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.bloqueados_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        self.bloqueados_tableWidget.setObjectName(u"bloqueados_tableWidget")
        self.bloqueados_tableWidget.setEnabled(True)
        self.bloqueados_tableWidget.setFocusPolicy(Qt.NoFocus)
        self.bloqueados_tableWidget.setStyleSheet(u"background-color: white;")
        self.bloqueados_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.bloqueados_tableWidget.horizontalHeader().setDefaultSectionSize(140)

        self.gridLayout_6.addWidget(self.bloqueados_tableWidget, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.terminados_tableWidget = QTableWidget(self.groupBox_6)
        if (self.terminados_tableWidget.columnCount() < 4):
            self.terminados_tableWidget.setColumnCount(4)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.terminados_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.terminados_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.terminados_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.terminados_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        self.terminados_tableWidget.setObjectName(u"terminados_tableWidget")
        self.terminados_tableWidget.setEnabled(True)
        self.terminados_tableWidget.setFocusPolicy(Qt.NoFocus)
        self.terminados_tableWidget.setStyleSheet(u"background-color: white;")
        self.terminados_tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.terminados_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.terminados_tableWidget.horizontalHeader().setDefaultSectionSize(95)

        self.gridLayout_7.addWidget(self.terminados_tableWidget, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_6, 1, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.memoria1_tableWidget = QTableWidget(self.groupBox_4)
        if (self.memoria1_tableWidget.columnCount() < 2):
            self.memoria1_tableWidget.setColumnCount(2)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.memoria1_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.memoria1_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        self.memoria1_tableWidget.setObjectName(u"memoria1_tableWidget")
        self.memoria1_tableWidget.setFocusPolicy(Qt.NoFocus)
        self.memoria1_tableWidget.setStyleSheet(u"background-color: white;")
        self.memoria1_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.memoria1_tableWidget.verticalHeader().setVisible(False)
        self.memoria1_tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.memoria1_tableWidget, 0, 1, 1, 1)

        self.memoria2_tableWidget = QTableWidget(self.groupBox_4)
        if (self.memoria2_tableWidget.columnCount() < 2):
            self.memoria2_tableWidget.setColumnCount(2)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.memoria2_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.memoria2_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        self.memoria2_tableWidget.setObjectName(u"memoria2_tableWidget")
        self.memoria2_tableWidget.setFocusPolicy(Qt.NoFocus)
        self.memoria2_tableWidget.setStyleSheet(u"background-color: white;")
        self.memoria2_tableWidget.verticalHeader().setVisible(False)

        self.gridLayout_5.addWidget(self.memoria2_tableWidget, 0, 2, 1, 1)

        self.tiempos_pushButton = QPushButton(self.groupBox_4)
        self.tiempos_pushButton.setObjectName(u"tiempos_pushButton")
        self.tiempos_pushButton.setEnabled(False)
        self.tiempos_pushButton.setStyleSheet(u"background-color: #dda1b6;")

        self.gridLayout_5.addWidget(self.tiempos_pushButton, 1, 2, 1, 1)

        self.procesos_pushButton = QPushButton(self.groupBox_4)
        self.procesos_pushButton.setObjectName(u"procesos_pushButton")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush3 = QBrush(QColor(221, 161, 182, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.procesos_pushButton.setPalette(palette1)
        self.procesos_pushButton.setStyleSheet(u"background-color: #dda1b6;")

        self.gridLayout_5.addWidget(self.procesos_pushButton, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_4, 0, 2, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1137, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Planificador", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Proceso en ejecuci\u00f3n", None))
        ___qtablewidgetitem = self.proceso_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Datos", None));
        ___qtablewidgetitem1 = self.proceso_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.proceso_tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None));
        ___qtablewidgetitem3 = self.proceso_tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem4 = self.proceso_tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"TME", None));
        ___qtablewidgetitem5 = self.proceso_tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tiempo transcurrido", None));
        ___qtablewidgetitem6 = self.proceso_tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Tiempo transcurrido quantum", None));
        ___qtablewidgetitem7 = self.proceso_tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Tiempo restante", None));
        self.quantum_label.setText(QCoreApplication.translate("MainWindow", u"Quantum: 0", None))
        self.contador_label.setText(QCoreApplication.translate("MainWindow", u"Contador general: 0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Procesos listos", None))
        ___qtablewidgetitem8 = self.pendientes_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem9 = self.pendientes_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None));
        ___qtablewidgetitem10 = self.pendientes_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"TME", None));
        ___qtablewidgetitem11 = self.pendientes_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"TT", None));
        self.pendientes_label.setText(QCoreApplication.translate("MainWindow", u"Numero de procesos nuevos: 0", None))
        self.sig_label.setText(QCoreApplication.translate("MainWindow", u"Sig. a ingresar:", None))
        self.idSig_label.setText(QCoreApplication.translate("MainWindow", u"ID: null", None))
        self.tamSig_label.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o: null", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Procesos bloqueados", None))
        ___qtablewidgetitem12 = self.bloqueados_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem13 = self.bloqueados_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None));
        ___qtablewidgetitem14 = self.bloqueados_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"TB", None));
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Procesos terminados", None))
        ___qtablewidgetitem15 = self.terminados_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem16 = self.terminados_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None));
        ___qtablewidgetitem17 = self.terminados_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem18 = self.terminados_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Memoria", None))
        ___qtablewidgetitem19 = self.memoria1_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Marco", None));
        ___qtablewidgetitem20 = self.memoria1_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Espacio ocupado", None));
        ___qtablewidgetitem21 = self.memoria2_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Marco", None));
        ___qtablewidgetitem22 = self.memoria2_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Espacio ocupado", None));
        self.tiempos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar Tabla de Procesos", None))
        self.procesos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar Procesos", None))
    # retranslateUi

