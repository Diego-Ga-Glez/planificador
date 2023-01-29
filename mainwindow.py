from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from  uipy.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #slots
        self.ui.procesos_pushButton.clicked.connect(self.num_window)

    @Slot()
    def num_window(self):
        print('click')
