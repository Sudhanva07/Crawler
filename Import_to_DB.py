from getData import *
from mysqlDB import * 

#import_DB function to send data to databse 
def Import_DB(link):
    print(link)
    a = sqlDB("localhost","root","","car_links")

    flag = 0
    car_name = ["Name","price"]
    name,left,right = get_data(link)

    [car_name.append(x) for x in left]
    [name.append(x) for x in right]
#     print(car_name)
#     print(name)
    for attr,val in zip(car_name,name):
        sql = "desc links"
        data = a.retrive_sql(sql)
        x = [i[0] for i in data]
        flag = 0
        val = val.replace("@","_").replace("'","").replace("/n","").replace(" ","")
        attr = attr.replace("(","_").replace(")","_").replace("'","").replace(" ","_").replace(".","")
        attr = attr.replace("-","_").replace("/","_or_").replace("&","and")

        for db_attr in x:
#             print(db_attr)
            if attr == db_attr :
                flag = 1
                break
            else:
                flag = 0
        print(flag)
        if flag == 0:
            create_table = "ALTER TABLE links ADD COLUMN %s VARCHAR(100) DEFAULT NULL"%(attr)
            a.execute_single(create_table)

        else:
            pass
        update_table = "UPDATE links set %s = '%s' where links='%s'"%(attr,val,link)
        a.execute_single(update_table)
        
    status = "UPDATE links set status = 1 where links='%s'"%(link)
    a.execute_single(status)
        