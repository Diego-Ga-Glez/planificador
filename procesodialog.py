from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot
from uipy.ui_procesodialog import Ui_ProcesoDialog

class ProcesosDialog(QDialog):
    def __init__(self,parent):
        super(ProcesosDialog, self).__init__(parent)
        self.ui = Ui_ProcesoDialog()
        self.ui.setupUi(self)

        #Slots
        #cambiar nombre
        self.ui.buttonBox.accepted.connect(self.formulario)

    @Slot()
    def formulario(self):
        proceso_aux = []
        proceso_aux.append(self.ui.nombre_lineEdit.text())
        proceso_aux.append(self.ui.operacion_comboBox.currentText())
        proceso_aux.append(int(self.ui.num1_lineEdit.text()))
        proceso_aux.append(int(self.ui.num2_lineEdit.text()))
        proceso_aux.append(self.ui.tiempo_spinBox.value())
        proceso_aux.append(self.ui.id_lineEdit.text())

        self.parent().procesos.append(proceso_aux)