

class Vehicle:

    def __init__(self):
        print("Vehicle")

    def general_use(self, type):
        print(f"For Travelling via: {type}")

class Car(Vehicle):
    def __init__(self, brand, model):
        print("Car")
        self.brand = brand
        self.model = model
        self.brand = brand
        self.model = model

    def print_details_car(self):
        super().__init__()
        print(self.brand, self.model)


class TwoWheeler(Vehicle):
    def __init__(self, brand, model):
        print("TwoWheeler")
        self.brand = brand
        self.model = model

    def print_details_twowheeler(self):
        super().__init__()
        print(self.brand, self.model)


c = Car("TATA", "Safari")
c.general_use("TATA")
c.print_details_car()

print("*"*50)

b = TwoWheeler("YAMAHA", "RX-100")
b.general_use("YAMAHA")
b.print_details_twowheeler()

print("*"*50)

# Multi-Level Inheritance

class Grandparent:
    def __init__(self):
        print("Grandparent")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child")

c = Child()

print("*"*50)
