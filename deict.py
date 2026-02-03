d = {}
d = {'a101': 'jhon','b101':'ksjmw','c101':'jweif'}
print(d)
print(type(d))

a ={10 : 'A',20 :'B' ,30:'C'}
print(a)

aa ={10 : 'A',20 :'B' ,10:'C'}
print(aa)

aa ={10 : 'A',20 :'B' ,10:'A'}
print(aa)

d = {'a101': 'jhon','b101':'ksjmw','c101':'jweif'}
print(d)

print(d['b101'])


#looping thruogh the dictionaries

d = {'A':'1010','B':'1011','C':'1011','D':'1111'}
for k,v in d.items():
    print(k,v)
    
for k in d.items():
     print(k)
 
d = {'name':'rahon','age':'30' , 'city':'bangalore'}
for k in d:
     print(k)
     
     
courses = {'name':'rahon','age':'30' , 'city':'bangalore'}
for i,(k,v) in enumerate(courses.items()):
    print(i,k,v)
print()

#built in functions
b = {'0oo1':'rahon','0oo2':'30' , '0oo3':'bangalore','0oo4':'indian'}
print(len(b))
print(max(b))
print(min(b))
print(any(b))
print(all(b))
print(sorted(b))
rev = reversed(b)
print(list(rev))


courses = {'cs101': 'CPP','CS201': 'SOP','CS301': 'AOP','CS401':'SOP'}
for k,v in reversed (courses.items()):
    print(k,v)


c = {'cs101': 'CPP','CS201': 'SOP','CS301': 'AOP','CS401':'SOP'}
dd = {'0oo1':'rahon','0oo2':'30' , '0oo3':'bangalore','0oo4':'indian'}
print(c.get('cs101','Absent'))
print(dd.get('cs401','passed n entered to the classroom'))
print(dd['0oo2'])

print(c.update(d))
print(c.popitem())
print(c.pop('cs101'))
print(c.clear())

contacts = {
    'anil' : {'DOB':'17/3/2021','Favorities':'igloo'},
    'amol' : {'DOB':'17/3/2023','Favorities':'tungloo'},
    'ravi' : {'DOB':'21/12/2021','Favorities':'artic'}
    
}
print(contacts)

animals = {'tiger': 141,'lion' : 152,'leapard': 110}
birds = {'eagle':38,'crow':3,'parrot':2}
combined = {**animals,**birds}
print(combined)


#1 .
student = {
    'anil ' : 20,'sharma':25 , 'thaisan':27,'rose':30 , 'ram':26
}
stud = student
student = {}
print(stud)

#2.
cricketer = {'sunil','virat','dhoni','sachin','rohit sharma'}
d = dict.fromkeys(cricketer,50)
print(len(cricketer))
print(len(d))
print(d)

#3.
import operator
d = {'oil': 230,'clip':150,'stud':175,'nut':35}
print(d)

#sorting by its keys

d1 = sorted(d.items())
print('assending order',d1)

d2 =sorted(d.items(),reverse=True)
print(d2)

#sorted by its values

d3 = sorted(d.items(),key = operator.itemgetter(1))
print(d3)

d4 = sorted(d.items(),key = operator.itemgetter(1),reverse=True)
print(d4)

#4

d1 = {'mango':30,'apple':50}
d2 = {'banana':40,'mango':60}
d3 = {'kiwi':90,'pinapaple':50}
d4 = {}
for d in (d1,d2,d3):
    d4.update(d)
    print(d4)
    
d5 = {**d1,**d2,**d3}
print(d5)
d6 = list((*d1,*d2,*d3))
print(d6)


d1 = {'anil': 40, 'smol' : 35}
if bool(d1):
   print( "dictionary is not empty")
d2 = {}
if not bool(d2):
    print("dictionary is empty")

