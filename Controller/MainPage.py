from PyQt5.QtCore import Qt,QPropertyAnimation,QCoreApplication,QPoint,QDateTime,QTimer
from PyQt5 import QtWidgets ,QtCore
from PyQt5.QtGui import *
import datetime
from Controller.ParentsPage import Parents_controller
from DbManger import DbManger
from View.MainPage import MainPage_Window


class MainPage_controller(QtWidgets.QMainWindow):
   def __init__(self):
       super(MainPage_controller, self).__init__()
       self.setWindowFlags( Qt.FramelessWindowHint)
       self.setAttribute(Qt.WA_TranslucentBackground)
       self.ui=MainPage_Window()
       self.ui.setupUi(self)
       self.ui.burger.clicked.connect(lambda: self.slideLeftMenu())
       self.dbManger=DbManger()

       ################Change Fragment
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

       ###############Task of Install
       self.Second()
       self.setTime()
       self.ui.IDNumber.textChanged.connect(self.loadData)
       self.ui.AddressCheck.stateChanged.connect(self.sameAdd)
       self.ui.Birth.textChanged.connect(lambda: self.AgeCheck() if  (len(self.ui.IDNumber.toPlainText())==10) else "")
   
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
   
  
       


#########ClientInfo#################
   def loadData(self):
       ###id_check###
        if len(self.ui.IDNumber.toPlainText())>0:
            if self.ui.IDNumber.toPlainText()[0].istitle():
                if len(self.ui.IDNumber.toPlainText())>1:
                    if self.ui.IDNumber.toPlainText()[1]=="1":
                        self.ui.Male.setChecked(True)
                    elif self.ui.IDNumber.toPlainText()[1]=="2":
                            self.ui.Female.setChecked(True)       
                    else:
                        ID= self.ui.IDNumber.toPlainText()
                        self.ui.IDNumber.setText(ID[0])
                        cur = self.ui.IDNumber.textCursor()
                        cur.movePosition(QTextCursor.End)
                        self.ui.IDNumber.setTextCursor(cur)  
            elif self.ui.IDNumber.toPlainText()[0].isalpha():
                self.ui.IDNumber.setText(self.ui.IDNumber.toPlainText()[0].upper())
                cur = self.ui.IDNumber.textCursor()
                cur.movePosition(QTextCursor.End)
                self.ui.IDNumber.setTextCursor(cur)            
            else:
                self.ui.IDNumber.setText("")
       
      ####Get Info
        if len(self.ui.IDNumber.toPlainText())==10:
            IdNum= self.ui.IDNumber.toPlainText()
            client=self.dbManger.ClientInfo(IdNum)
            if client:
                self.ui.Name.setText(client[2])
                self.ui.Birth.setText(client[3])
                self.ui.Addr1.setText(client[5])
                self.ui.Addr2 .setText(client[6])
                self.ui.SecondId.setCurrentText(client[1])
                self.AddrCheck(client[5],client[6])
                self.AgeCheck()
        elif len(self.ui.IDNumber.toPlainText())==0:
            self.ui.SecondId.setCurrentText("請選擇")
        else:
            self.ui.Name.clear()
            self.ui.Birth.clear()
            self.ui.Male.setChecked(False)
            self.ui.Male.setChecked(False)
            self.ui.AddressCheck.setChecked(False)
            self.ui.Addr1.clear()
            self.ui.Addr2 .clear()
            self.ui.AddressCheck.setChecked(False)
      
   def AddrCheck(self,a1,a2):
       self.ui.AddressCheck.setChecked(True) if (a1==a2) else (self.ui.AddressCheck.setChecked(False))

   def sameAdd(self):
       if self.ui.Addr1.toPlainText():
           self.ui.Addr2.setText(self.ui.Addr1.toPlainText())  

   def AgeCheck(self):  
       age=0
       if len(self.ui.IDNumber.toPlainText())==10 & len(self.ui.Birth.toPlainText())==10:
           
            print(self.ui.IDNumber.toPlainText())
            today=str(datetime.date.today()).split("-")
            birth=self.ui.Birth.toPlainText().split("/")
            if(int(today[1])-int(birth[1])>=0):
                    age=int(today[0])-int(birth[0])
            else:
                    age=int(today[0])-int(birth[0])-1
            
            if age<18:
                    print(age)
                    self.parent=Parents_controller()
                    self.parent.show()

   def Second(self):
     items=self.dbManger.SecondIDType()
     self.ui.SecondId.addItems(items)

   
   def setTime(self):
       timer=QTimer(self)
       timer.timeout.connect(self.Nowtime)
       timer.start(1000)
    
   def Nowtime(self):
       datetime = QDateTime.currentDateTime() #獲取當前日期與時間
       self.ui.Date.setText(datetime.toString())
    #    print(datetime.toString())

            # loc_dt = datetime.datetime.today() 
            # loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
            # self.trigger.emit(str(loc_dt_format))
            # print(str(loc_dt_format))


       
                




   
   
   
  