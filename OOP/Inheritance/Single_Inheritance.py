class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def speed(self):
        return "This is speedy"

class Car(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

class Bike(Vehicle):
    def __init__(self, brand, model, milage):
        super().__init__(brand, model)
        self.milage = milage

toyota = Car("Toyota", "Corolla", 4)
print(toyota.capacity) # 4
print(toyota.speed()) # This is speedy
