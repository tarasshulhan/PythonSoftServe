
userNum1 = int(input("Please input the first number:"))
userNum2 = int(input("Please input the second number:"))

if userNum1 == userNum2:
    print("The numbers are equal")
else:
    print("The first number ({}) is larger".format(userNum1) if userNum1 > userNum2 else "The second number ({}) is larger".format(userNum2))