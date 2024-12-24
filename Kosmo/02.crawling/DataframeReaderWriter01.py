# 데이터 프레임 읽기 / 쓰기

# 넘파이 : numerical python (행렬)
import numpy as np
import pandas as pd

myindex = ['이순신', '김유신', '강감찬', '광해군', '연산군']   # 행 색인
mycolumns = ['서울', '부산', '광주', '목포', '수원']      # 열 색인
mylist = list(10 * onedata for onedata in range(1, 26))
print(mylist)

# np.reshape 함수는 차원을 변형해주는 함수
myframe = pd.DataFrame(np.reshape(mylist, (5, 5)), index=myindex, columns=mycolumns)
print(myframe)

# iloc 속성은 행 인덱스를 기준으로 행을 추출하는 속성
# index location
#

print('\n# 1행만 Series로 읽어오기')
result = myframe.iloc[1]
print(result)

print('\n# 몇 개의 행을 읽어 오기')
result = myframe.iloc[1, 3]
print(result)

print('\n# 짝수 행만 가져 오기')
result = myframe.iloc[0::2]
print(result)

print('\n# 홀수 행만 가져 오기')
result = myframe.iloc[1::2]
print(result)

# loc 속성은 라벨(행색인)의 이름을 이용하여 데이터를 찾아 준다.
print('\n# 이순신 행만 Series로 읽어 오기')
result = myframe.loc['이순신']
print(result)

print('\n# 이순신 행만 DataFrame로 읽어 오기')
result = myframe.loc[['이순신']]
print(result)

print('\n# 강감감과 이순신 데이터 읽어 오기')
result = myframe.loc[['이순신', '강감찬']]
print(result)

print('\n# 행 색인 정보 추출')
print(myframe.index)

# 랜덤하게 3개를 복원 추출한다.
mytarget = np.random.choice(myframe.index, 3)
#print(mytarget)
result = myframe.loc[mytarget]
print(result)

print('\n# 강감찬의 광주 실적 ')
result = myframe.loc[['강감찬'],['광주']]
print(result)

print('\n# 연산군과 광해군의 광주/목포 ')
result = myframe.loc[['연산군', '광해군'], ['광주', '목포']]
print(result)

print('\n# 연속적인 데이터 가져 오기')
result = myframe.loc['김유신':'광해군', '광주':'목포']
print(result)

print('\n# boolean 색인')
result = myframe.loc[[False, True, True, False, True]]
print(result)

print('\n# 부산 실적이 100이하인 항목')
result = myframe.loc[myframe['부산'] <= 100]
print(result)

print('\n# 목포 실적이 140인 항목')
result = myframe.loc[myframe['목포'] == 140]
print(result)

print('\n# 람다 함수의 사용')
result = myframe.loc[lambda df : df['광주'] >= 130]
print(result)


print('\n# 이순신과 강감찬의 부산 실적 30으로 변경')
myframe.loc[['이순신', '강감찬'], ['부산']] = 30
print(myframe)

print('\n# 김유신부터 광해군까지 경주 실적 80으로 변경')
myframe.loc['김유신':'광해군', ['경주']] = 80
print(myframe)

print('\n# 연산군의 모든 실적 50으로 변경')
myframe.loc[['연산군'], :] = 50
print(myframe)

print('\n# 모든 사람의 광주 실적 60으로 변경')
myframe.loc[:, ['광주']] = 60
print(myframe)

print('\n# 경주 실적이 70이하인, 데이터들의 경주/광주 컬럼을 모두 0으로 변경하기')
myframe.loc[myframe['경주'] <= 70, ['경주', '광주']] = 0
print(myframe)

print('finished')