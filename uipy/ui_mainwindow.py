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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(939, 600)
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
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pendientes_tableWidget = QTableWidget(self.groupBox_2)
        if (self.pendientes_tableWidget.columnCount() < 3):
            self.pendientes_tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.pendientes_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.pendientes_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.pendientes_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.pendientes_tableWidget.setObjectName(u"pendientes_tableWidget")
        self.pendientes_tableWidget.setEnabled(False)
        self.pendientes_tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.pendientes_tableWidget.setAutoFillBackground(False)
        self.pendientes_tableWidget.setStyleSheet(u"background-color: white;")
        self.pendientes_tableWidget.horizontalHeader().setVisible(True)
        self.pendientes_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.pendientes_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.pendientes_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.pendientes_tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.pendientes_tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.pendientes_tableWidget, 1, 0, 1, 1)

        self.pendientes_label = QLabel(self.groupBox_2)
        self.pendientes_label.setObjectName(u"pendientes_label")
        self.pendientes_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.pendientes_label, 2, 0, 1, 1)

        self.actual_label = QLabel(self.groupBox_2)
        self.actual_label.setObjectName(u"actual_label")
        self.actual_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.actual_label, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.proceso_tableWidget = QTableWidget(self.groupBox)
        if (self.proceso_tableWidget.columnCount() < 1):
            self.proceso_tableWidget.setColumnCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.proceso_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        if (self.proceso_tableWidget.rowCount() < 5):
            self.proceso_tableWidget.setRowCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.proceso_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.proceso_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.proceso_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.proceso_tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.proceso_tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        self.proceso_tableWidget.setObjectName(u"proceso_tableWidget")
        self.proceso_tableWidget.setEnabled(False)
        self.proceso_tableWidget.setStyleSheet(u"background-color: white;")

        self.gridLayout.addWidget(self.proceso_tableWidget, 1, 0, 1, 1)

        self.procesos_pushButton = QPushButton(self.groupBox)
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
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.procesos_pushButton.setPalette(palette1)
        self.procesos_pushButton.setStyleSheet(u"background-color: #dda1b6;\n"
"color: black;")

        self.gridLayout.addWidget(self.procesos_pushButton, 3, 0, 1, 1)

        self.proceso_label = QLabel(self.groupBox)
        self.proceso_label.setObjectName(u"proceso_label")
        self.proceso_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.proceso_label, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.terminados_label = QLabel(self.groupBox_3)
        self.terminados_label.setObjectName(u"terminados_label")
        self.terminados_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.terminados_label, 0, 0, 1, 1)

        self.terminados_tableWidget = QTableWidget(self.groupBox_3)
        if (self.terminados_tableWidget.columnCount() < 4):
            self.terminados_tableWidget.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.terminados_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.terminados_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.terminados_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.terminados_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        self.terminados_tableWidget.setObjectName(u"terminados_tableWidget")
        self.terminados_tableWidget.setEnabled(False)
        self.terminados_tableWidget.setStyleSheet(u"background-color: white;")

        self.gridLayout_3.addWidget(self.terminados_tableWidget, 1, 0, 1, 1)

        self.contador_label = QLabel(self.groupBox_3)
        self.contador_label.setObjectName(u"contador_label")
        self.contador_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.contador_label, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 939, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Planificador", None))
        self.groupBox_2.setTitle("")
        ___qtablewidgetitem = self.pendientes_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.pendientes_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"TME", None));
        ___qtablewidgetitem2 = self.pendientes_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"TT", None));
        self.pendientes_label.setText(QCoreApplication.translate("MainWindow", u"Lotes pendientes: 0", None))
        self.actual_label.setText(QCoreApplication.translate("MainWindow", u"Lote actual", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem3 = self.proceso_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Datos", None));
        ___qtablewidgetitem4 = self.proceso_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem5 = self.proceso_tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem6 = self.proceso_tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"TME", None));
        ___qtablewidgetitem7 = self.proceso_tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Tiempo transcurrido", None));
        ___qtablewidgetitem8 = self.proceso_tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Tiempo restante", None));
        self.procesos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar Procesos", None))
        self.proceso_label.setText(QCoreApplication.translate("MainWindow", u"Proceso en ejecuci\u00f3n", None))
        self.groupBox_3.setTitle("")
        self.terminados_label.setText(QCoreApplication.translate("MainWindow", u"Procesos terminados", None))
        ___qtablewidgetitem9 = self.terminados_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Lote", None));
        ___qtablewidgetitem10 = self.terminados_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem11 = self.terminados_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem12 = self.terminados_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        self.contador_label.setText(QCoreApplication.translate("MainWindow", u"Contador general: 0", None))
    # retranslateUi

