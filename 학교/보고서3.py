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
print('합 : ' ,myNum.add())
print('곱 : ' ,myNum.prod())        
        
