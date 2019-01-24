import bs4
import requests

class obtainData:
#     def __init__(self):
#         self.link = ""
#         self.data = list
        
    def get_data(link):
#         self.link = link
        req = requests.get(link)
        data_to_send  = []
        soup = bs4.BeautifulSoup(req.text,"html.parser")
        data = soup.find("div",attrs={"class","gsc_col-xs-12 gsc_col-sm-12 gsc_col-md-7 gsc_col-lg-7 overviewdetail"})
        data_to_send.append(data.h1.get_text())
        
        
        data2 = data.find("div",attrs={"class","price"})
        price = data2.get_text().split('*')
        data_to_send.append(price[0])
        
        
        data = soup.find_all("td",attrs={"class","gsc_col-xs-12 textHold"})
        for dat in data:
            data_to_send.append(dat.get_text())
#             print(type(dat.get_text()))
        
        return data_to_send
