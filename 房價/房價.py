import requests
from bs4 import BeautifulSoup
#載入所有套件
a=0
for i in range(0,10): #迴圈，可以爬取10頁
    url = ('http://buy.sinyi.com.tw/list/%E5%8F%B0%E5%8C%97-keyword/{}.html').format(i)
    html = requests.get(url)
    sp = BeautifulSoup(html.content, 'html.parser')
    data1 = sp.select(".LongInfoCard_Type_Left")
    data2 = sp.select(".LongInfoCard_Type_Right")
    for n in range(0,len(data1)):
        print(data1[n].find('div',{'class':'LongInfoCard_Type_Name'}).text.strip()) #名稱
        print(data1[n].find('div',{'class':'LongInfoCard_Type_Address'}).text.strip()) #地址 
        print(data1[n].find('div',{'class':'LongInfoCard_Type_HouseInfo'}).text.strip(),'建坪     ',end="")
        print(data2[n].find('span',{'style':"font-size:1.75em;font-weight:500;color:#dd2525"}).text.strip(),'萬') #房價
        
        
        print('============================')

    
