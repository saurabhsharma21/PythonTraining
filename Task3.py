# Create a list of the 10 elements of four different types of Data Type like int, 
# string, complex and float.
#1
#firstlist = [1, 2.5, 3, 4.8, 7, "Saurabh", "3j+i", "nine", 10 ]

#2
# listtwo = [1,2,3,4,5]
# slice_list= listtwo[2:3]
# print(slice_list)

#3
# list3 = [1,2,3,4]
# sum_list = 0
# prod_list = 1

# for i in list3:
#     sum_list = sum_list + i
#     prod_list = prod_list * i
# print(sum_list)
# print(prod_list)

#4
# minmax_list = [1,2,3,4,5,6,7,8,9,10]
# print(min(minmax_list))
# print(max(minmax_list))

#5
# list5 = [1,2,3,4,5,6,7,8,9]
# newlist = []
# for i in list5:
#     if i%2 == 0:
#         continue
#     else:
#         newlist.append(i)
# print(newlist)

#6
# list1 = []
# for i in range(1,31):
#    if i <= 5 or i >= 25:
#        list1.append(i**2)
# print(list1)

#7

# a = [[1, 3, 5, 7, 9, 10], [2, 4, 6, 8]]
# b = a[0] [:-1] + a[1]
# print(b)

#8
# d1={1:2,3:4}
# d2={5:6,7:9}
# d3={8:11,9:15}
# d1.update(d2) 
# d1.update(d3)
# print(d1)

#9
# mydict = {}
# for i in range(1, 10):
#     mydict[i]= i**2
# print(mydict)

#10
# newlist = input("Enter values in csv format")
# newlistnumber= [newlist]
# newlisttuple = tuple(newlist)
# print(newlistnumber)
# print(newlisttuple)

#11
# mylist = [1, 2.4, 'Saurabh', 3+4j, 5, 1001, 'ConsultAdd', 9+8j, 99.9, 10.0]
# print(mylist)

#12
# mylist = [1,2,4.4,'Saurabh', 101, 999]
# print(mylist[1:5])

#13
# x = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# print(x[5][0:4])
# print(x[6:8])
# # print(x[0:4][5:7]) NOT sure about the answer
# print(x[::-1])
# print(x[0:9:2])
# print(x[5][5][0])

#14
# mylist1 = list(range(1,1001))
# print(mylist1)
# mylist2 = xrange(0, 1001)
# print(mylist2)

#15
# Tuples do not allow values to be changed hence can be used in places where the data is required
# to be fixed, which makes them benificial over list. 

#16
# mylist = []
# for i in range(1, 100):
#     if i%3 == 0 and i%2 == 0:
#         mylist.append(i)
# print(mylist)

#17
# x = 'Saurabh'
# x_reverse = x[::-1]
# vov = ['a','e','i','o','u']
# for i in range(len(x_reverse)):
#     if x_reverse[i] in vov:
#         print(x_reverse[i], i)

#18
# mylist = 'hello my name is abcd'
# mylist2 = mylist.split(" ")
# for i in mylist2:
#     if len(i)%2 == 0:
#         print(mylist2)

#20


#21
#Write a program to find out the occurrence of a specific word from an alphanumeric statement.
# Example: 12abcbacbaba344ab

# Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

# x = '12abcbacbaba344ab'
# count = 0
# mylist1 = []

# for i in x:
#     if i.isalpha():
#         if i not in mylist1:
#             mylist1.append(i)

# for i in range (0, len(mylist1)):
#     print(mylist1[i], '=', x.count(mylist1[i])
#     )

# 9. Write a program in python to print the pair of numbers whose sum is equal to result
# number that is let& say 8.

# x=[1,2,3,4,5,6,7,8,9,-1]

# for i in x:
#     j = x.index(i)+1
#     # print("i",i)
#     while j < len(x):
        
#         if i+x[j] == 8:
#             print("number1", i)
#             print("number 2", x[j])
#         else:
#             print(i,x[j])
#         j = j+1

#20

# even_list = []
# odd_list = []
# min_ = 1
# max_ = 50
# while (len(even_list) < 5) or (len(odd_list) < 5):

#     x = int(input("enter a number between 1 and 50"))

#     if (x < min_) or (x > max_):
#         print("Out of range")
#     elif x % 2 == 0:
#         even_list.append(x)
#         print(even_list)
#     else:
#         odd_list.append(x)
#         print(odd_list)
# totalofeven = sum(even_list)
# print(totalofeven, " ", max(even_list) )

# totalofodd = sum(odd_list)
# print(totalofodd, " ", max(odd_list))

#21
# Generate and print another tuple whose values are even numbers in the given tuple
# x = (1,2,3,4,5,6,7,8,9,10)
# y = []
# for i in x:
#     if i % 2 == 0:
#         y.append(i)
# y = tuple(y)
# print(y)