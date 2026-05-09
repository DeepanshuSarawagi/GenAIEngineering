class Circle:
    def __init__(self, radius, color=None):
        self.radius = radius
        self.color = color

    def area(self):
        return 3.14 * self.radius ** 2

color = 'blue'
smallCir = Circle(10, color)
print(f"Area of {color} circle: {smallCir.area()}")