
userNum = int(input("Please input a positive integer: "))

# n is operating variable to save user num
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("The factorial of {} is: ".format(userNum) + str(factorial(userNum)) if userNum >= 0 else "The input must be a positive integer")



