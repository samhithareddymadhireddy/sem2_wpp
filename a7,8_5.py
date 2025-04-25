import math

# Base class
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Taking input from user
shape_type = int(input("Enter the choice of shape (1.rectangle 2.circle): "))

if shape_type == 1:
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    rect = Rectangle(width, height)
    print("Area of rectangle:", rect.area())
    print("Perimeter of rectangle:", rect.perimeter())

elif shape_type == 2:
    radius = float(input("Enter the radius of the circle: "))
    circ = Circle(radius)
    print("Area of circle:", circ.area())
    print("Perimeter of circle (circumference):", circ.perimeter())

else:
    print("Invalid shape type.")
