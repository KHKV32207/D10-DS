# str1 = 'something'
# x = 0
# while x<len(str1):
#     print(str1[x])
#     x+=1
    
#to print reverse the str1
# x=len(str1)-1
# while x>=0:
#     print(str1[x])
#     x-=1

#to check the ovels in str1
# x=0
# while x<len(str1):
#     if str1[x] in 'aeiou':
#        print(str1[x])
#     x+=1

#to rev a num is palindrom
# num=565
# num1=num
# rev=0
# while num>0:
#      id=num%10
#      rev=rev*10+id
#      num=num//10
# print(rev)
# if rev==num1:
#         print('it is a palindrom')
# else:
#         print('it is not a palindrom')    

# num = 158
# count = 0
# while num>0:
#     id = num%10
#     count+=1
#     num=num//10
#     print(count)



"""to find the digits in the given number"""
# x=int(input('enter the sum:'))
# count=0
# while x>0:
#     id=x%10
#     print(id)
#     count+=1
#     x=x//10
# print(count)


"""to find the perfet number"""

# num=int(input('emter the numner:'))
# sum = 0
# i=1
# while i <= num//2 :
#     if num%i==0:
#         print(i)
#         sum+=i
#     i=i+1
# if sum==num:
#     print('it is a perfect number')
# else:  
#     print('it is not a perfect number')
  
  
  
"""to find the perfect square"""
 
# num=int(input('enter the number:'))
# x=1
# is_perfect_square=False
# while x<=num//2:
#     if x*x==num:
#             is_perfect_square=True
#     x+=1
# if is_perfect_square==True:       
#     print('it is a perfect square')
# else:
#     print('it is not a perfect square')    
    
    
    
"""to check the given number armstrong or not"""
# num=int(intput('enter the number:'))
# sum=0
# x=num
# while x>0:
#     id=x%10
#     sum+=id**3
#     x=x//10
    
    
    
# h = [10,20,'python',30,50,'java']
# s1 = 0
# for c in h:
#     if type(c) == int:
#         s1+=c
# print(s1)

"""print even value multiply by 2"""

h = [10,12,13,14,15]
k = []
for x in h:
    if x%2==0:
        x*=2
        k.append(x)
    else:
        k.append(x)
print(k)            


#even index
tem = []
for x in range(len(h)):
    if x%2==0:
        tem.append(h[x]*2)
    else:
        tem.append(h[x])
print(tem)

"""without using sort find ascending order"""

res = [10,9,5,15,13]
for x in range(len(res)):
    for y in range(x+1,len(res)):
        if res[x]>res[y]:
            res[x],res[y]=res[y],res[x]
print(res)

#descending order

res = [10,9,5,15,13]
for x in range(len(res)):
    for y in range(x+1,len(res)):
        if res[x]<res[y]:
            res[x],res[y]=res[y],res[x]
print(res)