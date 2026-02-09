"""
Kenneth Huang
Feb 5, 2026
Lab 5 | Functions
"""
from lab05_functions import *

print("Example 1: User Defined Functions")

height = 2
width = 10
area = area_rectangle(height, width)
display_result(height, width, area)

print("Example 2: Calculate Distance Between Two Points")

x1 = collect_number("x1")
y1 = collect_number("y1")
x2 = collect_number("x2")
y2 = collect_number("y2")

distance = calculate_distance_between_two_points(x1, y1, x2, y2)

display_distance_result(x1, y1, x2, y2, distance)

HIDDEN = generate_randomish_value(0, 100)
while True:
    guess = int(input("Guess the number!\n> "))
    if guessing_game(guess, HIDDEN):
        break
