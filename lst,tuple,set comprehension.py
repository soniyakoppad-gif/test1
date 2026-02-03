# #list comprehension

# # #generate 20 random number in the range 10 to 100

# # import random

# # d = [random.randint(10,100) for  x in range(20)]
# # print(d)

# # #genreate square n cube of al number]

# # a = [(x,x*2,x**3) for x in range(10)]
# # print(a)

# # # convert list of string to list of integers

# # b = [int(x) for x in ['10','20','30','40']]
# # print(b)

# # c = [float (x)for x in [10,20,30,40]]
# # print(c)

# #generate a list of even number in the range 10 to 30
# a = [n for n in range(10,30) if n%2 == 0]
# print(a)

# #from list delete all umber having a value between 20 and 50
# b = [num for num in a if num < 20 and num>50]
# print(b)

# # flatten the list of list
# arr = [[1,2,3,4],[5,6,7],[7,8,9,10]]
# cc = [*arr[0],*arr[1],*arr[2]]
# print(cc)

# ab = [(i,j,k) for i in[1,2,3] for j in [1,2,3] for k in [1,2,3] if i!=j and  j != k and k!=i]
# print(ab)

# # set comprehension
# aaa = {x**2 for x in range(10)}
# print(aaa)

# abn = {num for num in a if num <20 and num>50}
# print(abn)

# #dictionary comprehension
# di = {'a':1,'b':2,'c':3,'d':4,'e':5}
# d2 = {k:v**3 for (k,v) in di.items()}
# print(d2)

# #obtain the dictionary with each value is cubed if value v >3

# d3 = {k:v ** 3 for (k,v) in di.items() if v>3}
# print(d3)

# d3 = {k : ('even' if v %2==0 else 'odd') for (k,v )in di.items()}
# print(d3)

# lst = [num for num in range(2,51)if num %2==0  and num %4 ==0 ]
# print(lst)

# mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# c4 = *mat[0],*mat[1],*mat[2]
# print(c4)


# import random
# r = {int(15+30 * random.random())for num in range(10)}
# print(r)
# count = len({num for num in r if num < 30})
# print(count)
# s = {num for num in r if num <30}
# r = r - s 
# print(r)

# lst =[(),(),(10),(10,20),('',),(10,20,30),(40,50),(),(45)]
# lst =[tpl for tpl in lst if tpl]
# print (lst)

# s1 = 'dreames may change ,but friends are forever'
# s2 = [''.join(w.capitalize() for w in s1.split())]
# s3 =s2[0]
# print (s3)

# words = {'TUB':1,'TOOTHBRUSH':2,'TOWEL':3,'NAILCUTTER':4}
# d2 = {''.join(alpha for alpha in k if alpha not in 'aeiou'):v for (k, v ) in words.items()}
# print (d2)

# mat1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# mat2 =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# mat3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
 # #rows # using list
# for i in range(len(mat1)):
# #columns
    # for j in range(len(mat1[0])):
        # mat3[i][j]= mat1[i][j]+mat2[i][j]
# print(mat3)

# #list comprehension
# mat3 =[[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
    # for i in range(len(mat1))]
# print(mat3)

emp = {
        'A101':{'name':'Ashish','age':30,'salary':21000},
        'B102':{'name':'Dinesh','age':25,'salary':12200},
        'A103':{'name':'Ramesh','age':28,'salary':11000},
        'B104':{'name':'Akheel','age':30,'salary':18000},
        'A105':{'name':'akash','age':32,'salary':20000}
        
}
print(emp)

d1 = {k:v for(k,v) in emp.items()if k.startswith('A')}
print(d1)
d2 = {k:v['name'] for (k,v) in emp.items()}
print (d2)
d3 = {k:v ['age'] for (k,v) in emp.items()}
print(d3)
d4 = {k:v ['age'] for (k,v) in emp.items() if v['age'] > 30}
print(d4)
#d5 = {k:v ['name'] for (k,v) in emp.items() if v['name'].startswith('A')}
#

d6 = {k:v ['age']for (k,v)in emp.items() if v['age'] < 30}
print(d6)


#emp 1:

employee = {
               'A1': {'ID':'A001','name':'ram','age':34},
                'B1': {'ID':'B002','name':'shilpa','age':34},
                'C1': {'ID':'C003','name':'prutvi','age':27},
                'B1': {'ID':'D004','name':'dhruva','age':25}
}
print(employee)

d1 = [(k,v) for(k,v) in employee.items() if k.startswith('B')]
print(d1)

d10 =[(k, v) for (k, v) in employee.items() if k.startswith('B')]
print(d10)


