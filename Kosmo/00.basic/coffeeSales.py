# coffeeSales.py
'''
외따옴표 3개를 연속으로 작성하여, 내부에 멀티 라인 주석을 작성할 수 있다.
커피 3잔을 모두 판매 완료할 때 까지, 판매하는 프로그램을 작성한다.
while 구문을 사용하도록 한다.
특정한 조건을 충족하면 break 구문으로 프로그램을 종료한다.
'''

coffee = 3
price = 2000

print('판매 가능한 커피 잔 수 : %d잔' %coffee)
print('단가 : %d 원' %price)

while True :
    money = int(input('돈을 입력하세요 : '))
    if money == price : # 1잔 판매 가능
        print('커피 1잔을 판매한다.')
        coffee -= 1
    elif money > price : # 1잔 판매 후 거스름돈 지불
        print('거스름돈 {}원을 주고, 커피를 판매한다.'.format(money-price))
        coffee -= 1
    else : # 판매할 수 없음
        print('금액이 부족하여 커피를 판매할 수 없다.')

    print('커피 {}잔이 판매 가능하다.'.format(coffee))

    if coffee == 0 :
        print('커피가 다 떨어졌다. 판매를 중지한다.')
        break
print('끝')