import re # 정규 표현식을 위한 모듈
from ChickenUtil import ChickenStore

brandName = 'nene'  # 브랜드 이름
base_url = 'https://nenechicken.com/17_new/sub_shop01.asp'   # 접속 url

def getData():
    savedData = []  # csv 파일로 저장될 리스트

    for page_idx in range(1, 46+1):  # 차후 변경 요망
        url = base_url + '?page=%d' % (page_idx)
        #print(url)
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()

        tablelists = soup.findAll('table', attrs={'class':'shopTable'})
        print(len(tablelists))
        for onetable in tablelists:
            # select_one은 요소 1개를 찾는다.
            # .은 class 속성을 의미한다.
            store = onetable.select_one('.shopName').string
            #print(store)
            temp = onetable.select_one('.shopAdd').string
            if temp == None:
                continue    # 이후 코드를 무시하고, 다음 반복문(for문)으로 이동
            #print(temp)

            im_address = onetable.select_one('.shopMap')
            im_address = im_address.a['href']
            #print(im_address)
            
            # 가장 먼저 오는 숫자 부터 뒤쪽의 모든 문자들을 추출
            regex = '\d\S*' # 정규 표현식
            pattern = re.compile(regex) # 컴파일
            mymatch = pattern.search(im_address) # search 함수로 찾고

            # group() 함수는 조건에 맞는 문자를 뽑아 내고, replace() 함수로 치환한다.
            addr_suffix = mymatch.group().replace("');", '')
            #print('주소 접미사')
            #print(addr_suffix)

            address = temp + ' ' + addr_suffix
            #print(address)

            imsi = temp.split(' ')
            sido = imsi[0]
            gungu = imsi[1]

            phone = onetable.select_one('.tooltiptext').string

            mydata = [brandName, store, sido, gungu, address, phone]
            savedData.append(mydata)
        # end inner for
    # end outer for

    chknStore.save2Csv(savedData)

print(brandName + '매장 크롤링 시작')
getData()
print(brandName + '매장 크롤링 끝')