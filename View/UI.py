# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Qt_Ui/CopyRight.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 695)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Declare_Img = QtWidgets.QLabel(self.centralwidget)
        self.Declare_Img.setGeometry(QtCore.QRect(120, 160, 581, 371))
        self.Declare_Img.setStyleSheet("border-image: url(:/image/900hz.jpg);\n"
"border-top-left-radius:40px;\n"
"border-bottom-left-radius:40px;\n"
"border-top-right-radius:40px;\n"
"border-bottom-right-radius:40px;")
        self.Declare_Img.setText("")
        self.Declare_Img.setAlignment(QtCore.Qt.AlignCenter)
        self.Declare_Img.setObjectName("Declare_Img")
        self.Slogan = QtWidgets.QLabel(self.centralwidget)
        self.Slogan.setGeometry(QtCore.QRect(310, 430, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Hanunoo")
        font.setPointSize(19)
        self.Slogan.setFont(font)
        self.Slogan.setStyleSheet("Color:white;")
        self.Slogan.setObjectName("Slogan")
        self.CompanyName = QtWidgets.QLabel(self.centralwidget)
        self.CompanyName.setGeometry(QtCore.QRect(150, 460, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Hanunoo")
        font.setPointSize(17)
        self.CompanyName.setFont(font)
        self.CompanyName.setStyleSheet("Color:white;")
        self.CompanyName.setObjectName("CompanyName")
        self.SystemName = QtWidgets.QLabel(self.centralwidget)
        self.SystemName.setGeometry(QtCore.QRect(140, 490, 291, 31))
        font = QtGui.QFont()
        font.setFamily("PCMyungjo")
        font.setPointSize(14)
        self.SystemName.setFont(font)
        self.SystemName.setStyleSheet("Color:white;")
        self.SystemName.setObjectName("SystemName")
        self.TeamName = QtWidgets.QLabel(self.centralwidget)
        self.TeamName.setGeometry(QtCore.QRect(550, 490, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Vai")
        font.setPointSize(14)
        self.TeamName.setFont(font)
        self.TeamName.setStyleSheet("Color:white;")
        self.TeamName.setObjectName("TeamName")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Slogan.setText(_translate("MainWindow", "Every calling for Reason"))
        self.CompanyName.setText(_translate("MainWindow", "900??????????????????"))
        self.SystemName.setText(_translate("MainWindow", "????????????????????????????????????  Version 0.5.28"))
        self.TeamName.setText(_translate("MainWindow", "????????????: D10817138"))
from View import copyright_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
