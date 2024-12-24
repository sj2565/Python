import pandas as pd
import numpy as np

# 매장 정보들에 대한 보정 작업을 수행하는 클래스
class ChickenCorreciton():
    myencoding = 'utf-8'

    def __init__(self, workfile):        # init : 생성자
        print('생성자 호출됨')
        self.workfile = workfile         # self. : 인스턴스 변수
        self.myframe = pd.read_csv(self.workfile, encoding=self.myencoding, index_col=0)
        #print(self.myframe.info())
        print(len(self.myframe)) # 행 개수
        print('-' * 40)
        #print(self.myframe.head())

        self.correctionSido()
        self.correctionGungu()
        self.showMergeResult()
        self.correctionAddress()

        filename = 'allStoreModified.csv'
        self.myframe.to_csv('allStoreModified.csv', encoding=self.myencoding)
        print(filename + '파일 저장됨')

    def correctionSido(self):
        # 실제 매장이 아닌 데이터는 분석 대상에서 제외
        self.myframe = self.myframe[self.myframe['store'] != 'CNTTEST']     # pelicana 매장
        self.myframe = self.myframe[self.myframe['sido'] != '테스트']        # pelicana 매장
        #print(len(self.myframe))

        #print('before sido')    # distinct
        #print(np.sort(self.myframe['sido'].unique()))   # 중복된 데이터는 unique를 사용해서 제거

        # 보정작업
        # 파일을 읽어 들여서 사전 데이터를 만든다.
        # 사전을 이용하여 시도 데이터를 보정한다.
        sidofile = open('sido_correction.txt', 'r', encoding=self.myencoding)     # 읽기위해 r
        # readlines() 함수는 모든 행을 읽어서 list 형태로 만들어 준다.
        linelists = sidofile.readlines()
        #print(linelists)

        sido_dict = {}
        for oneline in linelists:
            mydata = oneline.replace('\n', '').split(':')
            sido_dict[mydata[0]]=mydata[1]

        #print(sido_dict)

        # apply 함수는 어떠한 수식이나 함수등을 이용하여 값을 변형시키는 함수
        # sido_dict.get(data, data)에서 1번째 data는 찾고자 하는 값, 2번째 데이터는 없을 경우 default 값
        self.myframe.sido = self.myframe.sido.apply(lambda data: sido_dict.get(data, data))

        #print('after sido')
        #print(np.sort(self.myframe['sido'].unique()))

    def correctionGungu(self):
        #('before gungu')
        #print(self.myframe['gungu'].unique())

        gungufile = open('gungu_correction.txt', 'r', encoding=self.myencoding)
        linelists = gungufile.readlines()

        gungu_dict = {}
        for oneline in linelists:
            mydata = oneline.replace('\n', '').split(':')
            gungu_dict[mydata[0]]=mydata[1]
            
        # \ 기호는 문장이 길 떄 한줄이라는 의미로 사용
        self.myframe.gungu = \
            self.myframe.gungu.apply(lambda data: gungu_dict.get(data, data))
            
        #print('after gungu')
        #print(self.myframe['gungu'].unique())

    def showMergeResult(self):
        # 전체 매장 csv와 표준 행정 구역 csv를 비교하여 표준화로 데이터 변형하기
        district = pd.read_csv('district.csv', encoding=self.myencoding)

        mergedData = pd.merge(self.myframe, district, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)

        # _merge 컬럼 : both, left_only, right_only
        # 우리는 표준 행정 주소 체계를 안 따르는 left_only 항A목을 찾으면 된다.
        #print(mergedData.head(10))
        result = mergedData.query('_merge=="left_only"')
        #print('좌측에만 있는 데이터')
        #print(result[['sido', 'gungu', 'address']])

    def correctionAddress(self):    # 주소지 보정하기
        try:
            for idx in range(len(self.myframe)):
                #print(self.myframe.iloc[idx])
                imsiseries = self.myframe.iloc[idx]
                addSplit = imsiseries['address'].split(' ')[2:]
                imsiAddress = [imsiseries['sido'], imsiseries['gungu']]
                imsiAddress = imsiAddress + addSplit
                self.myframe.iloc[idx]['address'] = ' '.join(imsiAddress)

        except TypeError as err:
            pass

# 모든 brand 매장 정보를 담고 있는 파일
filename = 'allstore.csv'
chknStore = ChickenCorreciton(filename)

print('끝')