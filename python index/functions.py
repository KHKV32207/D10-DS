#task
# def movie(ticketsprice,ticketsquantity):
#     amount=(ticketsprice*ticketsquantity)
#     if(amount>2000):
#         return('YOU GOT A COKE+POPCORN')
#     elif (amount>1500):
#          return('YOU GOT A COKE')
#     else:
#          return('THANK YOU VISIT AGAIN')


# print(movie(600,4))
# print(movie(400,4))
# print(movie(300,4))
    
    
# def movie_tickets(price,quantity):
#     total=price*quantity
#     print(f'total amount is {total}')
#     return 'thankyou visit again'
# movie_tickets(int(input('enter tickets price:')),int(input('enter no of tickets:')))


# def showtime(name,movie):
#   print(f'{name} is watching {movie}')
#   return 'thankyou visit again'
# showtime('sruthi','og')
# print(showtime('harsha','avengers'))



"""find the perfect square and perfect number using functions"""

def perfect_square(x,):
    y=1
    is_perfect_square=False
    while y<=x//2:
        if y*y==x:
            is_perfect_square=True
        y+=1
    if is_perfect_square==True:
        print('it is a perfect square')
    else:
        print('it is not a perfect square')        
perfect_square(9)
perfect_square(16)
perfect_square(10)        
        
def perfect_number(x):
    y=1
    sum=0
    while y<=x//2:
        if x%y==0:
            sum+=y
        y+=1
    if x==sum:
        print('it is a perfect number')
    else:
        print('it is not a perfect number')
 
perfect_number(6)
perfect_number(28)   
perfect_number(27)
