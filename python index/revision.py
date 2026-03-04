# year = int(input("Enter the year :"))
# if year%400 == 0:
#     print(f"{year} is a leap year")
# elif year%100 == 0:
#     print(f"{year} is not a leap year")
# elif year%4 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# units = int(input("Enter the number of units consumed :"))
# if units<=100:
#     electricity_bill = units*2
# elif units>100 and units<=200:
#     electricity_bill = 100*2 + (units-100)*3
# elif units>200 and units<=300:
#     electricity_bill = 100*2 + 100*3 + (units-200)*5
# print(f"The electricity bill is : {electricity_bill}")


# cart = {'cart_items': 10,
#         'total_price': 3200,
#         'address':{'d.no':'4-8-123',
#                    'street':'madhapur',
#                    'landmark':'near big bazar'}
#             }

# cart['user_type']='prime'
# cart['address']['pincode']=500821
# print(cart)


# contacts=[{'name':'harsha','ph':'9874563210'},
#           {'name':'karun','ph':'7894561230'},
#           {'name':'abhishek','ph':'6547893210'},
#           ]
# contacts[1]['status']='block'
# contacts[2]['number']='6541237890'
# print(contacts)


for num in range(1,11):
 print(f"{5} * {num} = {5*num}")