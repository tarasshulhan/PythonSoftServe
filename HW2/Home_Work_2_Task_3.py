'''
Taras Shulhan
Python Core 355
Homework 2 Task 3
'''


num_1 = int(input("Input a number: "))
num_2 = int(input("Input another number: "))

print("First number: " + str(num_1) + "\nSecond number: " + str(num_2) + "\nSwapping...")

num_1 = num_1 + num_2
num_2 = num_1 - num_2
num_1 = num_1 - num_2

print("First number: " + str(num_1) + "\nSecond number: " + str(num_2))