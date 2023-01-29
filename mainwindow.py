import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QMainWindow
from  uipy.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
