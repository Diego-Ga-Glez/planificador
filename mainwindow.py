from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtCore import Slot
from  uipy.ui_mainwindow import Ui_MainWindow
from numdialog import NumDialog
from procesodialog import ProcesosDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # variables
        self.procesos = []
        self.num = 0

        # interfaces graficas
        self.num_w = NumDialog(self)
        self.proceso_w = ProcesosDialog(self)

        #slots
        self.ui.procesos_pushButton.clicked.connect(self.mostrar_num_window)
    
    @Slot()
    def mostrar_num_window(self):
        self.num_w.show()
        self.num_w.exec()

        for i in range(self.num):
            self.proceso_w.ui.num_proceso_label.setText(str('PROCESO #' + str(i+1)))
            self.proceso_w.show()
            self.proceso_w.exec()

    
    def actualizar_tabla_pendientes(self):
        self.ui.pendientes_tableWidget.setColumnCount(2)
        self.ui.pendientes_tableWidget.setRowCount(len(self.procesos))
        row = 0

        for i in self.procesos:
            id_widget = QTableWidgetItem(i[5])
            op_widget = QTableWidgetItem(i[1])
            self.ui.pendientes_tableWidget.setItem(row,0,id_widget)
            self.ui.pendientes_tableWidget.setItem(row,1,op_widget)
            row+=1