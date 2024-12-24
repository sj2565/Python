# 척도 설문 조사) 1. 매우 그렇다 2. 그렇다 3. 보통이다 4. 그렇지 않다. 5 매우 그렇지 않다.
# 범주(카테고리) 형 척도 : 성별, 직업, 크기를 비교할 필요가 없다
# 막대, 파이

# 연속형 척도 : 키(height), 몸무게, 숫자의 비교가 의미 있다.
# 꺾은 선, 산점도, 박스 플롯, 히스토그램
cnt, PNG, UNDERBAR = 0, 'png', '-'
CHART_NAME = 'barChartExam'

filename = './../data/주요발생국가주간동향(4월2째주).csv'

import pandas as pd
# 국가 컬럼을 색인으로 사용
data = pd.read_csv(filename, index_col='국가')
print(data.columns)
print('-' *30)

print(data.head())
print('-'*30)

chartdata = data['4월06일']

print(chartdata)

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

def MakeBarChart01(x, y, color, xlabel, ylabel, title):
    plt.figure()
    plt.bar(x, y, color=color, alpha=0.7)   # alpha는 불투명도를 의미 0.0 ~ 1.0 사이의 값

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    #plt.grid(True)  # 배경에 줄 표시

    YTICKS_INTERVAL = 50000     # 수치에 따라 y축 눈금 크기가 달라진다
    maxlim = (int(y.max()/YTICKS_INTERVAL)+1) * YTICKS_INTERVAL
    print(maxlim)   # maxlim은 y축 눈금의 최대 값

    # np.arange는 파이썬의 range() 함수와 동일한 기능을 한다.
    values=np.arange(0, maxlim + 1, YTICKS_INTERVAL)
    plt.yticks(values, ['%s' % format(val, ',') for val in values])

    ratio = 100 * y / y.sum()
    print(ratio)

    plt.rc('font', size = 8)
    for idx in range(y.size):
        value = format(y[idx], ',') + '건'   # ex) 60건
        ratioval = '%.1f%%' %(ratio[idx])   # ex) ratio는 20.0%
        plt.text(x=idx, y=y[idx] + 1, s=value, horizontalalignment = 'center')
        plt.text(x=idx, y=y[idx] / 2, s=ratioval, horizontalalignment='center')
    
    meanval = y.mean()  # 평균 값
    print(meanval)
    print('-' * 30)

    average = '평균 %d건' %meanval
    plt.axhline(y=meanval, color='r', linewidth=1, linestyle='dashed')  # dashed : 점선
    plt.text(x=y.size-1, y=meanval + 200, s=average, horizontalalignment='center')

    global cnt
    cnt = cnt + 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2)   # zfill(2) -> 0으로 두자리를 채워라
    plt.savefig(savefile)
    print(savefile + '파일이 저장되었다.')

colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']
mycolor=colors[0:len(chartdata)]

MakeBarChart01(x=chartdata.index, y=chartdata, color=mycolor, xlabel='국가명', ylabel='발생건수', title='국가별 코로나 발생 건수')
##################################################################################################

def MakeBarChart02(chartdata, rotation, title, ylim=None, stacked=False, yticks_interval = 10000):
    plt.figure()
    chartdata.plot(kind='bar', rot=rotation, title=title, legend=True, stacked=stacked)

    plt.legend(loc='best')     # 범례의 위치는 스스로 판단하여 적절한 곳에 만들어 줘야 한다.

    if stacked == False:
        maxlim = (int(max(chartdata.max())/ yticks_interval) + 1 ) * yticks_interval
        values = np.arange(0, maxlim + 1, yticks_interval)
        plt.yticks(values, ['%s' %format(val, ',') for val in values])
    else :  # 누적 막대 그래프이면
        maxlim = (int(max(chartdata.max(axis=1)) / yticks_interval) + 1) * yticks_interval
        values = np.arange(0, maxlim + 1, yticks_interval)
        plt.yticks(values, ['%s' % format(val, ',') for val in values])

    if ylim != None :
        plt.ylim(ylim)  # y축 상하한 값

    global cnt
    cnt = cnt + 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2)  # zfill(2) -> 0으로 두자리를 채워라
    plt.savefig(savefile)
    print(savefile + '파일이 저장되었다.')

data=pd.read_csv(filename, index_col='국가')

COUNTRY = ['프랑스', '중국', '영국', '이란']
WHEN=['4월06일', '4월07일', '4월08일']
data = data.loc[COUNTRY, WHEN]
print(data)
print('-' * 30)

data.index.name='국가명'
data.columns.name='일자'

print(data)
print('-' *30)

#MakeBarChart02(chartdata=data, rotation=0, title='국가별 일별 발생 건수', stacked=True)
MakeBarChart02(chartdata=data, rotation=0, title='국가별 일별 발생 건수', ylim=[0, 100000])  # y좌표 수치
##################################################################################################
dataT = data.T  # 전치) 행과 열을 서로 바꿈
MakeBarChart02(chartdata=dataT, rotation=0, title='일별 국가별 발생 건수')
##################################################################################################
ymax = dataT.sum(axis=1)
ymaxlimit = ymax.max() + 10

MakeBarChart02(chartdata=data, rotation=0, stacked=True, title='국가별 일별 발생 건수(누적)', ylim=[0, ymaxlimit], yticks_interval=50000)

###########################################배껴온 소스#######################################################

data = pd.read_csv(filename, index_col='국가')

three = [item for item in data.index if item in ['프랑스', '영국', '중국']]
print(three)

data = data.loc[three]

print(data)
print('-' * 30)

column_names = data.columns.tolist()
print('column_names')
print(column_names)

# 국가별 numpy 배열을 저장하고 있는 사전
chartdata = {}

for row in data.index:
    # print(data.loc[row])
    # print(type(row))
    chartdata[row] = data.loc[row].values

print('chartdata')
print(chartdata)

def MakeBarChart03(chartdata, column_names):
    """
    Parameters
    ----------
    chartdata : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *column_names*.
    column_names : list of str
        The category labels.
    """
    labels = list(chartdata.keys())
    data = np.array(list(chartdata.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(column_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            ax.text(x, y, str(int(c)), ha='center', va='center',
                    color=text_color)
    ax.legend(ncol=len(column_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    global cnt
    cnt = cnt + 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2)
    plt.savefig(savefile, dpi=400)
    print(savefile + ' 파일이 저장되었습니다.')

    return fig, ax
# end def MakeBarChart03

MakeBarChart03(chartdata, column_names)

#########################################################################################
def MakeBarChart04(chartdata, suptitle):
    # fig : figure(도화지), axes[0]/axes[1]
    fig, axes = plt.subplots(nrows=2, ncols=1)  # 2행 1열

    chartdata.plot(kind='bar', ax=axes[0], rot=0, alpha=0.7)
    chartdata.plot(kind='barh', ax=axes[1], rot=0, alpha=0.7, color = 'm')

    fig.suptitle(suptitle)  # sup : super

    global cnt
    cnt = cnt + 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2)
    plt.savefig(savefile, dpi=400)
    print(savefile + ' 파일이 저장되었습니다.')

data = pd.read_csv(filename, index_col='국가')

only_usa = [item for item in data.index if item in ['미국']]
print(only_usa)
print('-' *30)

data = data.loc[only_usa].T
print(data)
print('-' *30)

MakeBarChart04(chartdata=data, suptitle='서버 플롯팅')

##########################################################################################
# 엑셀처럼 Table이 존재하는 Bar Chart 그리기
data = pd.read_csv(filename, index_col='국가')

print(data.columns)
print('-' * 30)

COUNTRY = ['스페인', '프랑스', '중국', '영국', '이란']
WHEN = ['4월06일', '4월07일', '4월08일', '4월09일', '4월10일']
data = data.loc[COUNTRY, WHEN]

print('data')
print(data)
print('-'*30)

# rows : 테이블에 보이는 행 색인 내용
rows = [x for x in data.index]
print('rows')
print(rows)
print('-'*30)

# columns : 테이블에 보이는 열 색인 내용
columns = [x for x in data.columns]
print('columns')
print(columns)
print('-'*30)

print('데이터 최대 값 :', max(data.max()))
print('-'*30)

n_rows = len(data) # 행 수
print('n_rows :', n_rows)
print('-'*30)

LEFT_MARGIN = 0.3
index = np.arange(len(columns)) + LEFT_MARGIN
print('index :', index)
print('-'*30)

bar_width = 1 - 2 * LEFT_MARGIN # 막대 그래프의 너비

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(columns))
print('y_offset :', y_offset)
print('-'*30)

# Plot bars and create text labels for the table
cell_text = [] # 표에 들어 가는 텍스트 내용
plt.figure()

for row in data.index:
    print('data[row]')
    chartdata = data.loc[row].tolist()
    print(chartdata)

    # bottom
    plt.bar(index, chartdata, bar_width, bottom=y_offset, label=row)

    # y_offset에는 열 단위로 누적된 값이 들어 갑니다.
    y_offset = y_offset + chartdata
    # y_offset = chartdata
    print('y_offset')
    print(y_offset)

    cell_text.append([format(x, ',') for x in chartdata])
    # cell_text.append([format(x, ',') for x in y_offset])
# end for

cell_text.reverse()
rows = [rows[idx] for idx in range(len(rows) - 1, -1, -1) ]

# Add a table at the bottom of the axes
print('cell_text : ', cell_text)
print('rows : ', rows)
# print('colors : ', colors)
print('columns : ', columns)
the_table = plt.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='bottom')

plt.legend(loc='best')
# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("발생 건수")

# values : y축의 눈금의 상한 값과 간격 지정하기
YTICKS_INTERVAL = 50000 # 단위 눈금 간격
maxlim = (int(y_offset.max()/YTICKS_INTERVAL)+1)*YTICKS_INTERVAL
print(maxlim)

values = np.arange(0, maxlim, YTICKS_INTERVAL)

plt.yticks(values, ['%s' % format(val, ',') for val in values])
plt.xticks([])
plt.title('테이블이 있는 막대 그래프')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2)
plt.savefig(savefile, dpi=400)
print(savefile + ' 파일이 저장되었습니다.')
###############################################################################
print('finished')