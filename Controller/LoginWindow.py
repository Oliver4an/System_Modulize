from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets 
from DbManger import DbManger
from View.LogInUI import LogIn_MainWindow
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

        dbManger=DbManger()
        perm =dbManger.Login(id,pwd)
    
        if perm:
            self.ui.warning.setText("")
            self.ui.Account.setText("")
            self.ui.PassWord.setText("")
            self.main_window = MainPage_controller()
            self.main_window.show()
            self.close()
        elif perm=="connect is not working":
            self.ui.warning.setText("connect is not working")
        else:
            self.ui.warning.setText("ID and Password Are not match !!")
         

