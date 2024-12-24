#naverCartoon.py
'''
네이버 카툰 페이지를 위한 요일 이름 폴더를 생성 (os모듈)

사용 모듈
os모듈은 파일 및 폴더에 대한 생성/수정/삭제 등의 작업을 도와주는 외부 모듈

구현 기술
예외처리,
'''
import os   #os모듈을 사용하겠다.

weekday_dict = {'mon':'월요일', 'tue':'화요일', 'wed':'수요일', 'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 'sun':'일요일'}

myfolder = 'c:\\imsi\\'

try :
    if not os.path.exists(myfolder) :       #임시폴더 생성
        os.mkdir(myfolder)                  #mkdir이 폴더 생성한 것

    for mydir in weekday_dict.values() :
        mypath = myfolder + mydir
        #print(mypath)
        if os.path.exists(mypath) :
            pass
        else : # 월요일 부터 일요일까지 폴더 생성
            os.mkdir(mypath)

except FileExistsError as err :
    pass                                    #오류를 무시하고 넘김
'''
크롤링) 인터넷 소스를 파악하여 필요한 데이터를 읽어 들인다 동작
크롤링을 하기 위해서 외부 라이브러리 Beautiful soup을 설치해야 한다.
cmd창에서 pip install beautifulsoup4 명령어로 설치를 하면 된다.

그리고 url을 다루기 위한 urllib 라이브러리와 같이 많이 사용된다.

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

myparser = 'html.parser'
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
response = urlopen(myurl)
soup = BeautifulSoup(response, myparser)
#print(type(soup))
#print(soup)

'''            
파이썬에서 파일을 읽거나 쓰기 위해서는 open() 함수를 사용하면 된다.
크게 텍스트와 이진 파일 형식으로 저장 가능하다.
모드) r(읽기), w(쓰기), t(문자), b(바이너리) 
'''

def saveFile(mysrc, myweekday, mytitle):    # def : 함수만들기
    image_file = urlopen(mysrc)
    filename = myfolder + myweekday + '\\' + mytitle + '.jpg'
    #print(filename) # 저장될 파일 경로와 이름
    myfile = open(filename, mode='wb')
    myfile.write(image_file.read())

mylist = [] # 데이터를 저장할 리스트

# div 태그 중에서 'class' 속성이 'thumb'인 항목을 찾아 준다.
mytarget = soup.find_all('div', attrs={'class':'thumb'})
print('카툰 총 개수 : %d' %len(mytarget))
for abcd in mytarget :
    myhref = abcd.find('a').attrs['href']
    myhref = myhref.replace('/webtoon/list?', '')
    #print(myhref)
    result = myhref.split('&')  # split 반환 타입은 문자열로 쪼개진 리스트
    #print(result)
    mytitleid = result[0].split('=')[1]
    myweekday = result[1].split('=')[1]

    myweekday = weekday_dict[myweekday]

    #print(mytitleid + '/' + myweekday)

    imgtag = abcd.find('img')
    mysrc = imgtag.attrs['src']
    mytitle = imgtag.attrs['title'].strip() # strip() : 공백 제거
    mytitle = mytitle.replace('?', '').replace(':', '')
    #print(mytitle + '/' + mysrc)

    mytuple = tuple([mytitleid, myweekday, mytitle, mysrc])
    mylist.append(mytuple)

    saveFile(mysrc, myweekday, mytitle) # 위에 쓰였던 saveFile함수 호출하기

#print(mylist[0:2])
'''
csv : comma separator value 콤마로 구분되어 있는 텍스트 파일
엑셀 또는 메모장으로 볼 수 있음
파이썬에서는 csv라는 모듈로 처리하거나 판다스로 처리할 수 있다.

'''
'''
판다스는 데이터 분석과 조작 등을 위한 라이브러리이다.
설치는 pip install pandas 명령어로 가능하다.

DataFrame은 판다스에서 가장 많이 사용되는 2차원 형태의 표
'''
from pandas import DataFrame

myframe = DataFrame(mylist, columns=['타이틀 번호', '요일', '제목', '링크'])
filename = 'cartoon.csv'
myframe.to_csv(filename, index=False)
print(filename + '파일로 저장됨')
print('finished')