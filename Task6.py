# 1. Write a program to Python find the values which is not divisible 3 but is
# should be a multiple of 7. Make sure to use only higher order function.

# def divfun(x):
#     if (x % 3 != 0) and (x % 7 == 0):
#         print(x)
# list(filter(divfun, range(20)))



# 2. Write a program in Python to multiple the element of list by itself using
# traditional function and pass the function to map to complete the operation.

# def selfmul(x):
#     y = []
#     for i in x:
#         y.append(i*i)
#     return y
# print(selfmul([1,2,3,4]))


# 3. Write a program to Python find out the character in a string which is
# uppercase using list comprehension.

x = input("Enter a string")
# for i in x:
#     if i.isalpha() and i.isupper():
#         print(i)

y = [i for i in x if i.isalpha() if i.isupper()]
print(y)

# number_list = [ x for x in range(20) if x % 2 == 0]
# print(number_list)
       

# 4. Write a program to construct a dictionary from the two lists containing the
# names of students and their corresponding subjects. The dictionary should maps
# the students with their respective subjects. Let’s see how to do this using for loops
# and dictionary comprehension. HINT-Use Zip function also
# ● Student = [&#39;Smit&#39;, &#39;Jaya&#39;, &#39;Rayyan&#39;]

# ● capital = [&#39;CSE&#39;, &#39;Networking&#39;, &#39;Operating System&#39;]
# 5. Learn More about Yield, next and Generators
# 6. Write a program in Python using generators to reverse the string. Input String
# = “Consultadd Training”
# 7. Write any example on decorators.
# 8. Learn about What is FRONT END and its Technologies and Tools
# ● Make sure to mention at least 5 top notch technologies of Frontend.
# ● Also mentioned the name of companies using those 5 technologies
# individually