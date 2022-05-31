from PyQt5.QtCore import Qt,QTimer,QPropertyAnimation
from PyQt5 import QtWidgets ,QtCore
from PyQt5.QtWidgets import QDesktopWidget
from matplotlib import widgets
import time
import pyodbc
from View.UI import Ui_MainWindow
from View.LogInUI import LogIn_MainWindow
from View.MainPage import MainPage_Window
class MainWindow_controller(QtWidgets.QMainWindow):
     def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super(MainWindow_controller, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.nav)
        self.timer.start(3000)
             
     def nav(self):
        size = widget.geometry()
        widget.setGeometry(
            (screen.width() - size.width()) / 2,  
            (screen.height() - size.height()) / 2,
        830, 652)
        widget.setCurrentIndex(widget.currentIndex()+1)

        self.timer.stop()
  

class LoginWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(LoginWindow_controller, self).__init__()
        self.ui = LogIn_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.nav)

    def mousePressEvent(self, event):
    
        self.clickPosition = event.globalPos()

        def moveWindow(e):
                # Detect if the window is  normal size
                # ###############################################  
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        
        self.ui.centralwidget.mouseMoveEvent = moveWindow

    
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
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                self.ui.warning.setText("ID and Password Are not match !!")
                print(permission.fetchone())

        except pyodbc.Error as ex:
            self.ui.warning.setText("connect is not working")


class MainPage_controller(QtWidgets.QMainWindow):
   def __init__(self):
       super(MainPage_controller, self).__init__()
       self.ui=MainPage_Window()
       self.ui.setupUi(self)
    #    self.ui.Fragment.mousePressEvent.connect(lambda: self.closeMenu())
       self.ui.burger.clicked.connect(lambda: self.slideLeftMenu())

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


   def closeMenu(self):
            # Get current left menu width
        width = self.ui.Left_Bar.width()
        
        # If minimized
        if width == 150:
            # Expand menu
            newWidth = 0
      
      

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.Left_Bar, b"minimumWidth")#Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    
if __name__ == '__main__':
    import sys
  
    app = QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QStackedWidget()
    screen = QDesktopWidget().screenGeometry()
    window = MainWindow_controller()
    Login=LoginWindow_controller()
    Main=MainPage_controller()
    widget.addWidget(window)
    widget.addWidget(Login)
    widget.addWidget(Main)
    
    size = widget.geometry()
    widget.setGeometry(
        (screen.width() - size.width()) / 2,  
        (screen.height() - size.height()) / 2,
        813, 695)
    widget.setWindowFlags(widget.windowFlags() | Qt.FramelessWindowHint)
    widget.setAttribute(Qt.WA_TranslucentBackground)
   
    widget.show()
    
   
    
   


    
   
    sys.exit(app.exec_())

   