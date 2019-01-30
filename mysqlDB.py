import mysql.connector

class sqlDB:
    def __init__(self,host,user,passwd,database):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.mydb = mysql.connector.connect(
          host= self.host,
          user=self.user,
          passwd=self.passwd,
          database=self.database
        )
        self.mycursor = self.mydb.cursor()
    
    def execute(self,sql,val):
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        print(self.mycursor.rowcount,"record inserted.")