import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', family = 'Malgun Gothic')
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'brokenLineExam'

filename = './../data/주요발생국가주간동향(4월2째주).csv'

data = pd.read_csv(filename, index_col='국가')
print(data.columns)
print('-'*30)
print(data)
print('-'*30)

chartdata = data['4월06일']
print(chartdata)
print('-'*30)

YTICKS_INTERVAL = 50000     # y축 눈금 간격
maxlim = (int(chartdata.max() / YTICKS_INTERVAL) + 1) * YTICKS_INTERVAL

values = np.arange(0, maxlim + 1, YTICKS_INTERVAL)
plt.yticks(values, ['%s' % format(val, ',') for val in values])

plt.xlabel('국가명')
plt.ylabel('발생 건수')
plt.grid(True)
plt.title('4월 6일 코로나 발생 건수')

# color는 선의 색상, linestyle은 선의 유형, marker는 표시할 기호
plt.plot(chartdata, color='blue', linestyle='solid', marker='o')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2)
plt.savefig(savefile)
print(savefile + '파일을 저장')

########################################################################
COUNTRY = ['스페인', '프랑스', '독일', '중국', '영국', '이란']
WHEN = ['4월06일', '4월07일', '4월08일', '4월09일', '4월10일']
chartdata = data.loc[COUNTRY, WHEN]
chartdata = chartdata.T
print(chartdata)

chartdata.plot(title = 'some', figsize=(10, 6), legend=True, marker ='o', rot=0)

plt.xlabel('일자')
plt.ylabel('국가명')
plt.title('일자별 국가명 꺾은 선')
plt.grid(True)

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2)
plt.savefig(savefile)
print(savefile + '파일을 저장')

###############################################################################
tipsfile = './../data/tips.csv'
myframe=pd.read_csv(tipsfile, index_col=0)
print(myframe.describe())

data_bill=myframe.loc[:, ['total_bill']]
data_tip=myframe.loc[:, ['tip']]

xrange = range(len(myframe))

fig, ax1 = plt.subplots()
ax1.set_title('결제 금액과 Top(이중축)')

color = 'tab:red'
ax1.set_ylabel('결제 금액', color=color)
ax1.plot(xrange, data_bill, color=color)
ax1.tick_params(axis='y', labelcolor = color)

# 동일한 x축에 대하여 y축 복사본을 만든다.
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('팁(tip)', color=color)
ax2.plot(xrange, data_tip, color=color)
ax2.tick_params(axis='y', labelcolor = color)

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2)
plt.savefig(savefile)
print(savefile + '파일을 저장')