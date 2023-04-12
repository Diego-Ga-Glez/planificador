from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QProgressBar
from PySide6.QtCore import Slot, Qt
from PySide6.QtTest import QTest
from PySide6.QtGui import QKeyEvent

from math import ceil

from uipy.ui_mainwindow import Ui_MainWindow
from numdialog import NumDialog
from timedialog import TimeDialog
from pagdialog import PagDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # variables
        self.procesos = []           # lista de procesos en total
        
        self.lote = []               # lote actual en ejecucion
        self.bloqueados = []

        self.ejecucion = []          # proceso en ejecucion
        self.terminados = []
        self.suspendidos = []       # procesos suspendidos
        self.contador = 0
        self.q = 0

        self.num_marcos = 40
        self.marcos = []
        # generar marcos
        # primer elemento espacio ocupado (5/5, 4/5, 3/5, 2/5, 1/5, 0/5)
        # segundo elemento quien lo ocupa (id del proceso)
        # tercer elemento qué página es
        for _ in range(self.num_marcos - 2):
            self.marcos.append([0,'null','null'])
        # Marcos para el SO
        self.marcos.append([5,'SO','null'])
        self.marcos.append([5,'SO','null'])

        # cantidad de marcos disponibles
        self.marcos_disponibles = 38

        self.interrupciones = False # variable para habilitar 
        self.pausa = False
        self.estado = True
        self.interrupcion = True
        self.suspendido = True

        # interfaces graficas
        self.num_w = NumDialog(self)
        self.time_w = TimeDialog(self)
        self.pag_w = PagDialog(self)

        #slots
        self.ui.procesos_pushButton.clicked.connect(self.mostrar_num_window)
        self.ui.tiempos_pushButton.clicked.connect(self.mostrar_time_window)

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

        memoria1H = self.ui.memoria1_tableWidget.horizontalHeader()
        memoria1H.setSectionResizeMode(QHeaderView.Stretch)
        memoria2H = self.ui.memoria2_tableWidget.horizontalHeader()
        memoria2H.setSectionResizeMode(QHeaderView.Stretch)
        memoria1V = self.ui.memoria1_tableWidget.verticalHeader()
        memoria1V.setSectionResizeMode(QHeaderView.Stretch)
        memoria2V = self.ui.memoria2_tableWidget.verticalHeader()
        memoria2V.setSectionResizeMode(QHeaderView.Stretch)

    def closeEvent(self, event):
        exit()
    
    def keyPressEvent(self, event: QKeyEvent):
        if self.interrupciones:
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

                # focus en la ventana mainwindows
                if self.time_w.isVisible():
                    self.time_w.close()

            elif event.key() == Qt.Key_N:
                if not self.pausa:
                    self.num_w.num_window(valor=False)

            elif event.key() == Qt.Key_T:
                if not self.pausa:
                    self.mostrar_time_window()
            
            elif event.key() == Qt.Key_A:
                if not self.pausa:
                    self.mostrar_pag_window()
            
            elif event.key() == Qt.Key_S:
                if not self.pausa:
                    self.suspendido = False

            elif event.key() == Qt.Key_R:
                if not self.pausa:
                    if len(self.suspendidos) != 0:
                        paginas = ceil(self.suspendidos[0][11]/5)
                        if self.marcos_disponibles >= paginas:
                            self.procesos.insert(0,self.suspendidos.pop(0))
                            self.memoria()
                            self.tabla_pendientes(1,0)
                            #self.txt_suspendidos()
        
        return super().keyPressEvent(event)
    
    @Slot()
    def mostrar_time_window(self):
        self.time_w.show()
        self.time_w.tabla_tiempos()
        self.time_w.exec()
    
    def mostrar_pag_window(self):
        self.pag_w.show()
        self.pag_w.tabla_paginas(1)
        self.pag_w.tabla_paginas(2)
        self.pag_w.exec()
    
    def calc_marcos_disponibles(self):
        num = 0
        for i in range(self.num_marcos):
            if self.marcos[i] == [0,'null','null']:
                num+=1

        return num
    
    def liberar_marcos(self, proceso):
        for i in range(self.num_marcos):
            if self.marcos[i][1] == proceso[0]:
                self.marcos[i][0] = 0
                self.marcos[i][1] = 'null'
                self.marcos[i][2] = 'null'

        self.marcos_disponibles = self.calc_marcos_disponibles()
    
    # ingresar procesos a memoria
    def memoria(self):
        # verifica que haya procesos para agregar
        if len(self.procesos) == 0:
            return
        
        continuar = True

        while len(self.procesos) != 0 and continuar:

            tamaño = self.procesos[0][11]
            paginas = ceil(tamaño/5) # calcular las paginas del proceso
            num_pagina = 1

            if self.marcos_disponibles >= paginas:
                for i in range(self.num_marcos):
                    if paginas == 0: 
                        break
                     # mientras paginas no sea cero y si hay una posicion libre 
                     # se agrega una pagina
                    if self.marcos[i] == [0,'null','null']:
                        # se agrega el espacio ocupado
                        if tamaño >= 5:
                            self.marcos[i][0] = 5
                            tamaño -= 5
                        else:
                            self.marcos[i][0] = tamaño
                            tamaño-=tamaño

                        # se agrega en el marco quien lo esta ocupando (id del proceso)
                        self.marcos[i][1] = self.procesos[0][0]
                        # se agrega el número de página
                        self.marcos[i][2] = num_pagina
                        paginas -= 1
                        num_pagina += 1

                # recalcular marcos disponibles
                self.marcos_disponibles = self.calc_marcos_disponibles()
                # agregar a listos
                self.procesos[0][8] = self.contador #TLL
                self.lote.append(self.procesos.pop(0))

            else:
                continuar = False 
    
    def mostrar_num_window(self):
        self.num_w.show()
        self.num_w.exec()
        self.ui.procesos_pushButton.setEnabled(False)
        self.interrupciones = True # habilita las interrupciones

        # agregar procesos a memoria 
        self.memoria()

        # se define el quantum en mainwindow
        self.q = self.num_w.quantum
        self.ui.quantum_label.setText("Quantum: " + str(self.q))
    
        self.proceso_ejecucion()
        self.tabla_memoria(self.ui.memoria1_tableWidget)
        self.tabla_memoria(self.ui.memoria2_tableWidget)
        self.ui.tiempos_pushButton.setEnabled(True)
        self.interrupciones = False
    
    def proceso_ejecucion(self):
        mantener_quantum = True
        while len(self.lote) + len(self.bloqueados) + len(self.suspendidos) > 0:
            if len(self.lote) != 0:
                self.pausa = False
                self.estado = True
                self.interrupcion = True
                self.suspendido = True
                
                ejecucion = self.lote[0]
                tiempo = ejecucion[5]
                if mantener_quantum:
                    quantum = 0
                mantener_quantum = True

                if self.lote[0][10] == -1:
                    self.lote[0][10] = self.contador #T-RES

                self.tabla_pendientes(1,0)

                while tiempo > 0 and self.suspendido and self.estado and self.interrupcion and quantum < self.q:
                    if self.pausa == False:
                        tiempo -= 1
                        quantum += 1
                        self.lote[0][5] -= 1
                        self.contador += 1
                        self.tabla_ejecucion(ejecucion, tiempo, quantum)
                        self.tabla_bloqueados()

                    QTest.qWait(1000)
 
                self.lote[0][6] = self.estado
                if self.lote[0][5] == 0:
                    self.lote[0][6] = True
                    
                self.ui.proceso_tableWidget.clearContents() # limpiar tabla
                
                if self.lote[0][5] == 0 or not self.estado:
                    terminado = self.lote.pop(0)
                    self.liberar_marcos(terminado) # liberar marcos
                    terminado[9] = self.contador #TF
                    self.terminados.append(terminado)
                    self.tabla_terminados()

                elif quantum == self.q and tiempo > 0:
                    self.lote.append(self.lote.pop(0)) 
                elif not self.interrupcion:
                    self.bloqueados.append(self.lote.pop(0))
                elif not self.suspendido:
                    if len(self.bloqueados) != 0:
                        self.liberar_marcos(self.bloqueados[0])
                        self.suspendidos.append(self.bloqueados.pop(0))
                        #self.txt_suspendidos()
                    else:
                         mantener_quantum = False
                    
                                
            else:
                if self.pausa == False:
                    if not self.suspendido:
                        if len(self.bloqueados) != 0:
                            self.bloqueados[0][7] = 1
                            self.liberar_marcos(self.bloqueados[0])
                            self.suspendidos.append(self.bloqueados.pop(0))
                            #self.txt_suspendidos()
                    self.contador += 1
                    self.ui.contador_label.setText('Contador general: ' + str(self.contador))
                    self.tabla_bloqueados()
                    self.tabla_pendientes(0,-1)
                    
                QTest.qWait(1000)

    def tabla_pendientes(self, bandera, excluir):
        if len(self.procesos) > 0:
            self.memoria()
        
        self.tabla_memoria(self.ui.memoria1_tableWidget)
        self.tabla_memoria(self.ui.memoria2_tableWidget)

        self.ui.pendientes_label.setText('Numero de procesos nuevos: ' + str(len(self.procesos)))

        if len(self.procesos) > 0:
            self.ui.idSig_label.setText('ID: ' + str(self.procesos[0][0]))
            self.ui.tamSig_label.setText('Tamaño: ' + str(self.procesos[0][11]))
        else:
            self.ui.idSig_label.setText('ID: null')
            self.ui.tamSig_label.setText('Tamaño: null')

        # self.tabla_pendientes (0,-1) imprime todos y excluye el elemento -1 (no existe)
        # self.tabla_pendientes (1,n) imprime todos menos uno y excluye el elemento n
        
        self.ui.pendientes_tableWidget.setColumnCount(4)
        self.ui.pendientes_tableWidget.setRowCount(len(self.lote)-bandera)
        row = 0

        for i in range(len(self.lote)):
            if i != excluir:
                id_widget = QTableWidgetItem(str(self.lote[i][0]))
                tam_widget = QTableWidgetItem(str(self.lote[i][11]))
                tme_widget = QTableWidgetItem(str(self.lote[i][4]))
                tt_widget = QTableWidgetItem(str(self.lote[i][4] - self.lote[i][5]))
                
                self.ui.pendientes_tableWidget.setItem(row,0,id_widget)
                self.ui.pendientes_tableWidget.setItem(row,1,tam_widget)
                self.ui.pendientes_tableWidget.setItem(row,2,tme_widget)
                self.ui.pendientes_tableWidget.setItem(row,3,tt_widget)

                row+=1
    
    def tabla_bloqueados(self):
        if len(self.bloqueados) != 0:
            if self.bloqueados[0][7] == 8:
                self.bloqueados[0][7] = 1
                self.lote.append(self.bloqueados.pop(0))
                self.tabla_pendientes(1,0)

        self.ui.bloqueados_tableWidget.setColumnCount(3)
        self.ui.bloqueados_tableWidget.setRowCount(len(self.bloqueados))
        row = 0

        for i in self.bloqueados:
            id_widget = QTableWidgetItem(str(i[0]))
            tam_widget = QTableWidgetItem(str(i[11]))
            tb_widget = QTableWidgetItem(str(i[7]))

            self.ui.bloqueados_tableWidget.setItem(row,0,id_widget)
            self.ui.bloqueados_tableWidget.setItem(row,1,tam_widget)
            self.ui.bloqueados_tableWidget.setItem(row,2,tb_widget)
            i[7] += 1
            row+=1

    def tabla_ejecucion(self, ejecucion, tiempo, quantum):
            self.ui.proceso_tableWidget.setColumnCount(1)
            self.ui.proceso_tableWidget.setRowCount(7)

            id_widget = QTableWidgetItem(str(ejecucion[0]))
            tam_widget = QTableWidgetItem(str(ejecucion[11]))

            operacion = self.concatenar_op(ejecucion[1], ejecucion[2], ejecucion[3])
            op_widget = QTableWidgetItem(operacion)

            tme_widget = QTableWidgetItem(str(ejecucion[4]))
            transcurrido_widget = QTableWidgetItem(str(ejecucion[4]-tiempo))
            quantum_widget = QTableWidgetItem(str(quantum))
            restante_widget = QTableWidgetItem(str(tiempo))

            self.ui.proceso_tableWidget.setItem(0,0,id_widget)
            self.ui.proceso_tableWidget.setItem(1,0,tam_widget)
            self.ui.proceso_tableWidget.setItem(2,0,op_widget)
            self.ui.proceso_tableWidget.setItem(3,0,tme_widget)
            self.ui.proceso_tableWidget.setItem(4,0,transcurrido_widget)
            self.ui.proceso_tableWidget.setItem(5,0,quantum_widget)
            self.ui.proceso_tableWidget.setItem(6,0,restante_widget)

            self.ui.contador_label.setText('Contador general: ' + str(self.contador))

    def tabla_terminados(self):
        self.ui.terminados_tableWidget.setColumnCount(4)
        self.ui.terminados_tableWidget.setRowCount(len(self.terminados))
        row = 0

        for i in self.terminados:
            id_widget = QTableWidgetItem(str(i[0]))
            tam_widget = QTableWidgetItem(str(i[11]))

            operacion = self.concatenar_op(i[1], i[2], i[3])
            op_widget = QTableWidgetItem(operacion)

            if i[6] == True:
                resultado = self.resultado_op(i[1], i[2], i[3])
            else:
                resultado = 'ERROR'

            res_widget = QTableWidgetItem(resultado)
            
            self.ui.terminados_tableWidget.setItem(row,0,id_widget)
            self.ui.terminados_tableWidget.setItem(row,1,tam_widget)
            self.ui.terminados_tableWidget.setItem(row,2,op_widget)
            self.ui.terminados_tableWidget.setItem(row,3,res_widget)
            row+=1
    
    def tabla_memoria(self, tabla):
        tabla.setColumnCount(2)
        tabla.setRowCount(20)
        row = 0

        for i in range(int(self.num_marcos/2)):
            if tabla == self.ui.memoria1_tableWidget:
                indice = i
            else:
                indice = int(i + self.num_marcos/2)

            marco_widget = QTableWidgetItem(str(indice + 1))
            progressbar = self.barra_progreso(indice, 'mainwindow')

            tabla.setItem(row,0,marco_widget)
            tabla.setCellWidget(row,1,progressbar)

            row+=1
    
    def barra_progreso(self, indice, ventana):
        progressbar = QProgressBar()
        progressbar.setMinimum(0)
        progressbar.setMaximum(5)
        progressbar.setValue(self.marcos[indice][0])
        progressbar.setAlignment(Qt.AlignCenter)

        color = '#C26E8B'

        if ventana == 'mainwindow':
            progressbar.setTextVisible(False)

        else:
            division = str(self.marcos[indice][0]) + ' / 5'
            progressbar.setFormat(division)

            if self.marcos[indice][1] != 'null': # Cambio de color de la barra
                encontrado = False
                
                for proceso in self.bloqueados: # Proceso bloqueado
                    if encontrado == True:
                        break
                    if self.marcos[indice][1] == proceso[0]:
                        color = '#96CDFF'
                        encontrado = True
                
                for proceso in self.lote: # Proceso listo
                    if encontrado == True:
                        break
                    if self.marcos[indice][1] == proceso[0]:
                        color = '#DBBADD'
                        if proceso[0] == self.lote[0][0]: # Proceso en ejecución
                            color = '#E4D6A7'
                        encontrado = True
                
                if self.marcos[indice][1] == 'SO':
                    color = '#2B4162'

        progressbar.setStyleSheet("QProgressBar::chunk {" f"background-color: {color};" "}")
        return progressbar

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