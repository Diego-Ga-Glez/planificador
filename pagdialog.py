from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from uipy.ui_pagdialog import Ui_PagDialog
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

class PagDialog(QDialog):
    def __init__(self,parent):
        super(PagDialog, self).__init__(parent)
        self.ui = Ui_PagDialog()
        self.ui.setupUi(self)

        #Tamaño de columnas
        memoria1H = self.ui.memoria1_tableWidget.horizontalHeader()
        memoria1H.setSectionResizeMode(QHeaderView.Stretch)
        memoria2H = self.ui.memoria2_tableWidget.horizontalHeader()
        memoria2H.setSectionResizeMode(QHeaderView.Stretch)
        memoria1V = self.ui.memoria1_tableWidget.verticalHeader()
        memoria1V.setSectionResizeMode(QHeaderView.Stretch)
        memoria2V = self.ui.memoria2_tableWidget.verticalHeader()
        memoria2V.setSectionResizeMode(QHeaderView.Stretch)

    def keyPressEvent(self, event: QKeyEvent):
        # focus en la ventana pagdialog
        if event.key() == Qt.Key_C:
            self.close()
        return super().keyPressEvent(event)
    
    def tabla_paginas(self, num_tabla):
        if num_tabla == 1:
            tabla = self.ui.memoria1_tableWidget
        else:
            tabla = self.ui.memoria2_tableWidget

        tabla.setColumnCount(4)
        tabla.setRowCount(20)
        row = 0

        for i in range(int(self.parent().num_marcos/2)):
            if tabla == self.ui.memoria1_tableWidget:
                indice = i
            else:
                indice = int(i + self.parent().num_marcos/2)
                
            marco_widget = QTableWidgetItem(str(indice + 1))
            proceso_widget = QTableWidgetItem(str(self.parent().marcos[indice][1]))
            pagina_widget = QTableWidgetItem(str(self.parent().marcos[indice][2]))
            progressbar = self.parent().barra_progreso(indice, 'pagdialog')

            tabla.setItem(row,0,marco_widget)
            tabla.setCellWidget(row,1,progressbar)
            tabla.setItem(row,2,proceso_widget)
            tabla.setItem(row,3,pagina_widget)
            row += 1