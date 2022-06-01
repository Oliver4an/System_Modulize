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
from Controller.MainPage import MainPage_controller
  
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

