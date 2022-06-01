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
  

class LoginWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow_controller, self).__init__()
        self.setWindowFlags( Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui = LogIn_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.nav)
 
    def nav(self):
       
        id = self.ui.Account.text()
        pwd=self.ui.PassWord.text()
        print(id,pwd)
        try:
            server="192.192.140.111"
            database="D10817138"
            username="sa"
            password="2022Takming"
            connect_string = "UID={u};PWD={p}".format(u=username, p=password)
            cnxn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            print("{c} is working".format(c=connect_string))
            cursor=cnxn.cursor()
            permission=cursor.execute(f"SELECT * FROM 員工資料表 WHERE 員工代號='{id}' AND 密碼='{pwd}'")
            
            if permission.fetchone():
                print(True)
                self.ui.warning.setText("")
                self.ui.Account.setText("")
                self.ui.PassWord.setText("")
                self.main_window = MainPage_controller()
                self.main_window.show()
                self.close()
            else:
                self.ui.warning.setText("ID and Password Are not match !!")
                print(permission.fetchone())

        except pyodbc.Error as ex:
            self.ui.warning.setText("connect is not working")


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

       

    
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())

   