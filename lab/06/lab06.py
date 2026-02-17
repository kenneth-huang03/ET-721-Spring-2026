"""
Kenneth Huang
Lab 6 | Classes Objects and Methods
"""

import matplotlib.pyplot as plt

print("Example 1")

class Circle(object):
    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour

    def add_to_radius(self, toAdd): 
        self.radius += toAdd
        return self.radius

class Rectangle(object):
    def __init__(self, height, width, colour):
        self.height = height
        self.width = width
        self.colour = colour 

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2

    def draw_self(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), (self.width, self.height), fc=self.colour))
        plt.axis("scaled")
        plt.plot()
        plt.show()


circle_1 = Circle(5, "Yellow")
circle_2 = Circle(2, "Red")

rectangle_1 = Rectangle(2, 3, "Green")
rectangle_2 = Rectangle(5, 4, "Blue")

print(f"The colour of circle_2 is {circle_2.colour}")
print(f"The area of rectangle_1 is {rectangle_1.height * rectangle_1.width}")
print(f"The area of rectangle_2 is {rectangle_2.height * rectangle_2.width}")

circle_2.colour = "Orange"
print(f"I changed the colour of circle_2 to {circle_2.colour}")

print(f"The radius of circle_2 is {circle_2.radius}")
circle_2.add_to_radius(6)
print(f"The new radius of circle_2 is {circle_2.radius}")

print(f"The area of rectangle_1 is {rectangle_1.area()}")
print(f"The perimeter of rectangle_2 is {rectangle_2.perimeter()}")

rectangle_2.draw_self()

print()
print()
print("Exercise")
class BankAccount: #Implicitly a child of object
    def __init__(self, account_number, account_holder, balance = 250.50):
        self.number = account_number
        self.holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Cannot deposit a value less than or equal to 0")
            return
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Cannot withdraw a value greater than your current balance")
            return
        self.balance -= amount
        return amount

    def display_balance(self):
        print(f"Current balance of Account {self.number} is ${self.balance}")

account = BankAccount(123456879, "Kenneth")
account.withdraw(700)
account.deposit(1000)
account.withdraw(500)
account.display_balance()
