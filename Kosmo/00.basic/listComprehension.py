# listComprehension.py
mylist01 = list(onedata for onedata in range(1, 6))
print(mylist01)

mylist02 = list(10  * onedata for onedata in range(1, 6))
print(mylist02)

# 짝수들만 제곱하여 리스트를 생성해 보라.
mylist03 = [3, 4, 6, 2]
result = [idx ** 2 for idx in mylist03 if idx % 2 == 0]
print(result)