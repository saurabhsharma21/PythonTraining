# 1. Write a program in Python to allow the error of syntax to go in exception.
# HINT: use SyntaxError
# x = 5
# try:
#     x/0 
# except:
#     print("can't be devided by zero")


# 2. Write a program in Python to allow user to open a file by using argv module. If
# the entered name is incorrect throw an exception and ask them to enter the name
# again. Make sure to use read only mode.

# from sys import argv
# programeName, fileName = argv
# print("Programe Name is: ", programeName)
# print("File Name is: ", fileName)
# while True:
#     try:
#         with open(fileName, 'r') as file1:
#             content = file1.read()
#             print(content)
#             break
#     except:
#         print("enter the correct filename")
#         try_2 = input("Do you want to try again!! Press Yes and No:")
#         if try_2 == "Yes":
#             filename = input("Enter the correct file name:")
#         elif try_2 == "No":
#             break

# 3. Write a program to handle an error if the user entered the number more than
# four digits it should return “Please length is too short/long !!! Please provide only four
# digits”

# while True:
#     try:
#         x1 = int(input("enter a 4 digit number"))
#         if len(str(x1)) == 4 :
#             print(x1)
#             break
#         else:
#             raise Exception
#     except:
#         print("Please enter a number, the entered number is too short/long ")


# 4. Create a login page backend to ask user to enter the UserEmail and password.
# Make sure to ask Re-Type Password and if the password is incorrect give chance to
# enter it again but it should not be more than 3 times.

# userName = input("please enter your email address")
# password = input("please enter the password")
# reEnter = input("please enter the password again")
# counter = 0 
# while counter < 3:
#     try:
#         if password == reEnter:
#             print("login Success")
#             break
#         else:
#             raise Exception
#     except:
#         if password != reEnter:
#             input("please re-enter the password")
#             counter = counter + 1
        
#         elif counter == 3:
#             print("login attempt over")
#             break

            
# 5.  https://www.programiz.com/python-programming/exception-handling Go through this link to understand Finally and
# Raise concept.

#COMPLETE

# 6
# Read any file using Python File handling concept and return only the even
# length string from the doc.txt file.
# Consider the content as:
    # Hello I am a file
    # Where you need to return the data string
    # Which is of even length
    # Make sure you return the content in
    # The same link as it is present.

fileName = open("doc.txt", "r")
while True:
    for i in fileName:
        if len(i)%2 == 0:
            print(i)
        else:
            continue
