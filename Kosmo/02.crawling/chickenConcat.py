'''
이미 수집한 치킨 매장들의 파일을 하나의 파일에 통합한다.
판다스
read_cav(0 함수 : csv 파일 읽기
concat() 함수 : csv 파일을 수직 방향으로 병합해주는 함수
'''
from pandas import DataFrame

newframe = DataFrame()  # 데이터를 합치고자 하는 데이터 프레임

chickenList = ['cheogajip', 'goobne', 'nene', 'pelicana']
#chickenList = ['cheogajip']
myencoding = 'utf-8'

import pandas as pd

for onestore in chickenList:
    filename = onestore + '.csv'
    #print(filename)
    # index_col=0 : 0번째 컬럼을 색인으로 사용하겠다.
    #myframe = pd.read_csv(filename, index_col=0, encoding=myencoding)
    myframe = pd.read_csv(filename, encoding=myencoding)
    # print(myframe.head())   # 앞 5행만 보기

    # 모든 데이터를 newframe 변수에 누적시킨다.
    newframe = pd.concat([newframe, myframe], axis=0, ignore_index=True)

# info() 해당 데이터 프레임의 정보를 간략하게 보여 준다.
# 판다스에서 str을 object라고 표현한다.
print(newframe.info())
print('finished')

totalfile = 'allstore.csv'
newframe.to_csv(totalfile, encoding=myencoding)
print(totalfile + '파일이 저장되었다.')