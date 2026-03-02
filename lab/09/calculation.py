"""
Kenneth Huang
Lab 9 | Unit Testing
Feb 26th, 2026
"""

def add_three_numbers(n1 = 0, n2 = 0, n3 = 0):
    return n1 + n2 + n3

def subtract_two_numbers(n1 = 0, n2 = 0):
    return n1 - n2

def multiply_three_numbers(n1 = 1, n2 = 1, n3 = 1):
    return n1 * n2 * n3

def divide_two_numbers(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("ERROR! Cannot divide by ZERO")
    except ValueError:
        print("ERROR! Input is Not a Number")
    except:
        print("ERROR! Cannot divide the inputs")
    return


