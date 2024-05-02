# 1. Create a Product class and a Shop class.
# 2. Inside the Shop class, create a method name add_product which adds products using the 
# Product class to the Shop class.
# 3. Inside the Shop class, create a method name buy_product which is used to buy a product and 
# check whether this product is available or not. If you successfully buy a product, then throw 
# a Congress message.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shop:
    def __init__(self, name):
        self.shopName = name
        self.products = []

    def __repr__(self):
        return f"The shop name is: {self.shopName}"
    #method
    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)
    def show_all_products(self):
        for product in self.products:
            print(f"Product Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
    def buy_product(self, name, price, quantity):
        for product in self.products:
            if(product.name.lower() == name.lower() and product.price<=price and product.quantity>=quantity):
                print(f"Congratulations! You have successfully buy the product: {product.name}")
                product.quantity -= quantity
                # if quantity becomes 0 then remove that product 
                if product.quantity == 0:
                    self.products.remove(product)
                return        
        print("Sorry! Product is not available")

myShop = Shop("Glory")
print(myShop) # The shop name is: Glory
myShop.add_product("Tomato", 20, 5)
myShop.add_product("Onion", 45, 1)
myShop.add_product("Potato", 30, 3)
myShop.add_product("Egg", 130, 4)
myShop.show_all_products()  # Product Name: Tomato, Price: 20, Quantity: 5
                            # Product Name: Onion, Price: 45, Quantity: 1
                            # Product Name: Potato, Price: 30, Quantity: 3
                            # Product Name: Egg, Price: 130, Quantity: 4

myShop.buy_product('tomato', 20, 2) # Congratulations! You have successfully buy the product: Tomato
myShop.buy_product("onion", 45, 1) # Congratulations! You have successfully buy the product: Onion
myShop.buy_product("giner", 30, 1) # Sorry! Product is not available
myShop.show_all_products()  # Product Name: Tomato, Price: 20, Quantity: 3
                            # Product Name: Potato, Price: 30, Quantity: 3
                            # Product Name: Egg, Price: 130, Quantity: 4
