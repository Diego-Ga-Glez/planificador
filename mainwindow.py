from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Slot
from PySide6.QtTest import QTest
from copy import deepcopy
from math import floor

from uipy.ui_mainwindow import Ui_MainWindow
from numdialog import NumDialog
from procesodialog import ProcesosDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # variables
        self.procesos = []           # lista de procesos en total
        self.lote = []               # lote actual en ejecucion
        self.num = 0                 # numero de ventanas para abrir
        self.ejecucion = []          # proceso en ejecucion
        self.terminados = []
        self.contador = 0

        # interfaces graficas
        self.num_w = NumDialog(self)
        self.proceso_w = ProcesosDialog(self)

        #slots
        self.ui.procesos_pushButton.clicked.connect(self.mostrar_num_window)

        # arreglar tamaño de columnas
        pendiente = self.ui.pendientes_tableWidget.horizontalHeader()
        pendiente.setSectionResizeMode(0,QHeaderView.Stretch)
        pendiente.setSectionResizeMode(1,QHeaderView.Stretch)

        proceso = self.ui.proceso_tableWidget.horizontalHeader()
        proceso.setSectionResizeMode(0,QHeaderView.Stretch)
        proceso = self.ui.proceso_tableWidget.verticalHeader()
        proceso.setSectionResizeMode(0,QHeaderView.Stretch)
        proceso.setSectionResizeMode(1,QHeaderView.Stretch)
        proceso.setSectionResizeMode(2,QHeaderView.Stretch)
        proceso.setSectionResizeMode(3,QHeaderView.Stretch)
        proceso.setSectionResizeMode(4,QHeaderView.Stretch)
        proceso.setSectionResizeMode(5,QHeaderView.Stretch)
        
        terminados = self.ui.terminados_tableWidget.horizontalHeader()
        terminados.setSectionResizeMode(0,QHeaderView.Stretch)
        terminados.setSectionResizeMode(1,QHeaderView.Stretch)
        terminados.setSectionResizeMode(2,QHeaderView.Stretch)

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
            #self.tabla_pendientes(True)

        # actualizar numero de lotes pendientes
        str_num_proc = str(floor(len(self.procesos)/4))
        self.ui.pendientes_label.setText('Lotes pendientes: '+ str_num_proc)
        ######################################################################
        self.ui.procesos_pushButton.setEnabled(False)
        QTest.qWait(1000)
        self.proceso_ejecucion()   
    
    def tabla_pendientes(self, bandera):
        if len(self.lote) == 0:
            if len(self.procesos) > 4:
                for i in range(4): self.lote.append(self.procesos[i])
            else:
                for i in range(len(self.procesos)): self.lote.append(self.procesos[i])
          
        '''

         Si la bandera es True se imprime toda la tabla
         Si es False se imprime toda excepto el primer 
         elemento

        '''
        
        self.ui.pendientes_tableWidget.setColumnCount(2)
        if bandera:
            self.ui.pendientes_tableWidget.setRowCount(len(self.lote))
        else:
            self.ui.pendientes_tableWidget.setRowCount(len(self.lote)-1)
        row = 0

        for i in self.lote:
            if bandera:
                nombre_widget = QTableWidgetItem(i[0])
                tme_widget = QTableWidgetItem(str(i[4]))
                self.ui.pendientes_tableWidget.setItem(row,0,nombre_widget)
                self.ui.pendientes_tableWidget.setItem(row,1,tme_widget)
                row+=1
            else:
                bandera = True
    
    def proceso_ejecucion(self):
        
        while len(self.procesos) > 0:
            '''
            Las siguientes dos lineas son para poder
            visualizar todos los elementos de otros lotes
            antes de que el primero pase a ser ejecutado
            '''
            self.tabla_pendientes(True)
            QTest.qWait(1000)
            #################################################

            ejecucion = self.procesos[0]
            tiempo = deepcopy(ejecucion[4])
            self.tabla_pendientes(False)

            while ejecucion[4] > 0:
                ejecucion[4] -= 1
                self.contador += 1
                self.tabla_ejecucion(ejecucion, tiempo)
                QTest.qWait(1000)

            self.terminados.append(self.procesos.pop(0))
            self.lote.pop(0)

            # actualizar numero de lotes pendientes
            str_num_proc = str(floor(len(self.procesos)/4))
            self.ui.pendientes_label.setText('Lotes pendientes: '+ str_num_proc)
            ######################################################################

            # limpiar tabla
            self.ui.proceso_tableWidget.removeColumn(0) 
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