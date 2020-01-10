#這是能夠運用google api和Python 將googlemap上面的每個餐廳資料爬下來並且儲存到excel裡面
import googlemaps #匯入google
import pprint
import pandas as pd
import time

API_KEY = 'AIzaSyCy4uxDR3u-V26WWTb6VNe7lm7ub-HBRrY' #把 API KEY 放進去(需要上網申請)

# Define our client
gmaps  = googlemaps.Client(key = API_KEY)

ids = [] 
cities = ["臺北市","新北市","基隆市"] #指定其中三個城市

for city in cities:
    results = []
    geocode_result = gmaps.geocode(city)
    loc = geocode_result[0]['geometry']['location']
    query_result = gmaps.places_nearby(keyword="餐廳",location=loc, radius=10000)
    results.extend(query_result['results'])
    while query_result.get('next_page_token'):
        time.sleep(2)
        query_result = gmaps.places_nearby(page_token=query_result['next_page_token'])
        results.extend(query_result['results'])    
    print("找到以"+city+"為中心半徑10000公尺的寵物店家數量(google mapi api上限提供60間): "+str(len(results)))
    for place in results:
        ids.append(place['place_id'])
        
stores_info = []
# 去除重複id
ids = list(set(ids)) 
for id in ids:
    stores_info.append(gmaps.place(place_id=id, language='zh-TW')['result'])
    
output = pd.DataFrame.from_dict(stores_info)

output.to_excel('D:/Desktop/Science/restaurant.xlsx',index = False)
