# a = [2,3,4,5]
# d1 = [val**2 for val  in a]
# print(d1)

# a = [1, 2, 3, 4, 5]
# res = []
# for val in a:
    # res.append(val**2)
# print(res)

# num = [2,3,4,5,6,6]
# b = [x*10 for x in num ]
# print(b)

# n = int(input("Enter how many terms: "))

# fib = [0, 1]

# [fib.append(fib[-1] + fib[-2]) for i in range(2, n)]

# print(fib)


c = [x for x in range(20)]
a = [x for x in c if x%2 ==0]
b = [x for x in c if x%2 !=0]
print("even num",a)
print("odd num",b)

num = [10, -5, 0, 7, -8, 12, -3]
positive = [n for n in num if n >0]
negative = [n for n in num if n< 0]
print("positive num",positive)
print("negative num",negative)

lst = ['ram','ravi','rohan','shipla','mohan']
uppercase = [x.upper() for x in lst]
print("upper case",uppercase)
set_upper = set(uppercase)
print(set_upper)

a = []
z = [x for x in range(10,30)]
aa = [x for x in z if x%2 == 0, a.append(x)]
print(aa)

a = []
z = [x for x in range(10,30)]
aa = [a.append(x) or x for x in z if x % 2 == 0]
print(a)
print(aa)







