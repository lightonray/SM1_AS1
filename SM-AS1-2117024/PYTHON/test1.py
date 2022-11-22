"""A dummy docstring."""
from abc import ABC,abstractmethod
from math import pi
from random import randint

class Shape(ABC):
    # A class attribute, so the same value is shared by everyone.
    """A dummy docstring."""
    count = 0
    # This method is executed automatically at every object creation.
    # Even though Shape is an abstract class, subclass objects can
    # still be created, and we want them to count as Shapes.
    def __init__(self):
        Shape.count += 1
    # All subclasses must implement these abstract methods, since
    # otherwise those subclasses are also abstract. (Which can also
    # be totally reasonable in some situations.)
    @abstractmethod
    def name(self):
        """A dummy docstring."""
    @abstractmethod
    def area(self):
        """A dummy docstring."""
    @abstractmethod
    def perimeter(self):
        """A dummy docstring."""
    def __str__(self):
        variable_n, variable_a, variable_p = self.name(), self.area(), self.perimeter()
        return f"{variable_n} of area {variable_a:.2f} and perimeter {variable_p:.2f}"

    # A subclass of Shape that defines area and perimeter to work one way.
class Rectangle(Shape):
    """A dummy docstring."""
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
    def name(self):
        return 'Square'
    def area(self):
        return self.__width * self.__height
    def perimeter(self):
        return 2 * (self.__width + self.__height)
    # We can define new methods that do not exist in superclass.
    def is_square(self):
        """A dummy docstring."""
        return self.__width == self.__height
    # Another subclass of Shape, with different area and perimeter formulas.
class Circle(Shape):
    """A dummy docstring."""
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
    """A dummy docstring."""
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

    # Let's create some objects to demonstrate how classes work.
    rectangle_one = Rectangle(2, 3)
    print(f"Created: {rectangle_one}.")
    rectangle_two = Rectangle(5, 5)
    print(f"Created: {rectangle_two}.")
    circle_one = Circle(10)
    print(f"Created: {circle_one}.")
    cricle_two = Circle(5)
    print(f"Created: {cricle_two}.")
    print(f"\nObject r1 is of type {(rectangle_one)}.")
    print(f"Is object r1 a Rectangle? {isinstance(rectangle_one, Rectangle)}")
    print(f"Is object r1 a Circle? {isinstance(rectangle_one, Circle)}")
    print(f"Is object r1 a Shape? {isinstance(rectangle_one, Shape)}")
    tmp1, tmp2 = circle_one.name, circle_one.area
    circle_one.name = lambda:"Bob"
    circle_one.area = lambda: randint(1, 100)
    print(f"\nObject c is now: {circle_one}")
    print(f"Object d is now: {cricle_two}")
    circle_one.name, circle_one.area = tmp1,tmp2
    print(f"Object c is now: {circle_one}")
    print(f"Object d is now: {cricle_two}")
    scaled_one = Scaled(rectangle_one, 2)
    print(f"Created: {scaled_one}.")
    scaled_two = Scaled(scaled_one, 3)
    print(f"Created: {scaled_two}.")

    print(f"Total of {Shape.count} Shape objects were created.")


if __name__ == "__main__":
    __demo()
