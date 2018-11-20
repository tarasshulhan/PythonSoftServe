list1 = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
red = list(filter(lambda x: x == 'red', list1))
print(red)

list2 = ['1','2','3','4','5','7']

list2int = list(map(int, list2))
print(list2int)

list2int2 = []
for i in list2:
    list2int2.append(int(i))

print(list2int2)