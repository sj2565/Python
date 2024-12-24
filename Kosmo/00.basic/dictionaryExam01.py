# dictionaryExam01.py
# 사전은 중괄호 {}를 사용한다.
# 또한, 함수 dict()을 사용하여 만들 수 있다.
# len() 함수는 요소의 갯수를 구해 준다.
dictionary = {'김유신': 50, '윤봉길': 40, '김구': 60}
print('사전 내역 : ', dictionary)
print('요소 개수 : ', len(dictionary))

print('\nkeys() 메소드는 키 목록을 보여준다.')

# 자바 코딩 => for(Integer item : list){}
for key in dictionary.keys() :
    print(key)

print('\nvalues() 메소드는 값 목록을 보여준다.')
for aa in dictionary.values() :
    print(aa)

print('\nitems() 메소드는 키와 값을 가지는 tuple() 형태로 보여준다.')
for (key, aa) in dictionary.items() :     # (key, aa) => tuple
    print("{}의 나이는 {}살입니다.".format(key, aa))
    
print('\n특정 키의 값 찾기')
print(dictionary['윤봉길']) # 자바의 getter
# print(dictionary['설진욱']) # 존재하지 않는 키는 keyError 오류 발생

print('\nin 키워드를 사용한 유관순 존재 여부')
finditem = '유관순'
if finditem in dictionary : 
    print(finditem + '는 존재')
else :
    print(finditem + '는 미존재')

print('\n사전 내용 비우기')
dictionary.clear()

print('\n사전 내역')
print(dictionary)

