from math import pi


class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


my_circle = Circle(5)

print(my_circle.area())
print(my_circle.perimeter())


