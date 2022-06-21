from PyQt5 import QtWidgets

from View.ParentsPage import Ui_MainWindow 

class Parents_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super(Parents_controller, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
      