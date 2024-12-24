# tupleExam01
# 튜플은 소괄호()를 사용한다.
# 또한, 함수 tuple()를 사용한다.
# 리스트와 다른 점은 read only라는 점이다.
# 요소의 개수를 늘리거나 줄일수는 있지만, 값은 변경이 불가능하다.
tuple01 = (10, 20, 30)
tuple01 =  tuple01+ (40, )
print('tuple01 : ', tuple01)

tuple02 = 10, 20, 30, 40 # 단순 콤마 연결

mylist=[10, 20, 30, 40]
tuple03 = tuple(mylist)
print(type(tuple03))

if tuple02 == tuple03 :
    print('component equal')
else :
    print('component not equal')

tuple04 = (10, 20, 30)
tuple05 = (40, 50, 60)
print('+ 연산자는 2개의 튜플을 합쳐 준다.')
tuple06 = tuple04 + tuple05
print(tuple06)

print('* 연산자는 튜플을 지정한 수 만큼 반복한다.')
tuple07 = tuple04 * 3
print(tuple07)
print('-' * 40)

print('튜플을 사용한 데이터 맞 교환(swap 기법)')
a, b = 11, 22 # a는 11이고, b는 22이다.
a, b = b, a
print('a :', a, ', b :', b)

tuple08 = (11, 22, 33, 44, 55, 66)
print(tuple08[1:3])

print(tuple08[3:])

# tuple08[0] = 111 => tuple은 값을 변경 할 수 없다.(오류 발생)