from PyQt5.QtCore import Qt,QTimer,QPropertyAnimation,QCoreApplication,QPoint
from PyQt5 import QtWidgets ,QtCore
from PyQt5.QtWidgets import QDesktopWidget
from matplotlib import widgets
import time
import pyodbc
from pyparsing import CloseMatch
from View.UI import Ui_MainWindow
from View.LogInUI import LogIn_MainWindow
from View.MainPage import MainPage_Window
from Controller.LoginWindow import LoginWindow_controller

class MainWindow_controller(QtWidgets.QMainWindow):
     def __init__(self):
        super(MainWindow_controller, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags( Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.nav)
        self.timer.start(3000)
             
     def nav(self):
        self.login_window=LoginWindow_controller()
        self.login_window.show()
        self.close()
        self.timer.stop()
  