import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font', family='Malgun Gothic')

cnt, PNG, UNDERBAR = 0, 'png', '-'
CHART_NAME = 'barChartExam'

filename = './../data/tips.csv'
tips = pd.read_csv(filename, encoding='utf-8', index_col=0)
print(tips.head())
print('-' *30)

#print(tips['total_bill'].unique())
#print(tips['smoker'].unique())

# 히스토그램 : 연속성 데이터의 개략적인 분포를 파악하고자 할 때 요긴하게 사용됨

x = tips['total_bill']
print(type(x))

fig, ax = plt.subplots()    # 1행 1열

num_bins = 30   # 계급의 개수, 많을수록 촘촘해짐
n, bins, patches = ax.hist(x, num_bins, density=True)   # density : y좌표 수치 변경됨
ax.set_title('지불 금액의 히스토그램')
ax.set_xlabel('Frequency')
ax.set_ylabel('Total Bill')

import numpy as np
mu = x.mean()   # 평균
sigma = x.std() # 표준 편차

y = ((1/ (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) **2 ))
ax.plot(bins, y, '--')

fig.tight_layout()

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2)
plt.savefig(savefile)
print(savefile + '파일 저장')

###########################################################################
humanfile = './../data/human_height.csv'
human = pd.read_csv(humanfile, encoding='utf-8')
print(human.head())
print('-' * 30)

fig, axes = plt.subplots(nrows=1, ncols=2)
giant = human['giant']
dwarf = human['dwarf']

axes[0].hist(giant, range=(210, 290), bins=20, alpha = 0.6)
axes[1].hist(dwarf, range=(100, 180), bins=20, alpha = 0.6)

axes[0].set_title('거인국의 키')
axes[1].set_title('소인국의 키')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2)
plt.savefig(savefile)
print(savefile + '파일 저장')

#########################################################################

fig, axes = plt.subplots()
man = human['man']
woman = human['woman']

x = np.array((man, woman)).T
print(x.shape)  # 형상 : 몇 행 몇 열

axes.hist(x, bins=num_bins, density = False, histtype='bar', stacked=True)
axes.set_title('누적 히스토그램')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2)
plt.savefig(savefile)
print(savefile + '파일 저장')