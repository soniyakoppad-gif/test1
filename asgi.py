 #lambda functions

# # from functools import reduce
    

# # nums = [3,2,6,8,4,6,2,9]

# # evens = list(filter(lambda n: n%2 ==0 ,nums))

# # doubles = list(map(lambda n : n*2,evens))

# # sum =reduce(lambda a,b : a+b,doubles)
# # print(sum)


# # def add(x,y):
    # # return x+y
    
# # lambda x,y : x+y



# # def starts_with_A(s):
    # # return s[0] == "A"

# # fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# # map_object = map(starts_with_A, fruit)

# # print(list(map_object))





 
   
# # n = int(input("enter the value of n:"))
# # output = n * n

# # print("square of number = ",output )

# def square(n):
    # return (x ** 2 for x in n)

# x = [2,3,4,5,6]
# print(list(square(x)))


# x ,y = 10,20
# lambda x,y: x+y

# n =6
# # p=lambda n : n* n * n
# # print(p(n))
# print((lambda n : n* n * n)(n))


# x,y,z = 10,20,30
# # avg =lambda x,y,z : (x+y+z)/3
# # print(avg(x,y,z))
# print((lambda x,y,z : (x+y+z)/3)(10,20,30))

# r = lambda s : s.lstrip().rstrip().upper()
# print(r(' Nagpur '))

# print((lambda s : s.lstrip().rstrip().upper())(' Ngur '))


# lst1 = [1,2,3,4,5]
# lst2 = [10,20,30,40,50]
# print((lambda l:sum(l)/ len(l))(lst1))
# print((lambda l:sum(l)/ len(l))(lst2))


# #higher order functions
# d = {'0il':230,'clip':150,'stud':175,'nut':35}
# d1 = sorted(d.items(),key = lambda kv:kv[1])
# print(d1)

# import math
# def fun(n):
    # return n * n
    
# lst = [5,10,15,20,25,30]
# m1 = map(math.radians,lst)
# m2 = map(math.radians,lst)
# m3 = map(fun,lst)
# print(list(m1))
# print(list(m2))
# print(list(m3))



# #Add 10 to argument a, and return the result:
# x = lambda a : a + 10
# print(x(5))


# x = lambda a,b : a * b
# print(x(5,6))

# y = lambda a,b : a / b
# print(y(12,6)) 

# #square of the functions
# def square (n):
  # op =  n * n
  # print(op)

# square(3)

# output = lambda n: n * n
# print(output(10))

# xx = lambda a,b,c : a + b + c
# print(xx(10,20,30))


# def myfunc(n):
    # return lambda a : a * n

# mydoubler = myfunc(2)
# mytripper = myfunc(3)

# print(mytripper(11))

num = [1,2,3,4,5]
doubled = list(map(lambda x : x * 2 , num))
print(doubled)


for i in range(len(num)):
    square_func = list(map(lambda x : x * x ,num ))
print(square_func)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_num = list(filter(lambda x : x %2 == 0 , numbers))
print(odd_num)


#Sort a list of tuples by the second element:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students,key = lambda x : x[1])
print(sorted_students)

#Sort strings by length:
words = ["apple", "pie", "banana", "cherry"]
word_sorted = sorted (words, key = lambda x : len(x))
print(word_sorted)

# fruits = ["a", "b", "c"]
# for x in fruits:
  # print(x)

# x = 10
# for x in range(x):
    # print(x)
    
    
# aa = "applexyapit"
# for x in aa:
    # print(x[0:5])
    
# test = ['a','b','c','d']
# rest = ['a','b']
# # output = ['aa','bb','cc']
# out = []

# test.remove(test[3])
# for i in range(len(test)):
    # out.append(test[i]+rest[i])
    

# print(out[:3])
    
# # output = [x + y for x, y in zip(test, rest)]

# ##map functions

#without using lambda function
def starts_with_A(s):
    return s[0] =="A"

fruits = ["Apple","Banana","Cheey","Apricot","Orange"]



may_object = map(starts_with_A, fruits)
print(list(may_object))



#using lambda
fruits = ["Apple","Banana","Cheey","Apricot","Orange"]
may_object = map(lambda s : s[0] == "A",fruits)
print(list(may_object))

##filter function
num = [1,2,3,4,5,6]
even = list(map(lambda x: x** 2, filter(lambda x : x % 2 == 0,num)))
print(even)

# reduce()

import functools
def getsum(x,y):
    return x+y

def getprod(x,y):
    return x*y
    
lst = [1,2,3,4,5]
s = functools.reduce(getsum,lst)
p = functools.reduce(getprod,lst)
print(s)
print(p) 


# using lambda with map() --> to get square of number
lst1 = [5,10,15,20,25]
x = map(lambda x : x ** 2 ,lst1)
print(list(x))

#using filter with lambda
lst2 = [5,10,18,27,25]
y = filter(lambda n : n % 5 == 0,lst2)
print(list(y))


#using lambda with reduce()
from functools import reduce
lst3 = [1,2,3,4,5]
s = reduce(lambda x,y :x+y,lst3)
p = reduce(lambda x,y :x*y,lst3)
print(s,p)








