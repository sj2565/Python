import time, datetime, ssl
import urllib.request
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver

# 모든 치킨 매장들을 위한 유틸리티 클래스 정의
class ChickenStore():
    # self는 객체 자신을 의미하는 특수 키워드
    def __init__(self, brandName, url):
        #print('생성자 호출됨')
        self.brandName = brandName
        self.url = url
        #print('브랜드 이름 : ', self.brandName)
        #print('웹 주소 : ', self.url)

        self.mycolumns = ['brand', 'store', 'sido', 'gungu', 'address', 'phone']

        if self.brandName != 'goobne':
            self.soup = self.get_request_url()
            self.driver = None
        else :
            filepath = 'c:/chromedriver'
            self.soup = None
            self.driver = webdriver.Chrome(filepath)
            self.driver.get(self.url)

    def get_request_url(self):
        request = urllib.request.Request(self.url)
        try:
            context = ssl._create_unverified_context()
            response = urllib.request.urlopen(request, context = context)
            if response.getcode() == 200: # http 응답 코드가 200이면 success를 의미
                if self.brandName != 'pelicana' :
                    return response.read().decode('UTF-8')
                else:
                    return response
        except Exception as err:
            print(err)  # err은 예외 객체
            now = datetime.datetime.now()   # 현재 시각
            print('[%s] error for url %s' %(now, self.url))
            return None # None은 실패 또는 부정적인 의미 보통 사용됨

    def getSoup(self):
        if self.soup == None:
            return None
        else :
            return BeautifulSoup(self.soup, 'html.parser')

    def save2Csv(self, result):
        data = pd.DataFrame(result, columns=self.mycolumns)
        data.to_csv(self.brandName + '.csv', encoding='UTF-8', index=False)
        print(self.brandName + '.csv' + ' 파일로 저장되었습니다.')

    def getWebDriver(self, cmdJavaScript):
        # cmdJavaScript : 문자열로 구성된 자바 스크립트 명령어
        #print(cmdJavaScript)
        self.driver.execute_script(cmdJavaScript) # 자바스크립트 실행은 execute_script
        wait = 5
        time.sleep(wait)
        # page_source : html 코드 내용
        mypage = self.driver.page_source

        return BeautifulSoup(mypage, 'html.parser')

