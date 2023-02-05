from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtCore import Slot
from PySide6.QtTest import QTest
from copy import deepcopy

from uipy.ui_mainwindow import Ui_MainWindow
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
        self.ejecucion = []
        self.terminados = []
        self.contador = 0

        # interfaces graficas
        self.num_w = NumDialog(self)
        self.proceso_w = ProcesosDialog(self)

        #slots
        self.ui.procesos_pushButton.clicked.connect(self.mostrar_num_window)

    def closeEvent(self, event):
        exit()
    
    @Slot()
    def mostrar_num_window(self):
        self.num_w.show()
        self.num_w.exec()

        for i in range(self.num):
            self.proceso_w.ui.num_proceso_label.setText(str('PROCESO #' + str(i+1)))
            self.proceso_w.show()
            self.proceso_w.exec()
            self.tabla_pendientes()

        self.ui.procesos_pushButton.setEnabled(False)
        #QTimer.singleShot(1000, self.proceso_ejecucion) #1000 milliseconds = 1 second
        QTest.qWait(1000)
        self.proceso_ejecucion()   
    
    def tabla_pendientes(self):

        self.ui.pendientes_tableWidget.setColumnCount(2)
        self.ui.pendientes_tableWidget.setRowCount(len(self.procesos))
        row = 0

        for i in self.procesos:
            nombre_widget = QTableWidgetItem(i[0])
            tme_widget = QTableWidgetItem(str(i[4]))
            self.ui.pendientes_tableWidget.setItem(row,0,nombre_widget)
            self.ui.pendientes_tableWidget.setItem(row,1,tme_widget)
            row+=1
    
    def proceso_ejecucion(self):
        aux = 0
        while len(self.procesos) > 0:
            aux+=1
            ejecucion = self.procesos[0]
            tiempo = deepcopy(ejecucion[4])
            while ejecucion[4] > 0:
                ejecucion[4] -= 1
                self.contador += 1
                QTest.qWait(1000)
                self.tabla_ejecucion(ejecucion, tiempo)

            self.terminados.append(self.procesos.pop(0))
            self.tabla_pendientes()
            self.tabla_terminados()

        self.ui.procesos_pushButton.setEnabled(True)
        
    def tabla_ejecucion(self, ejecucion, tiempo):
            self.ui.proceso_tableWidget.setColumnCount(1)
            self.ui.proceso_tableWidget.setRowCount(6)

            id_widget = QTableWidgetItem(ejecucion[5])
            nombre_widget = QTableWidgetItem(ejecucion[0])

            operacion = self.concatenar_op(ejecucion[1], ejecucion[2], ejecucion[3])

            op_widget = QTableWidgetItem(operacion)
            tme_widget = QTableWidgetItem(str(tiempo))
            transcurrido_widget = QTableWidgetItem(str(tiempo-ejecucion[4]))
            restante_widget = QTableWidgetItem(str(ejecucion[4]))

            self.ui.proceso_tableWidget.setItem(0,0,id_widget)
            self.ui.proceso_tableWidget.setItem(1,0,nombre_widget)
            self.ui.proceso_tableWidget.setItem(2,0,op_widget)
            self.ui.proceso_tableWidget.setItem(3,0,tme_widget)
            self.ui.proceso_tableWidget.setItem(4,0,transcurrido_widget)
            self.ui.proceso_tableWidget.setItem(5,0,restante_widget)

            self.ui.contador_label.setText('Contador general: ' + str(self.contador))


    def tabla_terminados(self):
        self.ui.terminados_tableWidget.setColumnCount(3)
        self.ui.terminados_tableWidget.setRowCount(len(self.terminados))
        row = 0

        for i in self.terminados:
            id_widget = QTableWidgetItem(i[5])

            operacion = self.concatenar_op(i[1], i[2], i[3])
            op_widget = QTableWidgetItem(operacion)

            resultado = self.resultado_op(i[1], i[2], i[3])
            res_widget = QTableWidgetItem(resultado)

            self.ui.terminados_tableWidget.setItem(row,0,id_widget)
            self.ui.terminados_tableWidget.setItem(row,1,op_widget)
            self.ui.terminados_tableWidget.setItem(row,2,res_widget)
            row+=1

    def concatenar_op(self, operador, operando1, operando2):
        if operador == 'Suma':
            op = '+'
        elif operador == 'Resta':
            op = '-'
        elif operador == 'Multiplicacion':
            op = 'x'
        elif operador == 'Division':
            op = '/'
            
        return str(operando1)+ ' ' + op + ' ' + str(operando2)
    
    def resultado_op(self, operador, operando1, operando2):
        if operador == 'Suma':
            resultado = operando1 + operando2
        elif operador == 'Resta':
            resultado = operando1 - operando2
        elif operador == 'Multiplicacion':
            resultado = operando1 * operando2
        elif operador == 'Division':
            resultado = operando1 / operando2
        
        return str(resultado)