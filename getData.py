import bs4
import requests


        



def get_data(link):

    data_to_send  = []
    data_to_get =[]
    req6 = requests.get(link)
    soup6 = bs4.BeautifulSoup(req6.text,"html.parser")
    #Car NAme
    data9 = soup6.find("div",attrs={"class","gsc_col-xs-12 gsc_col-sm-12 gsc_col-md-7 gsc_col-lg-7 overviewdetail"})
    data_to_send.append(data9.h1.get_text())

    #Car Price
    data10 = data9.find("div",attrs={"class","price"})
    if data10 == None:
        data_to_send.append("varient Experied")
    else:
        price = data10.get_text().split('*')
        data_to_send.append(price[0])

    #---------------car details----------------------------------

    data7 = soup6.find_all("table",attrs={"class","keyfeature"})
    print(len(data7))
    if len(data7) == 13:
        data_in_td = data7[2:7]
        data_in_single = data7[7:-1]
    elif len(data7) == 12:
        data_in_td = data7[1:6]
        data_in_single = data7[6:-1]


    for dat in data_in_td:
        data = dat.find_all("td")
        for tdata in data:
            data_to_get.append(tdata.get_text())
    #                 data = 1
    for dat in data_in_single:
        daa = dat.find_all("i")
        for da in daa:
            data_to_get.append(da.get_text()[0:1000])
    #                 dara =1 
    data_left = data_to_get[::2]
    data_right = data_to_get[1::2]



    return data_to_send,data_left,data_right


#         return data_to_send



