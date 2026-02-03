# #class and objects
# a = 3.14   # a  is an object of float class
# s = 'sudsh' # s is an object of str class
# lst = [10,20,30]   #lst is an object of list class
# tpl = ['a','b','c']  #tuple is an object of type class
# print(a,s,lst,tpl)

# s1 = 'ridesh'  # s1,s2 is object of typee str class
# s2 = 'geeta'
# print(s1,s2)


# #user _defined class
# class employee:
    # def set_data():
        # set.name = n
        # # set.age = a
        # # set.salary = s

    # # def display_data():
        # # print(set.name,set.age,set.salary)


# # # # # e1 = employee()
# # # # # e1.set_data('ramesh',23,25000)
# # # # # e1.display_data()
# # # # # e2 = employee()
# # # # # e2.set_data('sudeshwar',28,300000)
# # # # # e2.display_data()

# # e1 = employee()
# # e2 = employee()
# # e3 = employee()
# # e3.name = 'rakesh'
# # e3.age = 25


# # def __init__(self,n = '',a = 0,s = 0.0):
    # # self._name = n
    # # self._age = a
    # # self._salary = s

# # def _del_(self):
    # # print('deleting object' +str(self))

# # e1 = employee()
# # e1.set_data('sudesh',25,30000)
# # e1.display_data()
# # e2 = employee('ramesh',23,25000)
# # e2.display_data()
# # e1 = None
# # e2 = None

# #1.
# class dog():
    # def __init__(self,name,bread):
        # self.name = name
        # self.bread = bread


    # def bark(self):
        # return f"{self.name} says woof!"


# #creates objects
# dog1 = dog("buddy","globals retrious")
# dog2 = dog("max","begade")

# print(dog1.bark())
# print(dog2.bark())

# #2.

# class car():
    # def __init__(self,brand,year):
        # self.brand = brand
        # self.year = year

    # def start(self):
        # return f"{self.brand}{self.year} is starting"

    # def stop(self):
        # return f"{self.brand}{self.year} is stoping"

# car1 = car("tesla",2022)
# print(car1.start())
# print(car1.stop())

# #.3.
# class Bankaccount():
    # def __init__(self,owner,balance=0):
        # self.owner = owner
        # self.balance = balance
        
    # def deposit(self, amount):
        # self.balance += amount
        # return f"Deposited {amount}. New balance: {self.balance}"
    
    # def withdraw(self, amount):
        # if amount <= self.balance: 
            # self.balance -= amount
            # return f"Withdrew {amount}. New balance: {self.balance}"
        # else:
            # return "Insufficient funds!"

# #Practice
# account =Bankaccount("Alice",500)
# print(account.deposit(200))
# print(account.withdraw(100))
# print(account.withdraw(700))


# #4.
# class number:
    # def set_number(self,n):
        # self.num = n
    
    # def get_number(self):
        # return self.num
        
    # def print_number(self):
        # print(self.num)
        
    # def isnegative(self):
        # if self.num <0:
            # return True
        # else:
            # return False
            
    # def isdivisibleby(self, n):
        # if n ==0:
            # return False
        # if self.num % n == 0:
            # return True
        # else:
            # return False
            
    # def absolute_value(self):
        # if self.num < 0 :
            # return self.num
        # else:
            # return - 1 * self.num
        
# x = number()
# x.set_number(-1234)
# x.print_number();
# if x.isdivisibleby(5) == True:
    # print("5 divides",x.get_number())
# else:
    # print("5 does not divide" ,x.get_number())
# print("absolute_value of",x.get_number(),"is",x.absolute_value())
        
        

        



# print(lst)
# x = lst.count(1)
# print("number of count sequence 1 :",x) 
# y = lst.count(3)
# print("number of count sequence 3 :",y)
# z = lst.count(2)
# print("number of count sequence 2 :",z)

# a = lst.count(4)
# print("number of count sequence 4:",a)



# lst = [1,2,3,4,3,1,5]

# lst1 = [1,2,3]
# lst2 = [3,4,5]
# lst1.append(lst2)
# print(lst1)

tpl = (1,2,3)
# print(tpl)
x= tpl +(4,)
print(x)



tpl = (1, 2, 3)
lst = list(tpl)
lst.append(4)
tpl = tuple(lst)
print(tpl)

s = "Python"
print(s[0::2])

print("".join(s[::2]))










