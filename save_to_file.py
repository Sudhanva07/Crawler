import csv
import os

def create_data_file(path):
    data = ['Name','Price','Milage','Engine','BHP','Transmission','Seats','ServiceCost']
    if not os.path.isfile(path):
        write_file(prj_name,data)
        
def write_file(path,data):
    with open(path,'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(data)
    csvFile.close
