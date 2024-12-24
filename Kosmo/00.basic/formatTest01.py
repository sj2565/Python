#formatTest01.jpy
coffee = 3
price = 2000

# {} 기호는 치환될 영역이다.
print("우리 매장에 커피가 {}잔이 있습니다.".format(coffee))

money = int(input('돈을 넣어 주세요. : '))
print("{}을 입금하셨습니다.".format(money))

change = money - price # 잔돈
message = "거스름돈은 {}원이며, 커피 {}잔을 판매합니다."
print(message.format(change, 1))

coffee = coffee - 1
print("남은 커피는 총 {} 잔 입니다.".format(coffee))