# Write a program to reverse a string.
# x = '1234abcd'
# def my_function(x):
#   return x[::-1]
# mytxt = my_function(x)
# print(mytxt)

# Write a function that accepts a string and calculate the number of uppercase letters
# and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# def my_function(x)
# x = input('Enter a string')
# capital = 0
# small = 0
# for i in x:
#     if i.isupper():
#         capital = capital + 1
        
#     else:
#         small = small + 1
# print(capital, small)

#Create a function that takes a list and returns a new list with unique elements of the first list.

# def my_function():
#     while len.list1 < 6: 
#         list1 = [input('Enter 5 elements')]
#     print(list1)

# def uninumber(list1):
#     list2 = []
#     for i in list1:
#         if i not in list2:
#             list2.append(i)
#         else:
#             continue
#     return(list2)
# print(uninumber([1,2,3,4,5,1,2,3,4,5,7]))

# Write a program that accepts a hyphen-separated sequence of words as input and
# prints the words in a hyphen-separated sequence after sorting them alphabetically.
    #DID NOT UNDERSTAND THE QUESTIONS 

# Write a program that accepts a sequence of lines as input and prints the lines after
# making all characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# line1 = input("enter the line 1")
# line2 = input("enter line 2 ")
# line3 = line1 + line2
# print(line3)
# line4 = line3.upper()
# print(line4)

# def compute(x1,x2):
#     sum = int(x1) + int(x2)
#     return sum

# a1 = "2"
# a2 = "3"
# print(compute(a1,a2))

# def mxlength(x1,x2):
#     a1 = len(x1)
#     a2 = len(x2)
#     if a1 > a2:
#         return(x1)
#     elif a1 == a2:
#         return(x1,x2)
#     else:
#         return(x2)

# y1 = input("enter string")
# y2 = input("enter secound string")
# print(mxlength(y1,y2))    

# Define a function which can generate and print a tuple 
# where the value are square of numbers between 1 and 20.

# def tuplegen():
#     list1 = []
#     for i in range(1, 21):
#         list1.append(i**2)
#     tuple1 = tuple(list1)
#     return tuple1
# print(tuplegen())

# Write a function called showNumbers that takes a parameter called lim
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.¶


# def showNumbers(limit):
#     for i in range(limit+1):
#         if i % 2== 0:
#             print(i, 'EVEN')
#         else:
#             print(i, 'ODD')

# showNumbers(7)

# def errorHandling():
#     try:
#         result = 5/0
#     except:
#         print("number can't be devided")
# errorHandling()