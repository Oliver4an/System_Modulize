from PyQt5 import QtCore, QtGui, QtWidgets


class MainPage_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QFrame(self.centralwidget)
        self.Header.setMaximumSize(QtCore.QSize(16777215, 75))
        self.Header.setStyleSheet("background-color:rgb(248,142,114);\n"
"border:none;")
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.burger = QtWidgets.QPushButton(self.Header)
        self.burger.setGeometry(QtCore.QRect(10, 20, 41, 31))
        self.burger.setStyleSheet("border-image: url(:/image/icons/cil-menu.png);")
        self.burger.setText("")
        self.burger.setObjectName("burger")
        self.verticalLayout.addWidget(self.Header)
        self.Context = QtWidgets.QFrame(self.centralwidget)
        self.Context.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Context.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Context.setObjectName("Context")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Context)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Left_Bar = QtWidgets.QFrame(self.Context)
        self.Left_Bar.setMaximumSize(QtCore.QSize(0, 16777215))
        self.Left_Bar.setStyleSheet("\n"
"\n"
"QFrame{\n"
"    background-color: rgb(249, 249, 249);\n"
"}\n"
"\n"
"QPushButton{\n"
"    width:150px;\n"
"    font-size: 20px;\n"
"    color:black;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(143,195,217);\n"
"}\n"
"\n"
"")
        self.Left_Bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Left_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Left_Bar.setObjectName("Left_Bar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Left_Bar)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contract = QtWidgets.QPushButton(self.Left_Bar)
        self.contract.setObjectName("contract")
        self.verticalLayout_2.addWidget(self.contract)
        self.rules = QtWidgets.QPushButton(self.Left_Bar)
        self.rules.setObjectName("rules")
        self.verticalLayout_2.addWidget(self.rules)
        self.install = QtWidgets.QPushButton(self.Left_Bar)
        self.install.setObjectName("install")
        self.verticalLayout_2.addWidget(self.install)
        self.change = QtWidgets.QPushButton(self.Left_Bar)
        self.change.setObjectName("change")
        self.verticalLayout_2.addWidget(self.change)
        self.claim = QtWidgets.QPushButton(self.Left_Bar)
        self.claim.setObjectName("claim")
        self.verticalLayout_2.addWidget(self.claim)
        self.bill = QtWidgets.QPushButton(self.Left_Bar)
        self.bill.setObjectName("bill")
        self.verticalLayout_2.addWidget(self.bill)
        self.writeoff = QtWidgets.QPushButton(self.Left_Bar)
        self.writeoff.setObjectName("writeoff")
        self.verticalLayout_2.addWidget(self.writeoff)
        self.print = QtWidgets.QPushButton(self.Left_Bar)
        self.print.setObjectName("print")
        self.verticalLayout_2.addWidget(self.print)
        self.logout = QtWidgets.QPushButton(self.Left_Bar)
        self.logout.setObjectName("logout")
        self.verticalLayout_2.addWidget(self.logout)
        self.exit = QtWidgets.QPushButton(self.Left_Bar)
        self.exit.setObjectName("exit")
        self.verticalLayout_2.addWidget(self.exit)
        self.horizontalLayout.addWidget(self.Left_Bar)
        self.Fragment = QtWidgets.QFrame(self.Context)
        self.Fragment.setStyleSheet("background-color:rgb(231,230,235);\n"
"border:none;")
        self.Fragment.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Fragment.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Fragment.setMidLineWidth(0)
        self.Fragment.setObjectName("Fragment")
        self.horizontalLayout.addWidget(self.Fragment)
        self.verticalLayout.addWidget(self.Context)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.contract.setText(_translate("MainWindow", "制定合約"))
        self.rules.setText(_translate("MainWindow", "營運規則"))
        self.install.setText(_translate("MainWindow", "申裝"))
        self.change.setText(_translate("MainWindow", "客戶異動"))
        self.claim.setText(_translate("MainWindow", "申吿"))
        self.bill.setText(_translate("MainWindow", "出帳"))
        self.writeoff.setText(_translate("MainWindow", "銷帳"))
        self.print.setText(_translate("MainWindow", "列印"))
        self.logout.setText(_translate("MainWindow", "登出"))
        self.exit.setText(_translate("MainWindow", "離開"))
from View import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainPage_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
