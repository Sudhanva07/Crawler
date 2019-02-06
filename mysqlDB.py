import mysql.connector

class sqlDB:
    
    #connection esablishing with mysql 
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
        self.mycursor = self.mydb.cursor(buffered=True)
    
    #execution of SQL query which has user input value
    def execute_val(self,sql,val):
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        print(self.mycursor.rowcount,"record inserted.")
    
    #execution od SQL query with just a single statement
    def execute_single(self,sql):
        self.mycursor.execute(sql)
        self.mydb.commit()
        print("DONE..")
        
    #execution of query and retrieving
    def retrive_sql(self,sql):
        self.mycursor.execute(sql)
        data = self.mycursor.fetchall()
        return data
    
    #execution of query and retrieving many at once
    def retrive_many(self,val):
        self.mycursor.execute(sql)
        data = sqlf.mycursor.fetchall()
        return data
    
    #For closing connection to DataBase 
    def closeDB(self):
        self.mydb.close()

    
        