# forWithString.py
# 특정 구문을 공백으로 나누고, 문자열 관련 함수들을 다루어 본다.
mystring = 'Life is an egg'

# split() 함수는 공백을 기준으로 잘라 내어 list로 반환
mylist = mystring.split()
print(type(mylist)) # 리스트
print(mylist)

print('반복문을 사용하여 출력해 보자.')
for item in mylist:
    print(item.upper())
    # print(type(item))

# range(1, 5, 2) ==> range(시작값, 끝값, 증감치)

print('range(5)')
for idx in range(5):
    print(idx)

print(range(1,5))
print(range(1,5,2))

print('짝수번째는 대문자, 홀수번째는 소문자로 표현한다.')
for idx in range(len(mylist)):
    if idx % 2 == 0 :
        mylist[idx] = mylist[idx].upper() # 대문자
    else :
        mylist[idx] = mylist[idx].lower() # 소문자

print('join() 함수를 사용하여 문자열 합치기')
result = '헤헤'.join(mylist)
print(result)