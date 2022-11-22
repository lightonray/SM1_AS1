from abc import ABC, abstractmethod
from math import pi
from random import randint




class Shape(ABC):

    
    count = 0

   
    def __init__(self):
        Shape.count += 1

    
    @abstractmethod
    def name(self):
        
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    
    def __str__(self):
        n, a, p = self.name(), self.area(), self.perimeter()
        return f"{n} of area {a:.2f} and perimeter {p:.2f}"




class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def name(self):
        if self.is_square():
            return 'Square'
        else:
            return 'Rectangle'

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    

    def is_square(self):
        return self.__width == self.__height




class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def name(self):
        return 'Circle'

    def area(self):
        return pi * self.__radius * self.__radius

    def perimeter(self):
        return pi * self.__radius * 2




class Scaled(Shape):

    def __init__(self, other, scale):
        super().__init__()
        self.other = other
        self.scale = scale

    def name(self):
        return f"({self.other.name()} scaled by {self.scale})"

    def area(self):
        return self.other.area() * self.scale * self.scale

    def perimeter(self):
        return self.other.perimeter() * self.scale




def __demo():
    
    r1 = Rectangle(2, 3)
    print(f"Created: {r1}.")
    r2 = Rectangle(5, 5)
    print(f"Created: {r2}.")
    c = Circle(10)
    print(f"Created: {c}.")
    d = Circle(5)
    print(f"Created: {d}.")

    
    print(f"\nObject r1 is of type {type(r1)}.")
    print(f"Is object r1 a Rectangle? {isinstance(r1, Rectangle)}")
    print(f"Is object r1 a Circle? {isinstance(r1, Circle)}")

    
    print(f"Is object r1 a Shape? {isinstance(r1, Shape)}")

    
    
    

    
    tmp1, tmp2 = c.name, c.area
    
    c.name = lambda: "Bob"
    c.area = lambda: randint(1, 100)
    print(f"\nObject c is now: {c}")  
    print(f"Object d is now: {d}")    

    
    c.name, c.area = tmp1, tmp2
    print(f"Object c is now: {c}")  
    print(f"Object d is now: {d}")  

    
    s1 = Scaled(r1, 2)
    print(f"Created: {s1}.")
    
    s2 = Scaled(s1, 3)
    print(f"Created: {s2}.")

    print(f"Total of {Shape.count} Shape objects were created.")


if __name__ == "__main__":
    __demo()
