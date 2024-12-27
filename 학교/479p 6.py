from abc import *

class Polygon(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2

rect = Rectangle(2.4, 4.3)
print('사각형 면적: %.2f' %rect.area())
print('사각형 둘레: %.2f' %rect.perimeter())
