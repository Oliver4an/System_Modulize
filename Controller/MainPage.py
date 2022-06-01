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


class MainPage_controller(QtWidgets.QMainWindow):
   def __init__(self):
       super(MainPage_controller, self).__init__()
       self.setWindowFlags( Qt.FramelessWindowHint)
       self.setAttribute(Qt.WA_TranslucentBackground)
       self.ui=MainPage_Window()
       self.ui.setupUi(self)
       self.ui.burger.clicked.connect(lambda: self.slideLeftMenu())
       self.ui.Context.setCurrentWidget(self.ui.Home)
       self.ui.contract.clicked.connect(lambda :self.CloseMenu(self.ui.Context.setCurrentWidget(self.ui.ContractLayout)))
       self.ui.rules.clicked.connect(lambda :self.CloseMenu(self.ui.Context.setCurrentWidget(self.ui.RulesLayout)))
       self.ui.install.clicked.connect(lambda :self.CloseMenu(self.ui.Context.setCurrentWidget(self.ui.InstallLayout)))
       self.ui.change.clicked.connect(lambda :self.CloseMenu(self.ui.Context.setCurrentWidget(self.ui.ChangeLayout)))
       self.ui.claim.clicked.connect(lambda :self.CloseMenu(self.ui.Context.setCurrentWidget(self.ui.ClaimLayout)))
       self.ui.bill.clicked.connect(lambda :self.CloseMenu(self.ui.Context.setCurrentWidget(self.ui.BillLayout)))
       self.ui.writeoff.clicked.connect(lambda : self.CloseMenu(self.ui.Context.setCurrentWidget(self.ui.WriteOffLayout)))
       self.ui.split.clicked.connect(lambda :self.CloseMenu(self.ui.Context.setCurrentWidget(self.ui.SplitLayout)))
       self.ui.print.clicked.connect(lambda :self.CloseMenu(self.ui.Context.setCurrentWidget(self.ui.PrintLayout)))
       self.ui.exit.clicked.connect(QCoreApplication.instance().quit)
       self.ui.logout.clicked.connect(lambda:self.logoff())

   def slideLeftMenu(self):
            # Get current left menu width
        width = self.ui.Left_Bar.width()
        
        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 150
        # If maximized
        else:
            # Restore menu
            newWidth =0
        print(f"width:{width},newWidth:{newWidth}")
        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.Left_Bar, b"minimumWidth")#Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

   def CloseMenu(self,action=""):
    action
    # Animate the transition
    self.animation = QPropertyAnimation(self.ui.Left_Bar, b"minimumWidth")#Animate minimumWidht
    self.animation.setDuration(250)
    self.animation.setStartValue(self.ui.Left_Bar.width())#Start value is the current menu width
    self.animation.setEndValue(0)#end value is the new menu width
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()

   def logoff(self):
       self.CloseMenu("")
       from Controller.LoginWindow import LoginWindow_controller
       self.login_window=LoginWindow_controller()
       self.login_window.show()
       self.close()
           
   def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()
    
   def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

       