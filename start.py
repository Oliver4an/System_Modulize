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
from Controller.MainWindow import MainWindow_controller
  

    
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())

   