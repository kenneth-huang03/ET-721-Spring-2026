"""
Kenneth Huang
Tuesday, March 3rd, 2026
Lab 10 | Unit Testing Using PyTest
"""
import pytest

from calculator import *

def test_add():
    assert add( 2,  3) ==  5
    assert add(-8,  5) == -3

def test_sub():
    assert subtract( 7,  5) ==   2
    assert subtract(-7,  5) == -12
    assert subtract(-7, -5) ==  -2

def test_divide():
    assert divide( 5,  2) == 2.5
    assert divide(10,  2) == 5

def test_divide_division_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

def test__validate_password():
    assert validate_password("peter$pan") is True

def test_validate_password_short():
    assert validate_password("pan") is False

def test_validate_password_invalid_special():
    assert validate_password("peter#pan") is False

@pytest.mark.parametrize("input, expect", [
        (  8, True ),
        ( -5, False),
        (  0, False),
        (-12, True ),
        ( 11, False),
])
def test_is_even(input, expect):
    assert is_even(input) == expect

@pytest.mark.parametrize("input, expect", [
        ("   peterpan       ",  True),
        ("peterpan",            True),
        ("peter pan",           False),
        ("peter#pan",           False),
        ("peter%pan",           False),
        ("peter$pan",           True),
        ("pan",                 False),
])
def test_validate_password(input, expect):
    assert validate_password(input) == expect
