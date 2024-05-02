# Example of Inheritance in Python

# Base class or Superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Unknown sound"

# Subclass inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Subclass inheriting from Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Subclass inheriting from Animal
class Cow(Animal):
    def speak(self):
        return "Moo!"

# Create instances of subclasses
dog = Dog("Doggy")
cat = Cat("Sugar")
cow = Cow("Humba")

# Call methods on instances
print(dog.name + " says: " + dog.speak()) # Doggy says: Woof!
print(cat.name + " says: " + cat.speak()) # Sugar says: Meow!
print(cow.name + " says: " + cow.speak()) # Humba says: Moo!
