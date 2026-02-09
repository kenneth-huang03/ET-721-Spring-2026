import math
import random

# Example 1
def area_rectangle(height, width):
    return height * width

def display_result(height, width, area):
    print(f"In a rectangle with width of {width} units and height of {height} units the area is {area} units.")

# Example 2
def collect_number(coordinate_name):
    number = int(input(f"Enter a number between 1-10 for {coordinate_name}:\n> "))

    while (number <= 1 or number >= 10):
        number = int(input(f"Oops!\nPlease enter a number between 1 and 10 for {coordinate_name}:\n> "))

    return number

def calculate_distance_between_two_points(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def display_distance_result(x1, y1, x2, y2, distance):
    print(f"Distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {round(distance, 2)}")

def generate_randomish_value(min, max):
    return random.randrange(min, max)

def guessing_game(guess, actual):
    if guess < actual:
        print("The number is larger than the guess")
    elif guess > actual:
        print("The number is smaller than the guess")
    elif guess == actual:
        print("You got it!")
        return True
    else:
        print("Uhh")
    return False

