from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from uipy.ui_timedialog import Ui_TimeDialog

class TimeDialog(QDialog):
    def __init__(self,parent):
        super(TimeDialog, self).__init__(parent)
        self.ui = Ui_TimeDialog()
        self.ui.setupUi(self)

        #Tamaño de columnas
        tiempos = self.ui.tiempos_tableWidget.horizontalHeader()
        tiempos.setSectionResizeMode(QHeaderView.Stretch)

    def tabla_tiempos(self):
        self.ui.tiempos_tableWidget.setColumnCount(12)
        self.ui.tiempos_tableWidget.setRowCount(len(self.parent().terminados))
        row = 0

         # id, op, num1, num2, TM, TT, estado, TB, TLL, TF, TR
        for i in self.parent().terminados:
            id_widget = QTableWidgetItem(str(i[0]))
            operacion = self.parent().concatenar_op(i[1], i[2], i[3])
            op_widget = QTableWidgetItem(operacion)

            if i[6] == True:
                resultado = self.parent().resultado_op(i[1], i[2], i[3])
            else:
                resultado = 'ERROR'
            
            t_transcurrido = i[4] - i[5]
            t_retorno = i[9] - i[8]

            res_widget = QTableWidgetItem(resultado)
            tme_widget = QTableWidgetItem(str(i[4]))
            tt_widget =  QTableWidgetItem(str(t_transcurrido))
            estado_widget = QTableWidgetItem('Terminado')
            tll_widget = QTableWidgetItem(str(i[8]))
            tf_widget = QTableWidgetItem(str(i[9]))
            tret_widget = QTableWidgetItem(str(t_retorno))
            tres_widget = QTableWidgetItem(str(i[10] - i[8]))
            te_widget = QTableWidgetItem(str(t_retorno - t_transcurrido))
            ts_widget = QTableWidgetItem(str(t_transcurrido))

            self.ui.tiempos_tableWidget.setItem(row,0,id_widget)
            self.ui.tiempos_tableWidget.setItem(row,1,op_widget)
            self.ui.tiempos_tableWidget.setItem(row,2,res_widget)
            self.ui.tiempos_tableWidget.setItem(row,3,tme_widget)
            self.ui.tiempos_tableWidget.setItem(row,4,tt_widget)
            self.ui.tiempos_tableWidget.setItem(row,5,estado_widget)
            self.ui.tiempos_tableWidget.setItem(row,6,tll_widget)
            self.ui.tiempos_tableWidget.setItem(row,7,tf_widget)
            self.ui.tiempos_tableWidget.setItem(row,8,tret_widget)
            self.ui.tiempos_tableWidget.setItem(row,9,tres_widget)
            self.ui.tiempos_tableWidget.setItem(row,10,te_widget)
            self.ui.tiempos_tableWidget.setItem(row,11,ts_widget)
            row+=1
