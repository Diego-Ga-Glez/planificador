from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import QValidator
from uipy.ui_procesodialog import Ui_ProcesoDialog
import re

# Comprueba si solo hay numeros en un line edit
class Numeros(QValidator):
    def validate(self, string,index):
        patron = re.compile("[0-9]+")

        if string == "":
            return QValidator.State.Acceptable, string, index

        if patron.fullmatch(string):
            return QValidator.State.Acceptable, string, index
        else:
            return QValidator.State.Invalid, string, index

class NumerosE(QValidator):
     def validate(self, string,index):
        str_patron = r"[-]?[0-9]+"
        patron = re.compile(str_patron)

        if string == "":
            return QValidator.State.Acceptable, string, index

        if string == "-":
            return QValidator.State.Acceptable, string, index

        if patron.fullmatch(string):
            return QValidator.State.Acceptable, string, index
        else:
            return QValidator.State.Invalid, string, index

class Letras(QValidator):
    def validate(self, string,index):
        patron = re.compile("[A-Za-z ]+")

        if string == "":
            return QValidator.State.Acceptable, string, index

        if patron.fullmatch(string):
            return QValidator.State.Acceptable, string, index
        else:
            return QValidator.State.Invalid, string, index

class ProcesosDialog(QDialog):
    def __init__(self,parent):
        super(ProcesosDialog, self).__init__(parent)
        self.ui = Ui_ProcesoDialog()
        self.ui.setupUi(self)

        self.ui.aceptar_pushButton.setEnabled(False)
        
        #Slots
        self.ui.aceptar_pushButton.clicked.connect(self.formulario)
        self.ui.nombre_lineEdit.textEdited.connect(self.validar_vacio)
        self.ui.num1_lineEdit.textEdited.connect(self.validar_vacio)
        self.ui.num2_lineEdit.textEdited.connect(self.validar_vacio)
        self.ui.tiempo_spinBox.valueChanged.connect(self.validar_vacio)
        self.ui.id_lineEdit.textEdited.connect(self.validar_vacio)

        self.ui.id_lineEdit.editingFinished.connect(self.validar_id)

        # validar datos
        self.ui.nombre_lineEdit.setValidator(Letras())
        self.ui.num1_lineEdit.setValidator(NumerosE())
        self.ui.num2_lineEdit.setValidator(NumerosE())
        self.ui.id_lineEdit.setValidator(Numeros())

    @Slot()
    def formulario(self):
        nombre = self.ui.nombre_lineEdit.text()
        op = self.ui.operacion_comboBox.currentText()
        num1 = int(self.ui.num1_lineEdit.text())
        num2 = int(self.ui.num2_lineEdit.text())
        tiempo = self.ui.tiempo_spinBox.value()
        id_f = self.ui.id_lineEdit.text()
        self.parent().procesos.append([nombre,op,num1,num2,tiempo,id_f])

        # limpiar formulario
        self.ui.nombre_lineEdit.setText("")
        self.ui.num1_lineEdit.setText("")
        self.ui.num2_lineEdit.setText("")
        self.ui.tiempo_spinBox.setValue(0)
        self.ui.id_lineEdit.setText("")

        # cerrar qdialog
        self.close()

    @Slot()
    def validar_vacio(self):
        nombre = self.ui.nombre_lineEdit.text()
        op = self.ui.operacion_comboBox.currentText()
        num1 = self.ui.num1_lineEdit.text()
        num2 = self.ui.num2_lineEdit.text()
        tiempo = self.ui.tiempo_spinBox.value()
        id_f = self.ui.id_lineEdit.text()


        if nombre.isspace():
            self.ui.aceptar_pushButton.setEnabled(False)
        elif nombre == "" or num1 == "" or num2 == "" or tiempo == 0 or id_f == "":
            self.ui.aceptar_pushButton.setEnabled(False)
        else:
            self.ui.aceptar_pushButton.setEnabled(True)

    @Slot()
    def validar_id(self):
        id_f = self.ui.id_lineEdit.text()
        
        for i in range(len(self.parent().procesos)):
            if self.parent().procesos[i][5] == id_f:
                self.ui.error_label.setText("ID repetido")
                self.ui.aceptar_pushButton.setEnabled(False)
                return
        
        for i in range(len(self.parent().terminados)):
            if self.parent().terminados[i][5] == id_f:
                self.ui.error_label.setText("ID repetido")
                self.ui.aceptar_pushButton.setEnabled(False)
                return

        self.ui.error_label.setText("")