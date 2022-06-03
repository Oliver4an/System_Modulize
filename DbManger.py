import json
import pyodbc

class DbManger():
    def __init__(self):
        self.server="192.192.140.111"
        self.database="D10817138"
        self.username="sa"
        self.password="2022Takming"
        self.cnxn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)

    def Login(self,id,pwd):
       
        try:
            print("DB is working")
            cursor=self.cnxn.cursor()
            permission=cursor.execute(f"SELECT * FROM 員工資料表 WHERE 員工代號='{id}' AND 密碼='{pwd}'")
            
            if permission.fetchone():
                return True
            else:
                return False

        except pyodbc.Error as ex:
            
            return "connect is not working"

    def ClientInfo(self,id):
        
        cursor=self.cnxn.cursor()
        rows=cursor.execute(f"SELECT * FROM 客戶基本資料 WHERE 身分證字號='{id}'").fetchall()
        data=[x for x in rows]
        data=data[0]
        return data

