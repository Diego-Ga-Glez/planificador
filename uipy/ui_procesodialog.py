# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'procesodialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_ProcesoDialog(object):
    def setupUi(self, ProcesoDialog):
        if not ProcesoDialog.objectName():
            ProcesoDialog.setObjectName(u"ProcesoDialog")
        ProcesoDialog.resize(558, 572)
        self.verticalLayout = QVBoxLayout(ProcesoDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.num_proceso_label = QLabel(ProcesoDialog)
        self.num_proceso_label.setObjectName(u"num_proceso_label")
        self.num_proceso_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.num_proceso_label)

        self.nombre_groupBox = QGroupBox(ProcesoDialog)
        self.nombre_groupBox.setObjectName(u"nombre_groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.nombre_groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.nombre_label = QLabel(self.nombre_groupBox)
        self.nombre_label.setObjectName(u"nombre_label")

        self.verticalLayout_3.addWidget(self.nombre_label)

        self.nombre_lineEdit = QLineEdit(self.nombre_groupBox)
        self.nombre_lineEdit.setObjectName(u"nombre_lineEdit")

        self.verticalLayout_3.addWidget(self.nombre_lineEdit)


        self.verticalLayout.addWidget(self.nombre_groupBox)

        self.operacion_groupBox = QGroupBox(ProcesoDialog)
        self.operacion_groupBox.setObjectName(u"operacion_groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.operacion_groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.operacion_label = QLabel(self.operacion_groupBox)
        self.operacion_label.setObjectName(u"operacion_label")

        self.verticalLayout_4.addWidget(self.operacion_label)

        self.operacion_comboBox = QComboBox(self.operacion_groupBox)
        self.operacion_comboBox.addItem("")
        self.operacion_comboBox.addItem("")
        self.operacion_comboBox.addItem("")
        self.operacion_comboBox.addItem("")
        self.operacion_comboBox.setObjectName(u"operacion_comboBox")

        self.verticalLayout_4.addWidget(self.operacion_comboBox)


        self.verticalLayout.addWidget(self.operacion_groupBox)

        self.numeros_groupBox = QGroupBox(ProcesoDialog)
        self.numeros_groupBox.setObjectName(u"numeros_groupBox")
        self.verticalLayout_6 = QVBoxLayout(self.numeros_groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.num1_label = QLabel(self.numeros_groupBox)
        self.num1_label.setObjectName(u"num1_label")

        self.verticalLayout_6.addWidget(self.num1_label)

        self.num1_lineEdit = QLineEdit(self.numeros_groupBox)
        self.num1_lineEdit.setObjectName(u"num1_lineEdit")

        self.verticalLayout_6.addWidget(self.num1_lineEdit)

        self.num2_label = QLabel(self.numeros_groupBox)
        self.num2_label.setObjectName(u"num2_label")

        self.verticalLayout_6.addWidget(self.num2_label)

        self.num2_lineEdit = QLineEdit(self.numeros_groupBox)
        self.num2_lineEdit.setObjectName(u"num2_lineEdit")

        self.verticalLayout_6.addWidget(self.num2_lineEdit)


        self.verticalLayout.addWidget(self.numeros_groupBox)

        self.tiempo_groupBox = QGroupBox(ProcesoDialog)
        self.tiempo_groupBox.setObjectName(u"tiempo_groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.tiempo_groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tiempo_label = QLabel(self.tiempo_groupBox)
        self.tiempo_label.setObjectName(u"tiempo_label")

        self.verticalLayout_5.addWidget(self.tiempo_label)

        self.tiempo_spinBox = QSpinBox(self.tiempo_groupBox)
        self.tiempo_spinBox.setObjectName(u"tiempo_spinBox")

        self.verticalLayout_5.addWidget(self.tiempo_spinBox)


        self.verticalLayout.addWidget(self.tiempo_groupBox)

        self.id_groupBox = QGroupBox(ProcesoDialog)
        self.id_groupBox.setObjectName(u"id_groupBox")
        self.verticalLayout_7 = QVBoxLayout(self.id_groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.id_label = QLabel(self.id_groupBox)
        self.id_label.setObjectName(u"id_label")

        self.verticalLayout_7.addWidget(self.id_label)

        self.id_lineEdit = QLineEdit(self.id_groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        self.id_lineEdit.setCursorPosition(0)

        self.verticalLayout_7.addWidget(self.id_lineEdit)


        self.verticalLayout.addWidget(self.id_groupBox)

        self.error_label = QLabel(ProcesoDialog)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.error_label)

        self.aceptar_pushButton = QPushButton(ProcesoDialog)
        self.aceptar_pushButton.setObjectName(u"aceptar_pushButton")

        self.verticalLayout.addWidget(self.aceptar_pushButton)


        self.retranslateUi(ProcesoDialog)

        QMetaObject.connectSlotsByName(ProcesoDialog)
    # setupUi

    def retranslateUi(self, ProcesoDialog):
        ProcesoDialog.setWindowTitle(QCoreApplication.translate("ProcesoDialog", u"Procesos", None))
        self.num_proceso_label.setText(QCoreApplication.translate("ProcesoDialog", u"PROCESO ", None))
        self.nombre_groupBox.setTitle("")
        self.nombre_label.setText(QCoreApplication.translate("ProcesoDialog", u"Nombre:", None))
        self.operacion_groupBox.setTitle("")
        self.operacion_label.setText(QCoreApplication.translate("ProcesoDialog", u"Operaci\u00f3n", None))
        self.operacion_comboBox.setItemText(0, QCoreApplication.translate("ProcesoDialog", u"Suma", None))
        self.operacion_comboBox.setItemText(1, QCoreApplication.translate("ProcesoDialog", u"Resta", None))
        self.operacion_comboBox.setItemText(2, QCoreApplication.translate("ProcesoDialog", u"Multiplicacion", None))
        self.operacion_comboBox.setItemText(3, QCoreApplication.translate("ProcesoDialog", u"Division", None))

        self.numeros_groupBox.setTitle("")
        self.num1_label.setText(QCoreApplication.translate("ProcesoDialog", u"Numero 1", None))
        self.num2_label.setText(QCoreApplication.translate("ProcesoDialog", u"Numero 2", None))
        self.tiempo_groupBox.setTitle("")
        self.tiempo_label.setText(QCoreApplication.translate("ProcesoDialog", u"Tiempo maximo", None))
        self.id_groupBox.setTitle("")
        self.id_label.setText(QCoreApplication.translate("ProcesoDialog", u"ID:", None))
        self.error_label.setText("")
        self.aceptar_pushButton.setText(QCoreApplication.translate("ProcesoDialog", u"Aceptar", None))
    # retranslateUi

