'''
Taras Shulhan
Python Core 355
Homework 2 Task 2
'''


four_digit_num = input("Please input a four digit number: ") # ask for input

num_list = [int(digit) for digit in str(four_digit_num)] # split the number into a list of integers

product = num_list[0]
for number in num_list[1:]: # multiply all digits together
    product *= number

reverse_num = [i for i in reversed(num_list)] # create new list from reversed list
reverse_num = ''.join(str(i) for i in reverse_num) # join back into a string

sorted_num = ''.join(str(i) for i in sorted(num_list))

print("The product of the four digits is: " + str(product) + "\nThe number reversed is: " + reverse_num
      + "\nThe number with the digits sorted is: " + sorted_num)
