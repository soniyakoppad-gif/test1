# # # fruits = {"banana": "yellow", "strawberry": "red", "grapes": "purple"}

# # # products = {
    # # # 'Jeans': 49.99,
    # # # 'T-Shirt': 14.99,
    # # # 'Suit': 89.99,
# # # }
# # # empty = {}
# # # empty = products
# # # print(empty)

# # # products = dict(Jeans=49.99, TShirt=14.99, Suit=89.99)
# # # print(products)


# # # customers = {
    # # # 281: {
        # # # 'first_name': 'John',
        # # # 'last_name': 'Smith',
        # # # 'age': 25,
    # # # },
    # # # 704: {
        # # # 'first_name': 'Mary',
        # # # 'last_name': 'Jackson',
        # # # 'age': 32,
    # # # },
# # # }
# # # print(customers)




# # # capitals = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}
# # # print(capitals)

# # # print(type(capitals))


# # # d = {}
# # # num_names = {1.5:"one",2.5 :"Two",3.5: "Three" }
# # # print(d,num_names)

# # # roman_names = {'I': 1 ,'II':2 ,'III':3}
# # # print(roman_names)

# # # dict_obj = {"Fruit":["Mango","Banana"], "Color":["Blue", "Red"]}
# # # print(dict_obj)

# # # num_keys = {1:"one",2:"TWO",3:"Threee",4:"FOUR",5:"FIVE"}
# # # print(num_keys)

# # # emptydict = {}
# # # numdict = dict(I='one', II='two', III='three')
# # # emptydict = numdict
# # # print(emptydict)

# # numNames={1:"One", 2: "Two", 3:"Three"}
# # print(numNames[1],numNames[2],numNames[3])

# # capitals = {"USA":"Washington DC", "France":"Paris", "India":"New Delhi"}
# # print(capitals["USA"], capitals["France"],) 
# # #print(capitals["usa"])

# # capitals = {"USA":"Washington DC", "France":"Paris", "India":"New Delhi"}
# # print(capitals.get("USA"))
# # print(capitals.get("France"))

# # capitals = {"USA":"Washington DC", "France":"Paris", "India":"New Delhi"}
# # for key in capitals:
    # # print("Key = " + key + ", Value = " + capitals[key])
    # # print("Key = " +key+  ", value = " + capitals[key]) 
    
# # captains = {"England":"Root", "Australia":"Smith", "India":"Dhoni"}
# # print(captains)

# # captains['India'] ='virat'
# # captains['Australia'] = 'joshi'
# # print(captains)

# # captains['southafrica'] = 'john smith'
# # print(captains)

# # del captains['Australia']
# # print(captains)

# # del captains

# # d1 = {'name': 'Steve', 'age': 21, 'marks': 60, 'course': 'Computer Engg'}
# # print(d1.keys())
# # print(d1.values())

# captains = {'England': 'Root', 'Australia': 'Paine', 'India': 'Virat', 'Srilanka': 'Jayasurya'}

# b = 'England' in captains
# print(b)

# b = 'India' in captains
# print(b)

# boys = {
# 'nilesh': 41,'soumitra':42,'nadeem': 47,'ravi':50
# }
# girls = {
# 'seema':30,'goutami':30,'chandra':30,'rosa':50
# }
# combined = {**boys,**girls}
# print(combined)

# combined = {**girls,**boys}
# print(combined)

# #max and min value #nested dictionary
# d = {
    # 'anu': {'salary':10000,'age':20,'height':6},
    # 'adhitya':{'salary':20000,'age':25,'height':7},
    # 'rahul': {'salary':26000,'age':26,'height':77}
    # }
# lst = []
# for v in d.values():
    # lst.append(v['salary'])
# print(max(lst))
# print(min(lst))


students = {
    'anu ' :{'maths':90,'kannada':100,'ss':89},
    'sharma ' :{'maths':67,'kannada':60,'ss':40},
    'ravi' :{'maths':78,'kannada':56,'ss':80}
}
print(students)
for name, marks in students.items():
    total = sum(marks.values())          # sum of marks
    avg = total / len(marks)             # average marks
    print(f"{name} → Total = {total}, Average = {avg:.2f}")
 







