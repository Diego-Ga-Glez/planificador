from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot
from uipy.ui_numdialog import Ui_NumDialog

class NumDialog(QDialog):
    def __init__(self,parent):
        super(NumDialog, self).__init__(parent)
        self.ui = Ui_NumDialog()
        self.ui.setupUi(self)

        #Slots
        self.ui.num_aceptar_buttonBox.accepted.connect(self.num_window)

    @Slot()
    def num_window(self):
        self.parent().num = self.ui.numero_spinBox.value()