# listBasic01.py
# 집합형 자료형 : 리스트, 사전, 튜플, 집합

# 리스트 []를 사용하여 만들 수 있다.
# 또한, list()라는 내장 함수를 이용하여 만들 수 있다.
# len() 함수는 요소의 갯수를 구해준다.
somelist=['이순신', '김유신', '신사임당', '김구', '황진이', '윤봉길', '김춘추']

print('요소 갯수 : %d' %(len(somelist)))

# 인덱싱 : 숫자와 [] 기호를 사용하여 원소 1개를 뽑아 내기
print(somelist[4])
print(somelist[-2]) # 역순

# 슬라이싱 : 집합 자료형의 일부 데이터를 뽑아 내기
# 시작값 <= [시작값:끝값:증감치] < 끝값
print(somelist[1:4])
print(somelist[4:])
print(somelist[:4])

length = len(somelist)
print(length)
print(somelist[1:length:2])
print(somelist[0:length:2])

# 3의 배수만 출력
print(somelist[0:length:3])