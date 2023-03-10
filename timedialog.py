from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from uipy.ui_timedialog import Ui_TimeDialog
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

class TimeDialog(QDialog):
    def __init__(self,parent):
        super(TimeDialog, self).__init__(parent)
        self.ui = Ui_TimeDialog()
        self.ui.setupUi(self)

        self.row = 0
        
        self.ui.tiempos_tableWidget.verticalScrollBar().setEnabled(True)

        #Tamaño de columnas
        tiempos = self.ui.tiempos_tableWidget.horizontalHeader()
        tiempos.setSectionResizeMode(QHeaderView.Stretch)

    def keyPressEvent(self, event: QKeyEvent):
        # focus en la ventana timedialog
        if event.key() == Qt.Key_C:
            self.close()
        return super().keyPressEvent(event)

    def tabla_tiempos(self):
        self.row = 0
        self.ui.tiempos_tableWidget.setColumnCount(13)
        rowCount = len(self.parent().terminados + self.parent().lote + self.parent().bloqueados + self.parent().procesos)
        self.ui.tiempos_tableWidget.setRowCount(rowCount)
        self.imprimir_tablas(self.parent().terminados)
        if len(self.parent().lote) > 0:
            self.imprimir_tablas([self.parent().lote[0],])
        self.imprimir_tablas(self.parent().lote[1:])
        self.imprimir_tablas(self.parent().bloqueados)
        self.imprimir_tablas(self.parent().procesos)


    def imprimir_tablas(self, lista):
         # id, op, num1, num2, TM, TT, estado, TB, TLL, TF, TR
        for i in lista:
            id_widget = QTableWidgetItem(str(i[0]))

            if lista == self.parent().terminados:
                estado_widget = QTableWidgetItem('Terminado')
            elif len(self.parent().lote) > 0 and lista == [self.parent().lote[0],]:
                estado_widget = QTableWidgetItem('Ejecucion')
            elif lista == self.parent().lote[1:]:
                estado_widget = QTableWidgetItem('Listo')
            elif lista == self.parent().bloqueados:
                estado_widget = QTableWidgetItem('Bloqueado')
            elif lista == self.parent().procesos:
                estado_widget = QTableWidgetItem('Nuevo')

            operacion = self.parent().concatenar_op(i[1], i[2], i[3])
            op_widget = QTableWidgetItem(operacion)

            if lista == self.parent().terminados:
                if i[6] == True:
                    resultado = self.parent().resultado_op(i[1], i[2], i[3])
                else:
                    resultado = 'ERROR'
            else:
                resultado = 'null'
            
            if lista != self.parent().procesos: 
                t_transcurrido = i[4] - i[5]
            else:
                t_transcurrido = 'null'

            if lista == self.parent().terminados:
                t_retorno = i[9] - i[8]
            else:
                t_retorno = 'null'

            res_widget = QTableWidgetItem(resultado)
            tme_widget = QTableWidgetItem(str(i[4]))
            tt_widget =  QTableWidgetItem(str(t_transcurrido))

            if lista != self.parent().procesos:
                tll_widget = QTableWidgetItem(str(i[8]))
            else:
                tll_widget = QTableWidgetItem('null')

            if lista == self.parent().terminados:
                tf_widget = QTableWidgetItem(str(i[9]))
            else:
                tf_widget = QTableWidgetItem('null')

            tret_widget = QTableWidgetItem(str(t_retorno))

            if i[10] != -1:
                tres_widget = QTableWidgetItem(str(i[10] - i[8]))
            else:
                tres_widget = QTableWidgetItem('null')

            if lista == self.parent().terminados:
                te_widget = QTableWidgetItem(str(t_retorno - t_transcurrido))
            else:
                if lista != self.parent().procesos: #Actual - tll - tt 
                    te_momentaneo = self.parent().contador - i[8] - t_transcurrido
                    te_widget = QTableWidgetItem(str(te_momentaneo))
                else:
                    te_widget = QTableWidgetItem('null')

            if lista != self.parent().procesos:
                ts_widget = QTableWidgetItem(str(t_transcurrido))
            else:
                ts_widget = QTableWidgetItem('null')
            
            if lista == self.parent().bloqueados:
                tb_widget = QTableWidgetItem(str(i[7] - 1))
            else:
                tb_widget = QTableWidgetItem('null')

            self.ui.tiempos_tableWidget.setItem(self.row,0,id_widget)
            self.ui.tiempos_tableWidget.setItem(self.row,1,estado_widget)
            self.ui.tiempos_tableWidget.setItem(self.row,2,op_widget)
            self.ui.tiempos_tableWidget.setItem(self.row,3,res_widget)
            self.ui.tiempos_tableWidget.setItem(self.row,4,tme_widget)
            self.ui.tiempos_tableWidget.setItem(self.row,5,tt_widget)
            self.ui.tiempos_tableWidget.setItem(self.row,6,tll_widget)
            self.ui.tiempos_tableWidget.setItem(self.row,7,tf_widget)
            self.ui.tiempos_tableWidget.setItem(self.row,8,tret_widget)
            self.ui.tiempos_tableWidget.setItem(self.row,9,tres_widget)
            self.ui.tiempos_tableWidget.setItem(self.row,10,te_widget)
            self.ui.tiempos_tableWidget.setItem(self.row,11,ts_widget)
            self.ui.tiempos_tableWidget.setItem(self.row,12,tb_widget)
            self.row += 1