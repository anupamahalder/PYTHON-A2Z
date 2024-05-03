# Example of Operator Overlaoding

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # for adding we need two things
    def __add__(self, other):
        # returning a new object 
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)
    

# Create two Point objects
point1 = Point(1, 2)
point2 = Point(3, 4)

# Use the + operator to add two Point objects
result = point1 + point2
print(f"X = {result.x}, Y = {result.y}")  # Output: X = 4, Y = 6

# Use the - operator to subtract two Point objects
res = point1 - point2
print(f"X = {res.x}, Y = {res.y}") # Output: X = -2, Y = -2

# Use the * operator to multiply two Point objects
ans = point1 * point2
print(f"X = {ans.x}, Y = {ans.y}") # Output: X = 3, Y = 8

""" 
In this example, 
1. The __add__ method is defined to overload the + operator for the Point class. 
When point1 + point2 is called, it internally invokes the __add__ method, and the resulting Point object 
contains the sum of the x and y coordinates of the two points.

2. The __sub__ method is defined to overload the - operator for the Point class.
When point1 - point2 is called, it internally invokes the __sub__ method, and the resulting Point object
contains the subtraction of the x and y coordinates of the two points.

3. The __mul__ method is defined to overload the * operator for the Point class.
When point1 * point2 is called, it internally invokes the __mul__ method, and the resulting Point object 
contains the multiplication of the x and y coordinates of the two points.
"""
