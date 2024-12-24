# inputOutput.py
# input 함수를 사용하면 데이터를 입력 받을 수 있다.
# 재실행 단축키 : shift + F10
name = input('이름 입력 : ')

# 형변환 int('10') ==> 10

age = int(input('나이 입력 : '))

newage = age + 5
print(newage)

print('이름 : ' + name)

# %s 기호는 문자열로 치환될 곳
print('이름 : %s' %name)

# 문자열로 형변환이 필요하다.
# str(5) ===> '5'
print('나이 : ' +str(age))
print('나이 : %s' %str(age))

# %d 기호는 숫자로 치환 될 곳
print('나이 : %d' % age)
print(newage)