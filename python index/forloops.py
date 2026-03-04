# #for n in range(1,21):
#     #if (n%3==0):
#         #print(f"{n} - fizz")
#     #if (n%5==0):
#         #print(f"{n} - buzz")
#     #if (n%3==0 and n%5==0):
#         #print(f"{n} - fizzbuzz")
#     #else:
#         #print(f"{n} - not divisible by 3 and 5")           
        
# #str1 = "data science"
# #print(str1[0])
# #print(str1[1])
# #for char in str1:
#     #print(char)
 
# #wap to print the multiplication table of 2 from 1 to 10    
# #for i in range(1,11):
#     #print(f"{2} x {i} = {2*i}")
# #to print the multiplication table of 2 from 1 to 10 in reverse order   
# #for i in range(10,0,-1):
#     #print(f"{2} x {i} = {2*i}")
    
# list1 = [10,23,45,31,24,67,87,45]
# #for x  in list1:  
#     #print(x)
# #print values for the list which indeces of 3rd to 6th
# #for i in range(3,6):
#     #print(list1[i])  
# #to print the elements in the list in reverse order
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i])         

# names = ['harsha','karun','kiran','abhishek']
#to print the even lenght name in the list
# for name in names:
#     if len(name)%2==0:
#         print(name)
#to print the odd lenght name in the list
#  for name in names:
#      if len(name)%2!=0:
#          print(name)   
#  for name in names:
#      if len(name)%2==0:
#          print(f"{name} - even")
#       else:
#           print(f"{name} - odd")


# str1="SOMETHING IS FISHY"
# x=1
# for char in str1:
#  print(char,str1[x])
# x+=1


# str1="DATA"
# for char in str1:
#     print(f"{char}-hello")


# list1=[2,3,4,5,6,7]
# for i in list1:
#     print(f"square of {i} is {i**2}")

"""to get lenght of each name in the list"""

# list1=['harsha','karun','kiran','karthik','shiva']
# for char in list1:
#     print(f"length of {char} is {len(char)}")

"""to multiply each element in the list with its indes"""
# nums=[3,4,5,6,7,8,9,10]
# x=0
# for i in nums:
#     print(i*nums[x])
#     x+=1
        

"""to count occurences of each character in the string""" 
# str1="BANANA"
# char_count={}       
# for char in str1:
#     if char in char_count:
#        char_count[char]+=1
#     else:
#         char_count[char]=1           
# print(char_count)


"""to get list of string in lower case to upper case and vice versa"""
# list1=['harsha','KARUN','kiran','KARITHIK','shiva']
# for name in list1:
#     if name==name.lower():
#         print(name.upper())
#     else:
#         print(name.lower())    


# list1=['harsha','KARUN','kiran','KARITHIK','shiva']
# op=[]
# for char in list1:
#     if char==char.upper():
#         op+=[char.lower()]
#     else:
#         op+=[char.upper()]    
# print(op)


# list1='sOmEtHiNg'
# op=''
# for char in list1:
#     if char==char.upper():
#         op+=char.lower()
#     else:
#         op+=char.upper()   
# print(op)
        
    
"""find the factorial of given number"""    
num=int(input("enter the number:"))
fact=1
for i in range(num,0,-1):
    fact=fact*i
    print(fact)
    
        
    