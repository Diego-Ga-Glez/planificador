# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'numdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QLabel, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_NumDialog(object):
    def setupUi(self, NumDialog):
        if not NumDialog.objectName():
            NumDialog.setObjectName(u"NumDialog")
        NumDialog.resize(195, 185)
        self.verticalLayout = QVBoxLayout(NumDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.numero_groupBox = QGroupBox(NumDialog)
        self.numero_groupBox.setObjectName(u"numero_groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.numero_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numero_label = QLabel(self.numero_groupBox)
        self.numero_label.setObjectName(u"numero_label")
        self.numero_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.numero_label)

        self.numero_spinBox = QSpinBox(self.numero_groupBox)
        self.numero_spinBox.setObjectName(u"numero_spinBox")

        self.verticalLayout_2.addWidget(self.numero_spinBox)


        self.verticalLayout.addWidget(self.numero_groupBox)

        self.num_aceptar_buttonBox = QDialogButtonBox(NumDialog)
        self.num_aceptar_buttonBox.setObjectName(u"num_aceptar_buttonBox")
        self.num_aceptar_buttonBox.setOrientation(Qt.Horizontal)
        self.num_aceptar_buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.num_aceptar_buttonBox)


        self.retranslateUi(NumDialog)
        self.num_aceptar_buttonBox.accepted.connect(NumDialog.accept)
        self.num_aceptar_buttonBox.rejected.connect(NumDialog.reject)

        QMetaObject.connectSlotsByName(NumDialog)
    # setupUi

    def retranslateUi(self, NumDialog):
        NumDialog.setWindowTitle(QCoreApplication.translate("NumDialog", u"Dialog", None))
        self.numero_groupBox.setTitle("")
        self.numero_label.setText(QCoreApplication.translate("NumDialog", u"N\u00famero de procesos", None))
    # retranslateUi

