'''
BeautifulSoup은 정적인 웹페이지만 크롤링이 가능하다.
자바 스크립트를 사용하는 동적인 페이지는 크롤링이 불가능하다.
동적인 페이지에 대한 처리는 셀레니엄(selenium)으로 처리 가능하다.
해당 브라우저를 동작 시키기 위한 드라이버가 필요하다.
준비물
    pip install selenium
    크롬 관련 드라이브 파일을 다운 받아서 저장
    https://sites.google.com/a/chromium.org/chromedriver/downloads
    드라이브 c:\에 파일 chromedriver.exe를 저장해 둔다.
'''
from itertools import count
from ChickenUtil import ChickenStore

brandName = 'goobne' # 브랜드 이름
base_url = 'https://www.goobne.co.kr/store/search_store.jsp'   # 접속 url

def getData():
    savedData = []
    chknStore = ChickenStore(brandName, base_url)

    bEndPage = True  # 마지막 페이지이면 True가 된다.

    for page_idx in count():
        print('%s번째 페이지가 호출됨' %str(page_idx + 1))
        bEndPage = False

        cmdJavaScript = "javascript:store.getList('%s')" %str(page_idx + 1)
        soup = chknStore.getWebDriver(cmdJavaScript)
        print(type(soup))

        store_list = soup.find('tbody', attrs={'id':'store_list'})
        mytrlists = store_list.findAll('tr')
        #print('매장 개수 : %d' %len(mytrlists))

        for onestore in mytrlists:
            mytdlists = onestore.findAll('td')
            #print('a' * 50)
            #print(mytdlists)

            if len(mytdlists) > 1 :
                store = onestore.select_one('td:nth-of-type(1)').get_text(strip=True) # a 태그가 없으므로 get_text쓰기
                phone = onestore.select_one('td:nth-of-type(2)').a.string
                address = onestore.select_one('td:nth-of-type(3)').a.string
                imsi = str(address).split(' ')
                sido = imsi[0]
                gungu = imsi[1]

                #print('b' * 50)
                #print(store + '/' + sido +  '/' + gungu +  '/' + address + '/' + phone)

                savedData.append([brandName, store, sido, gungu, address, phone])
            else : # 마지막 페이지는 <td> 태그가 1개 이다
                bEndPage = True
                break
        # end inner for

        if bEndPage == True:
            break

    # end outer for

    chknStore.save2Csv(savedData)
print(brandName + '매장 크롤링 시작')
getData()
print(brandName + '매장 크롤링 끝')