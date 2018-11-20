class Figure():
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def info(self):
        print("Figure")
        print("Color: " + str(self.color))

class Square(Figure):
    def __init__(self, color, side_length):
        super.__init__(color)
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2

    def info(self):
        print("Square")
        print("Color: " + str(self.color))
        print("Side length: " + str(self.side_length))
        print("The area is: " + str(self.get_area()))

class Rectangle(Figure):
    def __init__(self, color, height, width):
        super.__init__(color)
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def info(self):
        print("Rectangle")
        print("Color: " + str(self.color))
        print("Height: " + str(self.height))
        print("Width:" + str(self.width))
        print("The area is: " + str(self.get_area()))

f1 = Square("red", 5)
f2 = Rectangle("blue", 5, 7)
f1.info()
f2.info()




