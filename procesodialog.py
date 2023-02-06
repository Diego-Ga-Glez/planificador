from PySide6.QtWidgets import QDialog,QMessageBox
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

        # pop up
        self.msg_box = QMessageBox()
        self.msg_box.setIcon(QMessageBox.Warning)
        self.msg_box.setWindowTitle('Warning')
        
        self.ui.aceptar_pushButton.setEnabled(False)
        
        #Slots
        self.ui.aceptar_pushButton.clicked.connect(self.formulario)
        self.ui.operacion_comboBox.currentTextChanged.connect(self.validar_vacio_errores)
        self.ui.nombre_lineEdit.textEdited.connect(self.validar_vacio_errores)
        self.ui.num1_lineEdit.textEdited.connect(self.validar_vacio_errores)
        self.ui.num2_lineEdit.textEdited.connect(self.validar_vacio_errores)
        self.ui.tiempo_spinBox.valueChanged.connect(self.validar_vacio_errores)
        self.ui.id_lineEdit.textEdited.connect(self.validar_vacio_errores)

        # validar datos
        self.ui.nombre_lineEdit.setValidator(Letras())
        self.ui.num1_lineEdit.setValidator(NumerosE())
        self.ui.num2_lineEdit.setValidator(NumerosE())
        self.ui.id_lineEdit.setValidator(Numeros())

    # limpiar formulario
    def limpiar(self):
        self.ui.nombre_lineEdit.setText("")
        self.ui.num1_lineEdit.setText("")
        self.ui.num2_lineEdit.setText("")
        self.ui.tiempo_spinBox.setValue(0)
        self.ui.id_lineEdit.setText("")
    
    def closeEvent(self, event):
        self.limpiar()
    
    @Slot()
    def formulario(self):
        nombre = self.ui.nombre_lineEdit.text()
        op = self.ui.operacion_comboBox.currentText()
        num1 = int(self.ui.num1_lineEdit.text())
        num2 = int(self.ui.num2_lineEdit.text())
        tiempo = self.ui.tiempo_spinBox.value()
        id_f = self.ui.id_lineEdit.text()
        self.parent().procesos.append([nombre,op,num1,num2,tiempo,id_f])

        self.limpiar()
        # cerrar qdialog
        self.close()

    @Slot()
    def validar_vacio_errores(self):
        nombre = self.ui.nombre_lineEdit.text()
        op = self.ui.operacion_comboBox.currentText()
        num1 = self.ui.num1_lineEdit.text()
        num2 = self.ui.num2_lineEdit.text()
        tiempo = self.ui.tiempo_spinBox.value()
        id_f = self.ui.id_lineEdit.text()

        # se comprueba que no haya campos vacios
        if nombre == "" or num1 == "" or num2 == "" or tiempo == 0 or id_f == "":
            self.ui.aceptar_pushButton.setEnabled(False)
        # se comprueba que en el nombre no haya puros espacios vacios
        elif nombre.isspace():
            self.ui.aceptar_pushButton.setEnabled(False)
        # se comprueba que en num1 y num2 no este unicamente el signo de menos
        elif num1 == "-" or num2 == "-":
            self.ui.aceptar_pushButton.setEnabled(False)
        # se comprueba si se quiere dividir entre 0
        elif (num2 == "0" or num2 == "-0") and op == "Division":
            self.ui.aceptar_pushButton.setEnabled(False)
        elif self.validar_id():
            self.ui.aceptar_pushButton.setEnabled(False)
        else:
            self.ui.aceptar_pushButton.setEnabled(True)

    def validar_id(self):
        id_f = self.ui.id_lineEdit.text()
        
        for i in range(len(self.parent().procesos)):
            if self.parent().procesos[i][5] == id_f:
                self.msg_box.setText("ID repetido")
                self.msg_box.exec()
                return True
        
        for i in range(len(self.parent().terminados)):
            if self.parent().terminados[i][5] == id_f:
                self.msg_box.setText("ID repetido")
                self.msg_box.exec()
                return True
        return False