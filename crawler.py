import bs4
import requests
from mysqlDB import *

class crawler:
    def __init__(self,base_url):
        self.base_url = base_url
        
    def Initialize_crawler(self,link):
        url = self.base_url + link
        req = requests.get(url)
        soup = bs4.BeautifulSoup(req.text,"html.parser")
        return soup
    
    def level1(self,soup):
        links = []
        data = soup.find_all("li",attrs={"class","gsc_col-xs-4 gsc_col-sm-3 gsc_col-md-3 gsc_col-lg-2"})
        for dat in data:
            links.append(dat.find("a").attrs["href"])
        return links
    
    def level2(self,soup):
        links = []
        data2 = soup.find("section",attrs={"class"," gsc_row gsc_container_hold heading BrandPagelist marginTop20"}).find_all("h3")
        for dat in data2:
            links.append(dat.a.attrs['href'])
        return links
            
    def level3(self,soup):
        links = []
        data5 = soup.find("table",attrs={"class","allvariant contentHold"}).find_all("a")
        # print(data5)
        for dat in data5:
            links.append(dat.attrs['href'])
        return links

    
base_url = "https://www.cardekho.com"
base_link = "/newcars"

mysq = sqlDB("localhost","root","","car_links")
sql = """INSERT INTO links (links) VALUES (%s)"""
a = crawler(base_url)

level1_links = a.level1(a.Initialize_crawler(base_link))
for link in level1_links:
    b = crawler(base_url)
    level2_links = b.level2(b.Initialize_crawler(link))
#     print(level2_links)
    for link2 in level2_links:
        if link2 == None:
            pass
        else:
            c = crawler(base_url)
            level3_links = c.level3(c.Initialize_crawler(link2))
#             print(level3_links)
            for item in level3_links:
                link_to_save = base_url + item
                mysq.execute_val(sql,(link_to_save,))
     