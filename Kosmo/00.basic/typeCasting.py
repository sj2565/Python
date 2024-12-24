# typeCasting.py
str1 = '100'
str2 = '200'
str3 = '12.345'

# type() 함수는 데이터의 유형을 알려준다.
print(type(str1))

int1 = int(str1)
int2 = int(str2)
sum = int1 + int2
print(type(int1))

# 타입 비교는 == 연산자를 사용하면 된다.
print(int1 == str)

# 콤마를 이용하여 데이터를 출력
print('sum : ', sum)

float1 = float(str3)
float2 = float(str2)
print('float2 : ', float2)

# 312.345 출력
add = sum + float1
print(add)

data1 = float(str1)
data2 = float(str2)
data3 = float(str3)
total = data1 + data2 + data3
print('total : ' , total)