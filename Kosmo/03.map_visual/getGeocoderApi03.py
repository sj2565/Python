# 특정 주소지에 대하여 카카오 api를 사용하여 위도와 경도를 추출한다.
# 해당 지오 코드 정보를 이용하여 지도에 표시해 본다.

address = '서울 마포구 신수동 451번지 세양청마루아파트 상가 101호'
url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address

api_key = '6701424d89703102c105e73ee0a1d216'
header = {'Authorization': 'KakaoAK ' + api_key}

import requests

def getGeocoder():
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

address_latlng = getGeocoder()
latitude = address_latlng[0]    # 위도
longitude = address_latlng[1]   # 경도

#latitude = 37.505
#longitude = 126.762

print('주소지 : ', address)
print('위도 : ', latitude)
print('경도 : ', longitude)

import folium

shopinfo = '교촌 신수점'
# foli_map은 지도 객체
foli_map = folium.Map(location=[latitude, longitude], zoom_start=17)
myicon = folium.Icon(color='red', icon='info-sign')
folium.Marker([latitude, longitude], popup=shopinfo, icon=myicon).add_to(foli_map)

folium.CircleMarker([latitude, longitude], radius = 300, color='blue', fill_color = 'red',fill=False, popup=shopinfo).add_to(foli_map)

filename = 'my_map_graph.html'
foli_map.save(filename)
print(filename + '파일 저장됨')