import math

def rect_area(length, width):
    return length * width

def tri_area(base, height):
    return (base * height) / 2

def circle_area(radius):
    return math.pi * (radius ** 2)

def main():
    type_of_operation = int(input("Enter 1 for Rectangle Area, 2 for Triangle area, and 3 for Circle area"))

    if type_of_operation == 1:
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))
        print("The area of the rectangle is {}".format(rect_area(length, width)))
    elif type_of_operation == 2:
        base = float(input("Enter triangle base: "))
        height = float(input("Enter triangle height: "))
        print("The area of the triangle is {}".format(tri_area(base, height)))
    elif type_of_operation == 3:
        radius = float(input("Enter the radius of the circle: "))
        print("The area of the circle is {}".format(circle_area(radius)))
    else:
        print("Wrong Command!")

main()

'''
def digit_sum(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum

print(digit_sum(12345))
'''