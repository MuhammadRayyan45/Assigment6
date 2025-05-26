
from abc import abstractmethod, ABC

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.widht = width
        self.height = height

    def area(self):
        return self.widht * self.height

rect = Rectangle(4, 5)
print(rect.area())        
            

