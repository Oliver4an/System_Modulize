import json
from sqlite3 import Cursor
import pyodbc
import re
class DbManger():
    def __init__(self):
        self.server="192.192.140.111"
        self.database="D10817138"
        self.username="sa"
        self.password="2022Takming"
        self.cnxn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        self.cursor=self.cnxn.cursor()

    def Login(self,id,pwd):
       
        try:
            print("DB is working")
            
            permission=self.cursor.execute(f"SELECT * FROM 員工資料表 WHERE 員工代號='{id}' AND 密碼='{pwd}'")
            
            if permission.fetchone():
                return True
            else:
                return False

        except pyodbc.Error as ex:
            
            return "connect is not working"

    def ClientInfo(self,id):
        rows=self.cursor.execute(f"SELECT * FROM 客戶基本資料 WHERE 身分證字號='{id}'").fetchall()
        if rows:
            data=[x for x in rows]
            data=data[0]
            return data

    def SecondIDType(self):
       data=[]
       items=self.cursor.execute(f"SELECT * FROM 第二證件 ").fetchall()
       for i in items:
           i=str(i)
           trantab=i.maketrans("(),''","     ")
           data.append(re.sub(r"\s+","",i.translate(trantab)))
       return data
   


