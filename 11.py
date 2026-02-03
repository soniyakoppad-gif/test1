    
#17.Write a Python program to calculate the length of a string
s ="Helloworld"
print(len(s))

#2.Write a Python program to sum all the items in a list.
lst = [1,2,3,4,5]
print(sum(lst))

#3. Write a Python program to multiplies all the items in a list.
def mul_items(items):
    total = items[0]
    for x in items:
        total *=x
    return total
    
print(mul_items([1,2,3,4]))

#4.. Write a Python program to get the largest number from a list
lst = [2,3,4,56,10]
print(max(lst))

#5. Write a Python program to get the smallest number from a list.
print(min(lst))

#6. Write a Python program to count the number of characters in a string
#Sample_String = 'google.com' 

string = "google.com"
chr_count = {}  
for ch in string:
    if ch in chr_count:
        chr_count[ch] +=1
    else:
        chr_count[ch] = 1

print(chr_count)




#Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com'
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def chr_freg(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] +=1
        else:
            dict[n] =1
        return dict
        
print(chr_freg('google.com'))



#Exercise 1: Concatenate two lists index-wise


def con(list1,list2):
    if len(list1) == len(list2):
        new_list = []
        iterate =len(list1)
        for i in range(iterate):
            new_list.append(list1[i]+list2[i])
        return new_list
    else:
        return "strings must be same length"
        
        

list1 = ["M", "na", "i", "Ro"]
list2 = ["y", "me", "s", "nny"]


print(con(list1,list2))


#Exercise 2: Reverse a list in Python
list1 = [10, 9, 8, 7, 6]
x =reversed(list1)
print(list(x))

#another method

def rev_string (lst):
    new_list = []
    iterate = len(lst)
    for  i in  range(iterate):
        new_list.append(lst[iterate-1-i])
        
    return new_list
lst =[10,9,8,7,6]
print(rev_string(lst))



#Exercise 3: Concatenate two lists in the following order
#['Hello Ram', 'Hello Bhawna', 'GoodMorning Ram', 'GoodMorning Bhawna']

def long_name (list1,list2):
    if len(list1) == len(list2):
        new_list = []
        for i in list1:
            for j in list2:
                new_list.append(i+j)
                
            return new_list
          

list1 = ["Hello ", "GoodMorning "]
list2 = ["Ram", "Bhawna"]

print(long_name(list1 , list2))




#Exercise 4: Turn every item of a list into its square


def sq_num(lst):
    new_list = []
    for  i in lst:
        new_list.append(i*i)
    return new_list

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sq_num(num))   
    
#Exercise 5: Remove empty strings from the list of strings
list1 = ["Mahi", "", "Bhawna", "Kabir", "", "Gandhi"]
list1.remove("")
print(list1)

def empty (list1):
    new_list = []
    for i in list1:
       if i != "":
           new_list.append(i)
    return new_list

list1 = ["Mahi", "", "Bhawna", "Kabir", "", "Gandhi"]
print(empty(list1)) 

#Exercise 6: Iterate both lists simultaneously

def  simul (list1,list2):
    new_list = []
    if len(list1) == len(list2):
        for  i in range(len(list1)):
            print(list1[i],list2[len(list2)-i-1])
        

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

simul(list1,list2)

#Exercise 7: Extend nested list by adding the sublist


list1 = ["A", "B", ["C", ["D", "E", ["F", "G"], "K"], "L"], "M", "N"]
sub_list = ["H", "I", "J"]
list1[2][1][2].extend(sub_list)
print(list1)


#Exercise 8: Add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


list1[2][2].append(600)
print(list1)



#Exercise 9: Remove all occurrences from a list
#list1 = [5, 20, 15, 20, 25, 50, 20]


def remove (lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list
    

list1 = [5, 20, 15, 20, 25, 50, 20]
print(remove(list1))  



#Exercise 10: Replace list’s item with new value if found
#list1 = [10, 9, 8, 7, 6]
def list_num(lst,old_number,new_number):
    new_list = []
    for i in lst:    
        if i != old_number:
            new_list.append(i)
        else:
            new_list.append(new_number)
    return new_list

list1 = [10, 9, 8, 7, 6]            
print(list_num(list1,6,14))
            
    



