# #Exercise 1: Calculate the multiplication and sum of two numbers
# num1 = 20
# num2 = 30
# print(num1 * num2)
# number1 = 40
# number2 = 30
# print(number1 + number2)

# #xercise 2: Print the Sum of a Current Number and a Previous number
# s = 0
# for i in range(0,11):
    # sum = s + i 
    # print(sum)
# s = i 

# #xercise 3: Print characters present at an even index number
# str = "PYnativetyui"
# print(str[0::2])
# size = len(str)
# for i in range(0, size - 1, 2):
    # print(str[i]) 
    

# #xercise 5: Check if the first and last numbers of a list are the same   

# first_num = numbers_list[0]
# last_num = numbers_list[-1]
# if first_num == last_num:           
    # return True
# else:
    # return False
        
# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))

# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))



lst = [1,2,3,4,5,6]
# for i in range(0,len(lst)):
    # for j in range(i,len(lst)):
        # if i != j:
            # print((lst[i],lst[j]))
            


lst = [1,2,3,4,5]



for i in range(len(lst) - 1):
    total = sum(lst[i+1:])
    for j in range(i+1, len(lst)):
        print((lst[i], total))
        total -= lst[j]
    print((lst[i], 0))
   
        
    
lst = [1, 2, 3, 4, 5]

for i in range(len(lst) - 1):
    total = 0
    
    # calculate sum of elements after lst[i]
    for k in range(i + 1, len(lst)):
        total = total + lst[k]

    # print required pairs
    for j in range(i + 1, len(lst)):
        print((lst[i], total))
        total = total - lst[j]

    print((lst[i], 0))

        
            
            
           
            




