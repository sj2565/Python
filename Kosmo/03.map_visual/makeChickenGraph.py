'''
보정된 치킨 매장 파일을 사용하여 매장별 집계를 구해 본다.
집계 데이터를 사용하여 파이, 막대 그래프를 그려 본다.
matplotlib는 데이터 시각화 라이브러리
    pip install matplotlib
'''
import pandas as pd
csvfile = './../02.crawling/allStoreModified.csv'
myframe = pd.read_csv(csvfile, index_col=0, encoding='utf-8')
print(myframe.head())

mycolor = ['r','g','b','m']
brand_dict = {'cheogajip':'처가집', 'goobne':'굽네', 'nene':'네네', 'pelicana':'페리카나'}

# (['brand'])별로 그룹화 하고 ['brand']에 대하여 연산을 수행
mygrouping = myframe.groupby(['brand'])['brand']

# count(), mean(), sum(), max(), min()
chartData = mygrouping.count()

newindex = [brand_dict[idx] for idx in chartData.index]
chartData.index = newindex
print((chartData))
print(type(chartData))

import matplotlib.pyplot as plt
# 글꼴을 맑은 고딕체로 변경
plt.rcParams['font.family'] = 'Malgun Gothic'

plt.figure()

chartData.plot(kind='pie', legend=False, autopct='%1.2f%%', colors=mycolor)

filename = 'makeChickenGraph01.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일이 저장되었다')
plt.show() # 차트를 보여 준다.

plt.figure()

# rot=30(각도)는 글자의 기울임 정도
chartData.plot(kind='barh', title='브랜드 별 총 매장수', legend=False, color=mycolor)

filename = 'makeChickenGraph02.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일이 저장되었다')

seoulframe = myframe.loc[myframe['sido'] == '서울특별시']
kkframe = myframe.loc[myframe['sido'] == '경기도']

newframe=pd.concat([seoulframe, kkframe], axis=0)
print(newframe.info())

mygrouping = newframe.groupby(['brand', 'sido'])['brand']
chartData = mygrouping.count()
print(chartData)

plt.figure()
chartData.plot(kind='bar', title='매장별 지역별 점포 갯수',  legend=True)
filename = 'makeChickenGraph03.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일이 저장되었다')