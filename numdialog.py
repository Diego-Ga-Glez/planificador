from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot
from uipy.ui_numdialog import Ui_NumDialog
from random import choice, randint

class NumDialog(QDialog):
    def __init__(self,parent):
        super(NumDialog, self).__init__(parent)
        self.ui = Ui_NumDialog()
        self.ui.setupUi(self)

        #Slots
        self.ui.num_aceptar_buttonBox.accepted.connect(self.num_window)

    @Slot()
    def num_window(self):
        num = self.ui.numero_spinBox.value()

        operaciones = ['Suma','Resta', 'Multiplicacion', 'Division', 'Residuo']

        for i in range(num):
            op = choice(operaciones)
            num1 = randint(0, 99)

            if op == 'Division' or op == 'Residuo':
                num2 = randint(1, 99)
            else:
                num2 = randint(0, 99)

            tiempo = randint(5, 16)
            id = i + 1

            self.parent().procesos.append([id,op,num1,num2,tiempo,tiempo,self.parent().estado])