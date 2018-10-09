'''
Taras Shulhan
Python Core Lv 355
Kata Counting Sheep
'''


def count_sheeps(arrayOfSheeps):
    Sheep_Count = 0
    for i in arrayOfSheeps:
        if i:
            Sheep_Count +=1
    return Sheep_Count
