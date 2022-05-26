from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from matplotlib import widgets
from View.UI import Ui_MainWindow
from View.LogInUI import LogIn_MainWindow
from PIL import Image
import time
import start

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super(MainWindow_controller, self).__init__()
        self.ui = Ui_MainWindow()
        self.work = QThread()
        self.ui.setupUi(self)
        self.ui.CompanyName.mouseDoubleClickEvent(self.nav)

        def nav():
            start.widget.setCurrentIndex(start.widget.currentIndex()+1)
        
        
 

class LoginWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super(LoginWindow_controller, self).__init__()
        self.ui = LogIn_MainWindow()
        self.ui.setupUi(self)
       

    
    




        


   