def Num_List():
    List_Len = int(input("Enter length of list: "))
    List = [int(input("Enter value: ")) for x in range(List_Len)]

    print(List)

    #print("Minimum:", min(List))
    min = List[0]
    for i in List:
        if i < min:
            min = i
    print("Minimum:", min)

    #print("Maximum:", max(List))
    max = List[0]
    for i in List:
        if i > max:
            max = i
    print("Maximum:", max)

def Num_Combinations():
    List = list(range(1,11))
    print(List)
    print("Evens, Divisible by 2:", [x for x in List if x % 2 == 0])
    print("Odds, Divisible by 3:", [x for x in List if x % 2 !=0 and x % 3 == 0])
    print("Not divisible by 2 or 3:", [x for x in List if x % 2 != 0 and x % 3 != 0])

def User_Factorial():
    User_Num = int(input("Enter an integer: "))

    if User_Num == 0:
        print("1")
    elif User_Num < 0:
        print("You can only take the integral of a positive integer.")
    else:
        Fact = 1
        for i in range(1, User_Num+1):
            Fact *= i
        print("The factorial of {} is {}.".format(User_Num, Fact))

def Check_User():
    while True:
        if input("Enter Username: ") == "First":
            print("Welcome!")
            break
        else:
            print("Wrong Username")


#Num_List()
#Num_Combinations()
#User_Factorial()
Check_User()