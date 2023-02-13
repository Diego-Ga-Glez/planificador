from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Slot, Qt
from PySide6.QtTest import QTest
from PySide6.QtGui import QKeyEvent

from copy import deepcopy
from math import floor, ceil
from random import choice, randint

from uipy.ui_mainwindow import Ui_MainWindow
from numdialog import NumDialog


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
        self.pausa = False
        self.estado = True

        # interfaces graficas
        self.num_w = NumDialog(self)

        #slots
        self.ui.procesos_pushButton.clicked.connect(self.mostrar_num_window)

        # tamaño de columnas
        pendiente = self.ui.pendientes_tableWidget.horizontalHeader()
        pendiente.setSectionResizeMode(QHeaderView.Stretch)

        proceso = self.ui.proceso_tableWidget.horizontalHeader()
        proceso.setSectionResizeMode(QHeaderView.Stretch)
        proceso = self.ui.proceso_tableWidget.verticalHeader()
        proceso.setSectionResizeMode(QHeaderView.Stretch)
        
        terminados = self.ui.terminados_tableWidget.horizontalHeader()
        terminados.setSectionResizeMode(QHeaderView.Stretch)
        

    def closeEvent(self, event):
        exit()
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_I:
            print('I')

        elif event.key() == Qt.Key_E:
            self.estado = False

        elif event.key() == Qt.Key_P:
            self.pausa = True
            
        elif event.key() == Qt.Key_C:
            self.pausa = False
        
        return super().keyPressEvent(event)
    
    @Slot()
    def mostrar_num_window(self):
        self.num_w.show()
        self.num_w.exec()

        operaciones = ['Suma','Resta', 'Multiplicacion', 'Division', 'Residuo']

        for i in range(self.num):
            op = choice(operaciones)
            num1 = randint(0, 99)

            if op == 'Division' or op == 'Residuo':
                num2 = randint(1, 99)
            else:
                num2 = randint(0, 99)

            tiempo = randint(5, 16)
            id = i + 1

            self.procesos.append([id,op,num1,num2,tiempo,tiempo,self.estado])

        self.ui.procesos_pushButton.setEnabled(False)
        QTest.qWait(1000)
        self.proceso_ejecucion()   
    
    # actualizar numero de lotes pendientes
    def actualizar_lotes_pendientes(self):
        num_proc = floor(len(self.procesos)/4)
        if len(self.procesos) % 4 != 0:
            self.ui.pendientes_label.setText('Lotes pendientes: '+ str(num_proc))
        else:
            self.ui.pendientes_label.setText('Lotes pendientes: '+ str(num_proc - 1))
    
    def tabla_pendientes(self, bandera):
        if len(self.lote) == 0:
            if len(self.procesos) > 4:
                for i in range(4): self.lote.append(self.procesos[i])
                self.actualizar_lotes_pendientes()
            else:
                for i in range(len(self.procesos)): self.lote.append(self.procesos[i])
                self.ui.pendientes_label.setText('Lotes pendientes: 0')
          
        '''

         Si la bandera es True se imprime toda la tabla
         Si es False se imprime toda excepto el primer 
         elemento

        '''

        self.ui.pendientes_tableWidget.setColumnCount(3)
        if bandera:
            self.ui.pendientes_tableWidget.setRowCount(len(self.lote))
        else:
            self.ui.pendientes_tableWidget.setRowCount(len(self.lote)-1)
        row = 0

        for i in self.lote:
            if bandera:
                id_widget = QTableWidgetItem(str(i[0]))
                tme_widget = QTableWidgetItem(str(i[4]))
                self.ui.pendientes_tableWidget.setItem(row,0,id_widget)
                self.ui.pendientes_tableWidget.setItem(row,1,tme_widget)
                row+=1
            else:
                bandera = True
    
    def proceso_ejecucion(self):
        while len(self.procesos) > 0:
            self.estado = True
            '''
            Las siguientes dos lineas son para poder
            visualizar todos los elementos de otros procesos
            antes de que el primero pase a ser ejecutado
            '''
            self.tabla_pendientes(True)
            QTest.qWait(1000)
            #################################################

            ejecucion = self.procesos[0]
            tiempo = ejecucion[5]
            self.tabla_pendientes(False)

            while tiempo > 0 and self.estado == True:
                if self.pausa == False:
                    tiempo -= 1
                    self.contador += 1
                self.tabla_ejecucion(ejecucion, tiempo)
                QTest.qWait(1000)

            self.procesos[0][6] = self.estado
            self.terminados.append(self.procesos.pop(0))
            self.lote.pop(0)

            # limpiar tabla
            self.ui.proceso_tableWidget.clearContents()
            self.tabla_terminados()
        
    def tabla_ejecucion(self, ejecucion, tiempo):
            self.ui.proceso_tableWidget.setColumnCount(1)
            self.ui.proceso_tableWidget.setRowCount(5)

            id_widget = QTableWidgetItem(str(ejecucion[0]))

            operacion = self.concatenar_op(ejecucion[1], ejecucion[2], ejecucion[3])

            op_widget = QTableWidgetItem(operacion)
            tme_widget = QTableWidgetItem(str(ejecucion[4]))
            transcurrido_widget = QTableWidgetItem(str(ejecucion[4]-tiempo))
            restante_widget = QTableWidgetItem(str(tiempo))

            self.ui.proceso_tableWidget.setItem(0,0,id_widget)
            self.ui.proceso_tableWidget.setItem(1,0,op_widget)
            self.ui.proceso_tableWidget.setItem(2,0,tme_widget)
            self.ui.proceso_tableWidget.setItem(3,0,transcurrido_widget)
            self.ui.proceso_tableWidget.setItem(4,0,restante_widget)

            self.ui.contador_label.setText('Contador general: ' + str(self.contador))


    def tabla_terminados(self):
        self.ui.terminados_tableWidget.setColumnCount(4)
        self.ui.terminados_tableWidget.setRowCount(len(self.terminados))
        row = 0

        for i in self.terminados:
            id_widget = QTableWidgetItem(str(i[0]))

            operacion = self.concatenar_op(i[1], i[2], i[3])
            op_widget = QTableWidgetItem(operacion)

            if i[6] == True:
                resultado = self.resultado_op(i[1], i[2], i[3])
            else:
                resultado = 'ERROR'

            res_widget = QTableWidgetItem(resultado)

            indice = self.terminados.index(i) + 1
            lote = str(ceil(indice / 4))
            lote_widget = QTableWidgetItem(lote)
            
            self.ui.terminados_tableWidget.setItem(row,0,lote_widget)
            self.ui.terminados_tableWidget.setItem(row,1,id_widget)
            self.ui.terminados_tableWidget.setItem(row,2,op_widget)
            self.ui.terminados_tableWidget.setItem(row,3,res_widget)
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
        elif operador == 'Residuo':
            op = '%'
            
        return str(operando1)+ ' ' + op + ' ' + str(operando2)
    
    def resultado_op(self, operador, operando1, operando2):
        if operador == 'Suma':
            resultado = operando1 + operando2
        elif operador == 'Resta':
            resultado = operando1 - operando2
        elif operador == 'Multiplicacion':
            resultado = operando1 * operando2
        elif operador == 'Division':
            resultado = round(operando1 / operando2, 2)
        elif operador == 'Residuo':
            resultado = operando1 % operando2
        
        return str(resultado)