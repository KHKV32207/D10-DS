class Product:
    def __init__(self,id,name,price,rating):
        self.id = id
        self.name = name
        self.price = price
        self.rating = rating

class User:
    def __init__(self):
        self.products = []

    def add_product(self):
        id = int(input('Enter Product ID: ')) # 3
        for product in self.products:
            if product.id == id:
                print('Product with this ID is already Exist..!')
                return
        name = input('Enter Product Name: ')
        price = int(input('Enter Product Price:'))
        rating = float(input('Enter Product Rating: '))
        product = Product(id,name,price,rating)
        self.products.append(product)
        print('Product is Successfully Added..!')

    def remove_product(self):
        if len(self.products) == 0:
            print('No Product Available..!')
            return
        
        id = int(input('Enter Product ID: ')) 
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                print('Product is Removed Successfully..!')
                return
        print("Product with this id doesn't exist..!")

    def update_product(self):
        if len(self.products) == 0:
            print('No Product Available..!')
            return
        
        id = int(input('Enter Product ID: ')) 
        for product in self.products:
            if product.id == id:
                while True:
                    print('\nSELECT -> 1 TO UPDATE NAME')
                    print('SELECT -> 2 TO UPDATE PRICE')
                    print('SELECT -> 3 TO UPDATE RATING')
                    print('SELECT -> 4 TO UPDATE ALL DETAILS')
                    print('SELECT -> 5 TO PROCEED WITH THE CHANGES')

                    choice = int(input('Enter your choice: '))
                    match choice:
                        case 1: 
                            new_name = input('Enter New Name: ')
                            product.name = new_name
                            print('Product name is updated successfully..!')
                        case 2:
                            new_price = int(input('Enter New Price: '))
                            product.price = new_price
                            print('Product price is updated successfully..!')
                        case 3:
                            new_rating = float(input('Enter New Rating: '))
                            product.rating = new_rating
                            print('Product rating is updated successfully..!')
                        case 4:
                            new_name = input('Enter New Name: ')
                            new_price = int(input('Enter New Price: '))
                            new_rating = float(input('Enter New Rating: '))
                            product.name,product.price,product.rating = new_name,new_price,new_rating
                            print('All details updated successfully..!')
                        case 5:
                            print('New Chnages reflected in your product..!')
                            return
                        case _:
                            print('Invalid Choice, Try Again..!')
        print("Product with this id doesn't exist..!")    

    def show_products(self):
        if len(self.products) == 0:
            print('No Product Available..!')
            return
        
        print('-'*38)
        print('|  ID  |  NAME  |  PRICE  |  RATING  |')
        print('-'*38)
        for product in self.products:
            print(f'|  {product.id}  |  {product.name}  |  {product.price}  |  {product.rating}  |')
        print('-'*38)
        
    def search_product(self):
        if len(self.products) == 0:
            print('No Product Available..!')
            return
        
        id = int(input('Enter Product ID: '))
        for product in self.products:
            if product.id == id:
                print('-'*38)
                print('|  ID  |  NAME  |  PRICE  |  RATING  |')
                print('-'*38)
                print(f'|  {product.id}  |  {product.name}  |  {product.price}  |  {product.rating}  |')
                print('-'*38)
                return
        print("Product with this id doesn't exist..!")     
        
    def sort_price(self):
        if len(self.products) == 0:
            print('No Product Available..!')
            return
        
        self.products.sort(key=lambda product:product.price,reverse=False)
        print('Product prices are sorted from Low to High..!') 
        
    def sort_rating(self):
        if len(self.products) == 0:
            print('No Product Available..!')
            return
        
        self.products.sort(key=lambda product:product.rating,reverse=True)
        print('Product ratings are sorted from High to Low..!') 
        
    def sort_id(self):
        if len(self.products) == 0:
            print('No Product Available..!')
            return
        
        self.products.sort(key=lambda product:product.id,reverse=False)
        print('Product IDs are sorted from Low to High..!') 
        
    def range_search(self):
        if len(self.products) == 0:
            print('No Product Available..!')
            return
        
        min_price = int(input('Enter Minimum price:'))
        max_price = int(input('Enter Maximum price:'))
        print('-'*38)
        for product in self.products:
            if min_price <= product.price <= max_price:
                print(f'|  {product.id}  |  {product.name}  |  {product.price}  |  {product.rating}  |')
        print('-'*38)


print('<---------- PRODUCT MANAGEMENT SYSTEM ---------->')
user = User()

while True:
    print('\nSELECT -> 1 TO ADD PRODUCT')
    print('SELECT -> 2 TO REMOVE PRODUCT')
    print('SELECT -> 3 TO UPDATE PRODUCT')
    print('SELECT -> 4 TO SHOW ALL PRODUCTS')
    print('SELECT -> 5 TO SEARCH A PRODUCT')
    print('SELECT -> 6 TO SORT PRODUCT PRICES')
    print('SELECT -> 7 TO SORT PRODUCT RATINGS')
    print('SELECT -> 8 TO SORT PRODUCT IDs')
    print('SELECT -> 9 TO SEARCH PRODUCT IN A PRICE RANGE')
    print('SELECT -> 10 TO EXIT FROM THE APP')

    choice = int(input('Enter your choice: '))
    match choice:
        case 1: user.add_product()
        case 2: user.remove_product()
        case 3: user.update_product()
        case 4: user.show_products()
        case 5: user.search_product()
        case 6: user.sort_price()
        case 7: user.sort_rating()
        case 8: user.sort_id()
        case 9: user.range_search()
        case 10:
            print('THANK YOU, VISIT AGAIN')
            break
        case _:
            print('Invalid Choice, Try Again..!')