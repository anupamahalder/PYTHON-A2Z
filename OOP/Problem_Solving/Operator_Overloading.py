# class Person:
#     def __init__(self, name, age, height, weight) -> None:
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight

# class Cricketer(Person):
#     def __init__(self, name, age, height, weight) -> None:
#         super().__init__(name, age, height, weight)

# sakib = Cricketer('Sakib', 38, 68, 91)
# musfiq = Cricketer('Rahim', 36, 68, 88)
# kamal = Cricketer('Kamal', 39, 68, 94)
# jack = Cricketer('Jack', 38, 68, 91)
# kalam = Cricketer('Kalam', 37, 68, 95)

# ---Problems---
# Find out which of these players is older using the operator overloading.

class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    # class attribute 
    persons = []

    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)
        # Append the current object to the persons list
        Cricketer.persons.append(self)
        
    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __ne__(self, other):
        return self.age != other.age
    
    def __eq__(self, other):
        return self.age == other.age

sakib = Cricketer('Sakib', 32, 68, 91)
musfiq = Cricketer('Rahim', 32, 68, 88)
kamal = Cricketer('Kamal', 31, 68, 94)
jack = Cricketer('Jack', 35, 68, 91)
kalam = Cricketer('Kalam', 33, 68, 95)

older_cricketer = max(Cricketer.persons)
print(older_cricketer.name)
