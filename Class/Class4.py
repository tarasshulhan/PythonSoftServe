def While_Evens():
    i = 0
    while i < 10:
        print(i)
        i+=2

def For_Evens():
    for i in range(0, 10, 2):
        print(i)

def Odds():
    for i in range(1, 20, 2):
        print(i)

def Odds_Continue():
    for i in range(0, 20, 1):
        if i % 2 == 0:
            continue
        else:
            print(i)

def Contains_Odds(list_1):
    for i in list_1:
        if i % 2 != 0:
            print("The list contains odds.")
            break
    else:
        print("The list contains no odds.")


Int_List = list(range(0, 20, 1))

def Float_List(list_1):
    for i in list_1:
        list_1[i] = float(list_1[i])
    return list_1

def Fibonacci(limit):
    Fib_List = [0, 1]
    a = 0
    b = 1
    c = 0
    while c < limit:
        c = a + b
        Fib_List.append(c)
        a = b
        b = c
    return Fib_List

Word_List = ["aa", "bb", "cc", "dd", "ee", "ff"]
def Print_List(list_1):
    for word in list_1:
        print(word)

def Print_List_2(list_1):
    for word in list_1:
        for letter in word:
            print(letter, end="&")
#While_Evens()
#For_Evens()
#Odds()
#Odds_Continue()
#Contains_Odds(list(range(0, 20, 1)))

#print(Int_List)
#print(Float_List(Int_List))

#print(Fibonacci(20))

Print_List(Word_List)
Print_List_2(Word_List)

