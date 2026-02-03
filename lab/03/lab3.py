"""
Kenneth Huang
Febuary 3rd, 2026
Lab 3 | Conditional Statements and Loops in Python
"""
print("Example 1: if-elif-else")
age = 11
if (age >= 21 and age <= 100):
    print("You are an adult!")
elif age >= 12:
    print("You are a teenager!")
elif age > 0:
    print("You are a kid!")
else:
    print("Unable to read age!")

print("Example 2: Iterating through a range with a for loop")
for x in range(0, 9, 1): # The third argument is by default 1
    print(x)

for x in range(9, 0, -1):
    print(x)

print("Example 3: Iterating through a list with a for loop")
numbers = [3, 6, 1, -8, 9, -5]
count_negative = 0
for number in numbers:
    if number < 0:
        count_negative += 1
else:
    print(f"There is/are {count_negative} negative numbers")

print("Example 4: Using a while loop as a counter")
counter = -3
step = 2
while counter <= 5:
    print(counter)
    counter += step

print("Example 5: Using a while loop to run a program infinitely")
decision = "y"
user_input = 0
while True:
    user_input = int(input("Enter a number:\n> "))

    if user_input == 0:
        print("Input is Zero")
    elif user_input % 2 == 0:
        print("Input is Even")
    else:
        print("Input is odd")

    decision = input("Would you like to continue? (y/n) ")
    if decision != "y" and decision != "Y":
        break

"""
Lab Exercise
"""
print("Exercise 1")
user_input = 0
while True:
    user_input = int(input("Enter a whole number\n> "))
    if user_input >= 1 and user_input <= 9:
        break

print("Exercise 2")
HIDDEN = 3
guess = 0
while True:
    guess += 1

    print(f"Attempt {guess}")
    usr = int(input("Enter your guess\n> "))
    
    if usr == HIDDEN:
        print("You got it!")
        break
    else:
        print("Sorry try again")

    if guess >= 3: 
        print("Aw you failed to get it within three attempts")
        break
