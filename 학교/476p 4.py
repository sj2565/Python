class Circle:
    '''원을 표현하는 클래스 정의'''
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * self.PI

c = Circle(2.5)
print(c.area())
print(c.radius)    
print(Circle.PI)
