
userNum1 = int(input("Please input the first number:"))
userNum2 = int(input("Please input the second number:"))

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

print("The G.C.D. of {} and {} is: ".format(userNum1, userNum2) + str(gcd(userNum1, userNum2)) +
      "\nThe L.C.M. of {} and {} is: ".format(userNum1, userNum2) + str(lcm(userNum1, userNum2)))
