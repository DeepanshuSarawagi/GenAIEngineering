class Circle:
    def __init__(self, __radius, __color=None):
        self.__radius = __radius
        self.__color = __color

    def area(self):
        return 3.14 * self.__radius ** 2

color = 'blue'
smallCir = Circle(10, color)
smallCir.__setattr__('__radius', 15)    # Access and modify radius attribute
print(f"Area of {color} circle: {smallCir.area()}")

print(smallCir.__getattribute__('__radius'))
print(dir(smallCir))
print(smallCir.__dict__)