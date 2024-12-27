data = input('영어 문장 입력 >> ')
word = data.split()
len(word)
print('단어의 개수는 개입니다. ' ,len(word))

nums = [1, 2, 3, 4, 5, 6, 7]
type(nums)
sum = 0
prod = 1
for x in nums:
    sum += x
    prod *= x
print('sum = ', sum)
print('product = ', prod)

class MyNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __del__(self):
        pass
    def add(self):
        return self.a + self.b
    def prod(self):
        return self.a * self.b

myNum = MyNum(1.2, 3.4)
print('sum = ', myNum.add())
print('product = ', myNum.prod())


