from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot
from uipy.ui_numdialog import Ui_NumDialog
from random import choice, randint

class NumDialog(QDialog):
    def __init__(self,parent):
        super(NumDialog, self).__init__(parent)
        self.ui = Ui_NumDialog()
        self.ui.setupUi(self)

        self.id = 0
        self.quantum = 0

        # definir min y max en spinbox
        self.ui.numero_spinBox.setMinimum(1)
        self.ui.numero_spinBox.setMaximum(99)

        #Slots
        self.ui.num_aceptar_buttonBox.accepted.connect(lambda: self.num_window(valor=True))

    @Slot()
    def num_window(self,valor):
        if valor:
            num = self.ui.numero_spinBox.value()
            self.quantum = self.ui.quantum_spinBox.value()
        else:
            num = 1

        operaciones = ['Suma','Resta', 'Multiplicacion', 'Division', 'Residuo']

        for _ in range(num):
            op = choice(operaciones)
            num1 = randint(0, 99)

            if op == 'Division' or op == 'Residuo':
                num2 = randint(1, 99)
            else:
                num2 = randint(0, 99)

            tiempo = randint(5, 16)
            self.id +=1

            # id, op, num1, num2, TM, TT, estado, TB, TLL, TF, TR
            self.parent().procesos.append([self.id,op,num1,num2,tiempo,tiempo,self.parent().estado,1,0,0,-1])

        if not valor:
            self.parent().tabla_pendientes(1,0)