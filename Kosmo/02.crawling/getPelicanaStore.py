from ChickenUtil import ChickenStore
from itertools import count

brandName = 'pelicana' # 브랜드 이름
base_url = 'https://pelicana.co.kr/store/stroe_search.html'   # 접속 url

def getData():
    savedData = []

    for page_idx in count():
        url = base_url + '?page=' +str(page_idx + 1)
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()
        #print(type(soup))

        mytable = soup.find('table', attrs={'class':'table mt20'})
        mytbody = mytable.find('tbody')

        shopExists = False  # 매장 정보가 없다고 가정

        for mytr in mytbody.findAll('tr'):
            shopExists = True
            #print(mytr.strings)
            mylist = list(mytr.strings)
            #print(mylist)

            store = mylist[1]
            address = mylist[3]
            imsiphone = mylist[5]

            phone = imsiphone.strip()

            #print("[" + store + "]")
            #print("[" + address + "]")
            #print("[" + imsiphone + "]")
            #print('-' * 30)

            if len(address) > 2 :
                imsi = address.split()
                sido = imsi[0]
                gungu = imsi[1]

                mydata = [brandName, store, sido, gungu, address, phone]
                savedData.append(mydata)

        #print(savedData)

        if shopExists == False:
            # 더 이상 존재하지 않으므로 파일로 저장하기
            chknStore.save2Csv(savedData)
            break

print(brandName + '매장 크롤링 시작')
getData()
print(brandName + '매장 크롤링 끝')