fruits = ['apple', 'banana', 'grapes', 'pear']
prices = (1000, 500, 1200, 1500)
fruitsprices = dict(zip(fruits, prices))
print(fruitsprices)
print("")
for i, fruits in enumerate((fruits), start = 1):
    print('{}  {} 가격: {} '.format(i, fruits, prices[0]))

