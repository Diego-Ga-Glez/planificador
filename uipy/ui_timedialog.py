# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timedialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QGroupBox, QHeaderView, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_TimeDialog(object):
    def setupUi(self, TimeDialog):
        if not TimeDialog.objectName():
            TimeDialog.setObjectName(u"TimeDialog")
        TimeDialog.resize(851, 352)
        TimeDialog.setFocusPolicy(Qt.StrongFocus)
        TimeDialog.setStyleSheet(u"background-color: #f1e4e8;")
        self.gridLayout_4 = QGridLayout(TimeDialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(TimeDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tiempos_tableWidget = QTableWidget(self.groupBox)
        if (self.tiempos_tableWidget.columnCount() < 12):
            self.tiempos_tableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tiempos_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tiempos_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tiempos_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tiempos_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tiempos_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tiempos_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tiempos_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tiempos_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tiempos_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tiempos_tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tiempos_tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tiempos_tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tiempos_tableWidget.setObjectName(u"tiempos_tableWidget")
        self.tiempos_tableWidget.setEnabled(True)
        self.tiempos_tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tiempos_tableWidget.setStyleSheet(u"background-color: white;")
        self.tiempos_tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tiempos_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tiempos_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout.addWidget(self.tiempos_tableWidget, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(TimeDialog)

        QMetaObject.connectSlotsByName(TimeDialog)
    # setupUi

    def retranslateUi(self, TimeDialog):
        TimeDialog.setWindowTitle(QCoreApplication.translate("TimeDialog", u"Tiempos de procesos", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tiempos_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TimeDialog", u"ID", None));
        ___qtablewidgetitem1 = self.tiempos_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TimeDialog", u"Operaci\u00f3n", None));
        ___qtablewidgetitem2 = self.tiempos_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TimeDialog", u"Resultado", None));
        ___qtablewidgetitem3 = self.tiempos_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TimeDialog", u"TME", None));
        ___qtablewidgetitem4 = self.tiempos_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TimeDialog", u"TT", None));
        ___qtablewidgetitem5 = self.tiempos_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TimeDialog", u"Estado", None));
        ___qtablewidgetitem6 = self.tiempos_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TimeDialog", u"TLL", None));
        ___qtablewidgetitem7 = self.tiempos_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TimeDialog", u"TF", None));
        ___qtablewidgetitem8 = self.tiempos_tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("TimeDialog", u"TRET", None));
        ___qtablewidgetitem9 = self.tiempos_tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("TimeDialog", u"TRES", None));
        ___qtablewidgetitem10 = self.tiempos_tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("TimeDialog", u"TE", None));
        ___qtablewidgetitem11 = self.tiempos_tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("TimeDialog", u"TS", None));
    # retranslateUi

