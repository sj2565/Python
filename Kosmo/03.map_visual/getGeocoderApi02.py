# 보정된 치킨 매방 정보 중에서 특정 지역의 특정 브랜드에 대한 목록을 지도에 그려준다.
import folium

url_header = 'https://dapi.kakao.com/v2/local/search/address.json?query='
api_key = '6701424d89703102c105e73ee0a1d216'
header = {'Authorization': 'KakaoAK ' + api_key}

import requests

def getGeocoder(address):
    url = url_header + address
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        try:
            mydict = response.json()
            print(type(mydict))
            print(mydict)
            latitude = mydict['documents'][0]['address']['y']
            longitude = mydict['documents'][0]['address']['x']
            result = latitude, longitude
        except Exception as err:
            return None     # 자바의 Null과 유사
    else:
        errmsg = 'error [' +str(response.status_code) + ']'
        print(errmsg)
        return None

    return result
# end def

brand_dict = {'cheogajip':'처가집' ,'goobne':'굽네' ,'nene':'네네' ,'pelicana':'페리카나'}
brand_color = {'cheogajip':'red' ,'goobne':'green' ,'nene':'blue' ,'pelicana':'yellow'}

def makeMap(brand, store, geoInfo):
    # 브랜드 이름(brand), 상호(store), 위도 경도 튜플(geoInfo)
    shopinfo = store + '(' + brand_dict[brand] + ')'     # 가게이름(브랜드)
    mycolor = brand_color[brand]
    latitude, longitude = float(geoInfo[0]), float(geoInfo[1])

    marker = folium.Marker([latitude, longitude], popup=shopinfo, \
                           icon=folium.Icon(color=mycolor, icon='info-sign')).add_to(mapObject)

# address_latlng = getGeocoder()

# 지도의 기준점
mylatitude = 37.56
mylongitude = 126.92
mapObject = folium.Map(location=[mylatitude, mylongitude], zoom_start=13)   # mapObject는 지도 객체

import pandas as pd

pd.options.display.max_columns = 1000
pd.options.display.max_rows = 100

csv_file = './../02.crawling/allStoreModified.csv'
myframe = pd.read_csv(csv_file, index_col=0, encoding='utf-8')
#print(myframe.head())

# '서대문구'의 '처가집'과 '네네' 매장에 대하여 지도를 그려본다.
where = '서대문구'
brandName = 'goobne'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName
mydata01 = myframe.loc[condition1 & condition2]
#print(mydata01)

brandName = 'nene'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName
mydata02 = myframe.loc[condition1 & condition2]
#print(mydata02)

mylist = []
mylist.append(mydata01)
mylist.append(mydata02)

mapData = pd.concat(mylist, axis=0)
print(mapData)

# mapData = ''
# sido = '제주특별자치도'
# condition1 = myframe['sido'] == sido
# mapData = myframe.loc[condition1]

ok, notok = 0, 0    # 지오 코딩 성공, 실패 회수
for idx in range(len(mapData)):
    brand = mapData.iloc[idx]['brand']
    store = mapData.iloc[idx]['store']
    address = mapData.iloc[idx]['address']
    geoInfo = getGeocoder(address)

    if geoInfo == None:
        print('Not Okay!!! : ' +address)
        notok += 1
    else:
        print('Okay~ : ' +brand + ' ' +address)
        ok += 1
        makeMap(brand, store, geoInfo)
    print('-' *30)
# end for

total = ok + notok
print('total : ', total)
print('ok : ', ok)
print('notok : ', notok)

# latitude = address_latlng[0]    # 위도
# longitude = address_latlng[1]   # 경도

filename = 'map_graph.html'
mapObject.save(filename)
print(filename + '파일 저장됨')