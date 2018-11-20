def Func1():
    try:
        user_int = int(input("Enter an intger: "))
        print("Even") if user_int % 2 == 0 else print("Odd")
    except ValueError as t:
        print("Not an integer")
        print(t)

def Func2():
    try:
        user_age = int(input("Enter your age: "))
        if user_age < 0:
            raise Exception("Negative Value")
        print("Even") if user_age % 2 == 0 else print("Odd")
    except Exception as n:
        print(n)
    except ValueError as v:
        print(v)
def Func3():
    try:
        a_val, b_val = map(float, input("Enter the two values separated by a comma: ").split(","))
        print(a_val / b_val)
    except ZeroDivisionError as z:
        print("Can not divide by zero")
        print(z)
    except ValueError as v:
        print("Please input two numbers separated by a comma")
        print(v)

def Func4():
    try:
        user_day = int(input("Input an integer to represent the day of the week: "))
        if user_day < 1 or user_day > 7:
            raise Exception("Not a day")
        if user_day == 1:
            print("Monday")
        elif user_day == 2:
            print("Tuesday")
        elif user_day == 3:
            print("Wednesday")
        elif user_day == 4:
            print("Thursday")
        elif user_day == 5:
            print("Friday")
        elif user_day == 6:
            print("Tuesday")
        elif user_day == 7:
            print("Sunday")
    except ValueError as v:
        print("Not a number")
        print(v)
    except Exception as n:
        print("This number does not correspond to a day of the week")
        print(n)


#Func1()
#Func2()
#Func3()
Func4()