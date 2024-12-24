# 스티브 잡스 워드 클라우드 만들기

filename = 'steve.txt'
myfile = open(filename, 'rt', encoding='utf-8')
text = myfile.read()    # read() 함수는 전체를 문자열로 읽어 들인다.
#print(text)

from wordcloud import WordCloud

wordcloud = WordCloud()     # 생성자 호출
wordcloud = wordcloud.generate(text)
# print(type(wordcloud))
# print('-' *30)

bindo = wordcloud.words_    # 단어들의 빈도 수
# print(type(bindo))
# print('-' *30)
#
# # 가장 많이 나온 단어에 대한 비율
# print(bindo)
# print('-' *30)

# 수치 비율이 가장 큰 것을 먼저 보여준다.
sortedData = sorted(bindo.items(), key=lambda x : x[1], reverse=True)
#print(sortedData)
#print('-' *30)

# 상위 10개만 추려서 막대 그래프로 나타내기
charData = sortedData[0:10]
xtick = []  # x축 눈금에 보여질 문구
chart = []  # 그려질 수치 데이터

for item in charData:
    xtick.append(item[0])
    chart.append(item[1])

mycolor=['r', 'g', 'b', 'y', 'm', 'c', '#FFF0F0' ,'#CCFFBB' ,'#05CCFF','#11CCFF']

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

plt.figure()
plt.bar(xtick, chart, color=mycolor)
plt.title('상위 빈도 Top 10')
filename = 'wordCloudEx01_01.png'
plt.savefig(filename)
print(filename + '파일이 생성됨')

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud)   # image show
plt.axis('off')
filename = 'wordCloudEx01_02.png'
plt.savefig(filename)
print(filename + '파일이 생성됨')
