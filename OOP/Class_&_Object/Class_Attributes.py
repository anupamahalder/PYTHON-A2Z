class Product:
    # constructor 
    def __init__(self, name, price):
        # creating instance attributes 
        self.name = name
        self.price = price
    # when print the class we want to print a string
    def __repr__(self):
        return f"(Name: {self.name}, Price: {self.price})"

class Shop:
    # class attribute (which is shared in all instances)
    products = [] #empty list initially
    # constructor
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"The shop name is: {self.name}"

    # method to add products on products list
    def add_products(self, name, price):
        product = Product(name, price)
        self.products.append(product)

# create an instance of Shop class
my_shop = Shop("Tasty Cafe")
print(my_shop) # The shop name is: Tasty Cafe

# add products 
my_shop.add_products("Water", 20)
my_shop.add_products("Mixer", 50000)
my_shop.add_products("Coffee maker", 3000)
my_shop.add_products("Tea bags", 900)

# print the products
print(my_shop.products) # [(Name: Water, Price: 20), (Name: Mixer, Price: 50000), (Name: Coffee maker, Price: 3000), (Name: Tea bags, Price: 900)]

your_shop = Shop("Yummy Cafe")
print(your_shop) # The shop name is: Yummy Cafe

# add products 
your_shop.add_products("Chicken", 3000)
your_shop.add_products("Peanut", 7000)

# print the products 
print(your_shop.products) # [(Name: Water, Price: 20), (Name: Mixer, Price: 50000), (Name: Coffee maker, Price: 3000), (Name: Tea bags, Price: 900), (Name: Chicken, Price: 3000), (Name: Peanut, Price: 7000)]
