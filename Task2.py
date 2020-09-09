# num = int(input("Enter a Number"))
# if (num % 3) == 0 and (num % 5) == 0:
#     print("ConsultAdd Python Training")
# elif (num % 3) == 0:
#     print("ConsultAdd")
# elif (num % 5) == 0:
#     print("c")

# num = int(input("Enter a number between 1 to 5"))
# result = 0
# if num in range(1,5):
#     num1 = int(input("Enter Number1"))
#     num2 = int(input("Enter Number2"))
#     if num == 1:
#         result = num1 + num2
#         print(result)
#     elif num == 2:
#         result = num1 - num2
#         print(result)
#     elif num == 3:
#         result = num1 * num2
#         print(result)
#     elif num == 4:
#         result = num1 / num2
#         print(result)
    
# elif num == 5:
#     num1 = int(input("Enter Number1"))
#     num2 = int(input("Enter Number2"))
#     num3 = int(input("Enter Number3"))
#     num4 = int(input("Enter Number4"))
#     result = (num1 + num2 + num3 + num4)/4
#     print(result)
# if result < 0:
    # print("NEGATIVE")

# a = 10
# b = 20
# c = 30
# avg = (a + b + c)/ 3
# print("average is", avg)
# if avg > a and avg > b and avg > c:
#     print("average is greator than", a, b, c)
# elif avg > a and avg > b:
#     print("Average is higher than", a, b)
# elif avg > a and avg > c:
#     print("average is higher than", a, c)
# elif avg > b and avg > c:
#     print("average is higher than", b, c)
# elif avg > a:
#     print("average is just higher than", a)
# elif avg > b:
#     print("average is just higher than", b)
# elif avg > c:
#     print("average is just higher than", c)

# while True:
#     num1 = int(input("Enter a number"))
#     if num1 > 0:
#         print("Good Going")
#         continue
#     elif num1 < 0:
#         print("it's Over")
#         break

# for i in range(2000, 3200):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i)
 ##6 .1       
# x = 123 
# for i in x:
#     print(i)
# Traceback (most recent call last):
#   File "c:\Users\shijohar\Desktop\Python\PythonTraining\Task2.py", line 71, in <module>
#     for i in x:
# TypeError: 'int' object is not iterable

# 6.2
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print("error")
# OUTPUT
# 0
# 1
# 2

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break
# OUTPUT
# 0
# 1
# 2
# 3
# 4

# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
#        Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement

# for count in range(0,7):
#     if count == 3 or count == 6:
#         continue
#     print(count)

# OUTPUT
# 0
# 1
# 2
# 4
# 5
# 8.  Write a program that accepts a string as an input from user and calculate the 
# number of digits and letters.
#      Expected output: consul12
#      Letters 6
#      Digits 2
# word = input("Enter a word and digit")
# digit = 0
# length = 0 
# for d in word:
#     if d.isdigit():
#         digit = digit+1
#     elif d.isalpha():
#         length = length+1
#     else:
#         pass
# print("total Digits are", digit)
# print("total Alpha are", length)
# OUTPUT
# Enter a word and digitconsul12
# total Digits are 2
# total Alpha are 6

# counter = 1 
# while counter <= 5:
#     number = int(input("Luck Number is"))
#     if number == 5:
#         print("Good Guess")
#     else:
#         print("Try Again")
#     counter = counter+1
# else:
#     print("Game Over")

# OUTPUT
# Luck Number is5
# Good Guess
# Luck Number is4
# Try Again
# Luck Number is3
# Try Again
# Luck Number is2
# Try Again
# Luck Number is5
# Good Guess
# Game Over

# counter = 1 
# while counter <= 5:
#     number = int(input("Luck Number is"))
#     if number == 5:
#         print("Good Guess")
#         break
#     else:
#         print("Try Again")
    
#     counter = counter+1
# else:
#     print("Sorry that was NOT a good Guess")
# OUTPUT
# Luck Number is1
# Try Again
# Luck Number is2
# Try Again
# Luck Number is3
# Try Again
# Luck Number is3
# Try Again
# Luck Number is4
# Try Again
# Sorry that was NOT a good Guess
