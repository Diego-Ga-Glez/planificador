from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Slot, Qt
from PySide6.QtTest import QTest
from PySide6.QtGui import QKeyEvent

from math import floor, ceil

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
        self.bloqueados = []
        self.num = 0

        self.ejecucion = []          # proceso en ejecucion
        self.terminados = []
        self.contador = 0
        self.pausa = False
        self.estado = True
        self.interrupcion = True

        # interfaces graficas
        self.num_w = NumDialog(self)

        #slots
        self.ui.procesos_pushButton.clicked.connect(self.mostrar_num_window)

        # tamaño de columnas
        pendiente = self.ui.pendientes_tableWidget.horizontalHeader()
        pendiente.setSectionResizeMode(QHeaderView.Stretch)

        bloqueados = self.ui.bloqueados_tableWidget.horizontalHeader()
        bloqueados.setSectionResizeMode(QHeaderView.Stretch)

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
            if not self.pausa:
                self.interrupcion = False

        elif event.key() == Qt.Key_E:
            if not self.pausa:
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
        self.ui.procesos_pushButton.setEnabled(False)
        QTest.qWait(1000)

        if len(self.procesos) > 4:
            for i in range(4): self.lote.append(self.procesos.pop(0))
        else:
            for i in range(len(self.procesos)): self.lote.append(self.procesos.pop(0))

        self.proceso_ejecucion()   
    
    
    def tabla_pendientes(self, bandera, excluir):
        if len(self.procesos) > 0:
            if len(self.lote) + len(self.bloqueados) != 4:
                self.lote.append(self.procesos.pop(0))
        
        self.ui.pendientes_label.setText('Numero de procesos nuevos: ' + str(len(self.procesos)))
          
        # self.tabla_pendientes (0,-1) imprime todos y excluye el elemento -1 (no existe)
        # self.tabla_pendientes (1,n) imprime todos menos uno y excluye el elemento n
        
        self.ui.pendientes_tableWidget.setColumnCount(3)
        self.ui.pendientes_tableWidget.setRowCount(len(self.lote)-bandera)
        row = 0

        for i in range(len(self.lote)):
            if i != excluir:
                id_widget = QTableWidgetItem(str(self.lote[i][0]))
                tme_widget = QTableWidgetItem(str(self.lote[i][4]))
                tt_widget =  QTableWidgetItem(str(self.lote[i][4] - self.lote[i][5]))
                self.ui.pendientes_tableWidget.setItem(row,0,id_widget)
                self.ui.pendientes_tableWidget.setItem(row,1,tme_widget)
                self.ui.pendientes_tableWidget.setItem(row,2,tt_widget)

                row+=1
    
    def proceso_ejecucion(self):
        while len(self.lote) + len(self.bloqueados) > 0:
            if len(self.lote) != 0:
                self.pausa = False
                self.estado = True
                self.interrupcion = True
                
                ejecucion = self.lote[0]
                tiempo = ejecucion[5]
                self.tabla_pendientes(1,0)

                while tiempo > 0 and self.estado and self.interrupcion:
                    if self.pausa == False:
                        tiempo -= 1
                        self.lote[0][5] -= 1
                        self.contador += 1
                        self.tabla_ejecucion(ejecucion, tiempo)
                        self.tabla_bloqueados()
                    QTest.qWait(1000)

                self.lote[0][6] = self.estado
                self.ui.proceso_tableWidget.clearContents() # limpiar tabla

                if self.interrupcion:
                    self.terminados.append(self.lote.pop(0))
                    self.tabla_terminados()
                else:
                    self.bloqueados.append(self.lote.pop(0))     
            else:
                if self.pausa == False:
                    self.contador += 1
                    self.ui.contador_label.setText('Contador general: ' + str(self.contador))
                    self.tabla_bloqueados()
                    self.tabla_pendientes(0,-1)
                QTest.qWait(1000)

    def tabla_bloqueados(self):
        num = None
        for i in range(len(self.bloqueados)):
            if self.bloqueados[i][7] == 15:
                num = i

        if num != None:
            self.bloqueados[num][7] = 0
            self.lote.append(self.bloqueados.pop(num))
            self.tabla_pendientes(1,0)

        self.ui.bloqueados_tableWidget.setColumnCount(2)
        self.ui.bloqueados_tableWidget.setRowCount(len(self.bloqueados))
        row = 0

        for i in self.bloqueados:
            id_widget = QTableWidgetItem(str(i[0]))
            tb_widget = QTableWidgetItem(str(i[7]))

            self.ui.bloqueados_tableWidget.setItem(row,0,id_widget)
            self.ui.bloqueados_tableWidget.setItem(row,1,tb_widget)
            i[7] += 1
            row+=1

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