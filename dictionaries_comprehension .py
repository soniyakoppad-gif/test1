#1. Create a dictionary of squares of numbers from 1 to 10
square = {x:x**2 for x in range(1,10)}
print(square)

#2. Create a dictionary of even numbers as keys and their squares as values
square = {x :x**2 for x in range(1,20) if x%2 == 0}
print(square)

#3.
#3. Create a dictionary of words and their lengths from a sentence
Enter_String= "Python is awesome"
leng = {word: len(word) for word in Enter_String.split()}
print(leng)
print(Enter_String)


#.4. Create a dictionary of lowercase characters from a string
string =" Hello World"
lower_case = {char:char.lower() for char in string if char.isalpha()}
print(lower_case)


#5. Create a dictionary of numbers and their cubes
cube = {x : x**3 for x in range(6)}
print(cube)

#6.6. Create a dictionary of numbers and their squares, excluding odd numbers
square = {x:x**2 for x in range(1,10) if x %2 == 0 }
print(square)

#7. Create a dictionary of numbers and their prime status

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
prime_num = {x:is_prime(x) for x in numbers}
print(prime_num)


##functions 
def func1():
    return func1
    
print("hello world")


def add(x,y):
    return x+y
    
print(add(3,5))

def subtract(x,y):
    return x-y
    
def multiply(x,y):
    return x*y

def divide (x,y):
    if y !=0:
        return x/y
    else:
        return "error:division by zero"
        
print(add(10, 5))        
print(subtract(10, 5))   
print(multiply(10, 5))   
print(divide(10, 5))     
print(divide(10, 0))


def calculator(x,y,operation):
    if operation == "add":
        return x+y
    elif operation == "subtract":
        return x-y
    elif operation == "multiply":
        return x*y
    elif operation == "divide":
        return x/y if y != 0 else "error:division by zero"
    else:
        return "invalid operation"
        
print(calculator(10, 5,"add"))        
print(calculator(10, 5 , "subtract"))   
print(calculator(10, 5,"multiply"))   
print(calculator(10, 5,"divide"))     

 #1.   
def func(name,age):
    return name,age
    
print(func("sonal",30))


#2.Exercise 2: Create a function with variable length of arguments

def func1(a,b,c):
    return a,b,c
    
print(func1(20,40,60))

def fun1(*args):
    for arg in args:
        print(arg)
        
fun1(10,20)
fun1(20,40,60)
print(80,100)


#Exercise 3: Return multiple values from a function
def calculation(a,b):
    addtion = a + b
    subtract = a - b
    return addtion,subtract
    
res = calculation(100,40)
print(res)

#4.Exercise 4: Create a function with a default argument
def showEmployee(name,salary="9000"):
    print("Name:",name,"salary:",salary)
    
    
    
showEmployee("Ben", 12000)
showEmployee("Jessa")

#5.Create an inner function
def outer_func1(a,b):
    square = a ** 2
    def addtion(a,b):
        return a+b
    add =addtion(a,b)
        
    
    return add+5

result = outer_func1(5,10)
print(result)
#6.call by new name
    
def display_student(name, age):
    print(name, age)


show_student = display_student

show_student("Emma", 26)

#Generate a Python list of all the even numbers between 4 to 30

print(list(range(4,30,2)))

x = [4, 6, 8, 24, 12, 2]
print(max(x))

#arguments
def greet(name):
    print("hello",name)
    
greet("john")
greet("david")

def student_list(name,roll_no):
    print(f"{name},{roll_no}")
    
student_list("sham",30)
student_list("rohan",40)

#sum and difference

def summ(a,b):
    summation = a+b
    print("summ:",summation)
    
summ(5,3)

#return statement
def find_sq(a):
    sq_num = a*a
    cube_num = a*a*a
    return sq_num,cube_num
    
square =find_sq(5)

print("square:",square)


#summ of numbers
sum = lambda x,y:x+y
print(sum(10,20))

#multiplication

multi = lambda x,y : x*y
print(multiply(10,5))

square = lambda x : x*x
print(square(4))

cube = lambda x: x*x*x
print(cube(3))

add = lambda x,y:x+y
print(add(10,30))


#num is +ve 
positive_num = lambda x : x>0
print(positive_num(10))
print(positive_num(-4))


#num is -ve
pairs = [(1, 5), (2, 3), (4, 1)]
sorted_pairs = sorted(pairs,key = lambda x:x[1])
print(sorted_pairs)

#reverse string
reverse =lambda x : x[::-1]
print(reverse("hello"))

#max of numbers
num_max = lambda x,y: x if x > y else y
print(num_max(10,20))


#min of number
min_num = lambda x,y :x if x<y else x
print(min_num(5,10))


#Example 1: Cube of a Number
cube1 = lambda x:x**3
print(cube1(6))

#Example 2: Check if a String Starts with "A"


start = lambda x : x.startswith("A")
print(start("Apple"))
print(start("Banana"))

starts_with_A = lambda s: s.startswith("A")
print(starts_with_A("Apple"))   # True
print(starts_with_A("banana"))  # False





 





    
