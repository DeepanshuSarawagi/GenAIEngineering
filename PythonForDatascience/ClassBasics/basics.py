class Circle:
    def __init__(self, __radius, __color=None):
        self.radius = __radius
        self.color = __color

    def area(self):
        return 3.14 * self.radius ** 2

color = 'blue'
smallCir = Circle(10, color)
smallCir.radius = 15    # Access and modify radius attribute
print(f"Area of {color} circle: {smallCir.area()}")