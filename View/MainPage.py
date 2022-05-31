# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Qt_Ui/MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MainPage_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border:none;\n"
)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MainFrame.setStyleSheet("background-color: rgb(0, 190, 255);\n"
"border:none;\n"
"border-radiue:30px;")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MainFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Left_Bar = QtWidgets.QFrame(self.MainFrame)
        self.Left_Bar.setMaximumSize(QtCore.QSize(0, 16777215))
        self.Left_Bar.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 132, 26);\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"    padding:5px 10px;\n"
"    border:none;\n"
"    border-radius:10px;\n"
"    background-color: rgb(255, 132, 26);\n"
"}")
        self.Left_Bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Left_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Left_Bar.setObjectName("Left_Bar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Left_Bar)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Left_Bar)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.Left_Bar)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.Left_Bar)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.Left_Bar)
        self.Fragment = QtWidgets.QFrame(self.MainFrame)
        self.Fragment.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Fragment.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Fragment.setObjectName("Fragment")
        self.Header = QtWidgets.QFrame(self.Fragment)
        self.Header.setGeometry(QtCore.QRect(0, -10, 796, 70))
        self.Header.setMaximumSize(QtCore.QSize(16777215, 70))
        self.Header.setStyleSheet("background-color: rgb(255, 132, 26);")
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.burger = QtWidgets.QPushButton(self.Header)
        self.burger.setGeometry(QtCore.QRect(20, 30, 71, 31))
        self.burger.setObjectName("burger")
        self.horizontalLayout.addWidget(self.Fragment)
        self.verticalLayout.addWidget(self.MainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.burger.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainPage_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
