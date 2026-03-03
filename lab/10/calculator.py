def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    # Testing
    print(add( 2,  3)) #   5
    print(add(-8,  5)) #  -3
    print(subtract( 7,  5)) #   2
    print(subtract(-7,  5)) # -12
    print(subtract(-7, -5)) #  -2

# Ex 1
def divide(a, b):
    if b == 0:
        raise ValueError("Division By Zero") # Pretty sure there is a DivisionByZero class already but whatever
    return a / b

if __name__ == "__main__":
    # print(divide(3, 0))
    print(divide(5, 2))

# Ex 2
def validate_password(password):
    password = password.strip()
    special = ('%' in password) or ('#' in password) or (' ' in password)

    return len(password) >= 8 and not special

if __name__ == "__main__":
    print(validate_password("peterpan"))    # true
    print(validate_password("peter pan"))   # false
    print(validate_password("peter#pan"))   # false
    print(validate_password("peter%pan"))   # false
    print(validate_password("peter$pan"))   # true
    print(validate_password("pan"))         # false

# Ex 3
def is_even(n):
    return n != 0 and n%2 == 0

if __name__ == "__main__":
    print(is_even(  8)) # true
    print(is_even( -5)) # false
    print(is_even(  0)) # false
    print(is_even(-12)) # true
    print(is_even( 11)) # false
