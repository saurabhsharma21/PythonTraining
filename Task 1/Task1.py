#Code
#>>> a = 1; b = 3.3; c = 'String'

#>>> c
#'String'
#>>> b
#3.3
#>>> a
#1
########################

#>>> x = 1 + 2j
#>>> a = 3
#>>> a = x
#>>> a
#(1+2j)
 
#########################
#>>> a = 2
#>>> b = 3
#>>> result = a
#>>> a = b
#>>> b = result
#>>> a
#3
#>>> b
#2


#>>> a = 5 
#>>> b = 7
#>>> a, b = b, a
#>>> a
#7
#>>> b
#5
#######################

Python 3.7.3 (default, Jun  2 2020, 19:48:59) 
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a = eval(input('Enter a value'))
Enter a value10
>>> a
10

Python 2.7.16 (default, Feb 29 2020, 01:55:37) 
[GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.29.20) (-macos10.15-objc- on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a = eval(raw_input('Enter a value'))
Enter a value0
>>> a
0

#############################
a = int(input("Input number 1"))
b = int(input("Input number 2"))
z = a + b + 30
print("Sum total is ", + z)

##############################

>>> a = 'Saurabh'
>>> print("the imput value data type is: ", type(a))
the imput value data type is:  <class 'str'>
>>> print("the input value data type is: ",type(a))
the input value data type is:  <class 'str'>

########################

typeOfVariable = 1 #lowerCamel
TypeOfVariable2 = 'Saurabh' #LadderCamel
TYPEOFVARIABLE3 = 10.98 #UPPERCASE

#####################################
Yes!This is possible due to the fact that the data types are dynamically typed in python.
>>> a= 10 
>>> type(a)
<type 'int'>
>>> a= 'Hello'
>>> type(a)
<type 'str'>