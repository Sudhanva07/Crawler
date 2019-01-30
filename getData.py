import bs4
import requests

class obtainData:
#     def __init__(self):
#         self.link = ""
#         self.data = list
        
    def get_data(self,link):
#         self.link = link
        data_to_send  = []
        req6 = requests.get(link)
        soup6 = bs4.BeautifulSoup(req6.text,"html.parser")
        
        data9 = soup6.find("div",attrs={"class","gsc_col-xs-12 gsc_col-sm-12 gsc_col-md-7 gsc_col-lg-7 overviewdetail"})
        data_to_send.append(data9.h1.get_text())

        data10 = data9.find("div",attrs={"class","price"})
        if data10 == None:
            data_to_send.append("varient Experied")
        else:
            price = data10.get_text().split('*')
            data_to_send.append(price[0])

        data6 = soup6.find_all("div",attrs={"data-id","Overview"})
        data7 = soup6.find("td",text="Fuel Type").parent
        data8 = data7.parent
        for dat in data8:
            data_to_send.append(dat.span.get_text())
        
        data9 = soup6.find("td",text="City Mileage")
        if data9 == None:
            data_to_send.insert(3,"None") 
#         print(soup6.find("td",text="City Mileage"))

        
        return data_to_send
