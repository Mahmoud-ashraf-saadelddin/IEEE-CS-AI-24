'''
Write a program that asks the user for input
and handles the possibility of the user entering a non-numeric value.
'''

try:
    m = int(input())
except ValueError as v:
    print(v)
    print("only numbers are allowed")
else:
    print(m)

# another solution:
# m = input()
# while m.isnumeric() != True:
#     m = input("enter a numeric value ")
#
# print(m)

'''
The isnumeric() method in Python checks whether all the characters in a string
 are numeric (0-9). It returns True if all characters are numeric, and False otherwise
'''
