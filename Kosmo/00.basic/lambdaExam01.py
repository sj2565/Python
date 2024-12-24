def nolamdba(x, y):
    return 3 * x + 2 * y

x, y = 3, 5
result = nolamdba(x, y)
print('일반 함수 방식 : %d' % (result))

# 람다함수는 일반함수를 간결하게 축약시킨 방법
yeslamdba = lambda x, y : 3 * x + 2 * y

result = yeslamdba(x, y)
print('람다 방식 01 : %d' % (result))

result = yeslamdba(5, 7)
print('람다 방식 02 : %d' % (result))