# Example of Method Overriding

class Animal:
    def speak(self):
        return "Unknown sound"
    
    def eat(self):
        return "Eat something"

class Dog(Animal):
    def speak(self):
        return "Vow vow"

class Cat(Animal):
    def eat(self):
        return "Eat fish"

# Create instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Call the speak() method on instances
print(animal.speak())  # Output: Unknown sound
print(animal.eat())    # Output: Eat something

print(dog.speak())     # Output: Vow vow
print(dog.eat())       # Output: Eat something

print(cat.speak())     # Output: Unknown sound 
print(cat.eat())       # Output: Eat fish

""" 

In this example,
    1. The Dog class overrides the speak() method inherited from the Animal class. When dog.speak() is called, 
    it invokes the speak() method defined in the Dog class, which returns "Vow vow" instead of the default 
    "Unknown sound" returned by the Animal class.

    2. The Cat class overrides the eat() method inherited from the Animal class. When cat.eat() is called,
    it invokes the eat() method defined in the Cat class, which returns "Eat fish" instead of the default 
    "Eat something" returned by the Animal class.

This demostrate method overriding, where the subclass provides its own implementation of a method defined
in the superclass.

"""
