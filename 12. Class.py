

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}\tAge: {self.age}\tMarks: {self.marks}")

aj = Student("Ashish", 27, 96)
aj.display_details()

print("*"*50)

class ShoppingCart:
    def __init__(self, Cart):
        self.Cart = Cart

    def add_item(self, item):
        self.Cart.append(item)

    def remove_item(self, item):
        self.Cart.remove(item)

    def print_cart(self):
        print(f"Cart Items: {self.Cart}")


cart_item =ShoppingCart(['Milk', 'Eggs'])
cart_item.print_cart()
cart_item.add_item('Rice')
cart_item.add_item('Banana')
cart_item.print_cart()
cart_item.remove_item('Banana')
cart_item.print_cart()

print("*"*50)