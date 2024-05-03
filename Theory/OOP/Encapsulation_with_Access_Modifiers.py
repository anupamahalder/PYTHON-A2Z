# Example of Encapsulation and Access Modifiers

class Car:
    def __init__(self, make, model, year):
        self.make = make            # Public attribute
        self._model = model         # Protected attribute
        self.__year = year          # Private attribute

    def display_info(self):
        return f"Make: {self.make}, Model: {self._model}, Year: {self.__year}"

    # Method to update private attribute
    def update_year(self, new_year):
        self.__year = new_year

# Create an instance of the Car class
car = Car("Toyota", "Corolla", 2022)

# Access the public attribute
print(car.make) # Output: Toyota

# Access protected attribute (conventionally considered private)
print(car._model) # Output: Corolla

# Access private attribute (Name mangling)
# In Python, private attributes are not truly private, they are name-mangled to prevent accidental access
# To access private attributes, you need to use name mangling syntax.
print(car._Car__year) # 2022

# Call method to display car information
print(car.display_info()) # Make: Toyota, Model: Corolla, Year: 2022

car._Car__year = 2024 # Also we can update the private attribute (Not conventional to do this)
print(car.display_info()) # Make: Toyota, Model: Corolla, Year: 2024

# Update private attribute using public method
car.update_year(2023)
print(car.display_info()) # Make: Toyota, Model: Corolla, Year: 2023


""" 
This example illustrates encapsulation and access modifiers in Python using a 'Car' class:

Encapsulation: 
The 'Car' class encapsulates attributes ('make', '_model', '__year') and methods ('display_info', 'update_year') into a single unit.
  
Access Modifiers:
   'make':
        Public attribute, accessible and modifiable from outside the class without any restrictions.
        Public attribute, accessible using 'car.make'.

   '_model': 
        Protected attribute (conventionally considered private), accessible and modifiable from outside the class, 
        but not intended to be accessed directly. Protected attribute, accessible using 'car._model'.
        However, it's not enforced by the language and can still be accessed from outside the class.

   '__year': 
        Private attribute, intended to be accessed and modified only within the class. In Python,
        private attributes are name-mangled to prevent accidental access from outside the class.
        Private attribute, accessed using name mangling syntax 'car._Car__year' from outside the class. 
        Directly accessing or modifying private attributes from outside the class is generally discouraged in Python.

"""
