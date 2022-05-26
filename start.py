from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QDesktopWidget
from matplotlib import widgets

import time
import pyodbc
from View.UI import Ui_MainWindow
from View.LogInUI import LogIn_MainWindow


       

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super(MainWindow_controller, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.nav)
    

    def nav(self):
        # time.sleep(3)
        size = widget.geometry()
        widget.setGeometry(
            (screen.width() - size.width()) / 2,  
            (screen.height() - size.height()) / 2,
           830, 652)
   
        widget.setCurrentIndex(widget.currentIndex()+1)

  

        
 
 

class LoginWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super(LoginWindow_controller, self).__init__()
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
            # print("{c} is working".format(c=connect_string))
            cursor=cnxn.cursor()
            permission=cursor.execute(f"SELECT * FROM 員工資料表 WHERE 員工代號='{id}' AND 密碼='{pwd}'")
            
            if permission.fetchone():
                print(True)
                self.ui.warning.setText("")
            else:
                self.ui.warning.setText("ID and Password Are not match !!")
                print(permission.fetchone())

        except pyodbc.Error as ex:
            self.ui.warning.setText("connect is not working")


     

       


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QStackedWidget()
    window = MainWindow_controller()
    Login=LoginWindow_controller()
    widget.addWidget(window)
    widget.addWidget(Login)
    screen = QDesktopWidget().screenGeometry()
    size = widget.geometry()
    widget.setGeometry(
        (screen.width() - size.width()) / 2,  
        (screen.height() - size.height()) / 2,
        813, 695)
    widget.setWindowFlags(widget.windowFlags() | Qt.FramelessWindowHint)
    widget.setAttribute(Qt.WA_TranslucentBackground)
    widget.show()
  
    
    sys.exit(app.exec_())

   