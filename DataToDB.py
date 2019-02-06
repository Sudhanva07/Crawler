from Import_to_DB import *
from mysqlDB import *

#sql connection from file mysqlDB
a = sqlDB("localhost","root","","car_links")

#Query to get links which have status 0
sql = "SELECT links from links where status = 0"
links = a.retrive_sql(sql)          #retrive_sql(sql) function of mysqlDB to execute and reteieve 
a.closeDB()                         #close connection to allow connection for Import_DB
for link in links:
    Import_DB(link[0])              #Import_Db allows to send data to Database