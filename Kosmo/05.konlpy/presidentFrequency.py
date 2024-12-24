'''
대통령 신년 연설문을 형태소 분석하여 워드 클라우드를 그려 본다.
빈도 수가 1이상이고, 2글자 이상의 명사들만 추린다.

관련 라이브러리
nltk : National Language Toolkit
pip install nltk

konlpy(코앤엘파이) : 한글 형태소 분석기 중의 하나
한글 형태소 분석을 위한 py코모란
이외에도 한나눔, 꼬꼬마, 트위터(Okt)
pip install PyKomoran
'''
import numpy as np
from PIL import Image # python image library
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import ImageColorGenerator

class Visualization :
    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.worddict = dict(wordlist)

    def makeWordCloud(self):
        alice_color_file = './../04.wordcloud/alice_color.png'
        alice_colring = np.array(Image.open(alice_color_file))
        fontpath = 'malgun.ttf'     # 폰트

        # relative_scaling : 상대적인 단어의 크기를 지정한다. 0.5가 적당
        wordcloud = WordCloud(font_path=fontpath, mask=alice_colring, \
                              relative_scaling=0.2, background_color='lightblue')

        wordcloud = wordcloud.generate_from_frequencies(self.worddict)

        image_colors = ImageColorGenerator(alice_colring)
        newwc = wordcloud.recolor(color_func=image_colors, random_state=42)

        #plt.imshow(wordcloud)
        plt.imshow(newwc)

        plt.axis('off')
        filename = 'myWordCloud.png'
        plt.savefig(filename)
        print(filename + '파일 저장됨')
    # end def makeWordCloud(self):

filename = '문재인대통령신년사.txt'
ko_con_text = open(filename, encoding='utf-8').read()

from PyKomoran import Komoran
komo = Komoran('STABLE')

# 사용자 정의 사전을 셋팅
# 파일에 사용자가 등록하고자하는 내용을 기록해 둔다.
komo.set_user_dic('user_dic.txt')

# nouns 함수는 명사만 추출
tokens_ko = komo.nouns(ko_con_text)
#print(tokens_ko)
#print('-' * 30)

stop_word_file = 'stopword.txt'     # 불용어 파일
stop_file = open(stop_word_file, 'rt', encoding='utf-8')
stop_word = [word.strip() for word in stop_file.readlines()]     # readlines : 한 줄 씩 읽기
#print(stop_word)    # 불용어 목록

tokens_ko = [each_word for each_word in tokens_ko if each_word not in stop_word]
#print(len(tokens_ko))

import nltk
ko = nltk.Text(tokens=tokens_ko)
# most_common(n) 함수는 가장 빈도가 큰 n개를 골라내 준다.
print(ko.vocab().most_common(300))

data = ko.vocab().most_common(300)

wordlist = list()   # 튜플(단어, 빈도수)를 저장할 리스트

for word, count in data :
    if(count >= 1 and len(word) >= 2):
        wordlist.append((word, count))

visual = Visualization(wordlist)
visual.makeWordCloud()
# visual.makeMakeBarChart()
print('끝')