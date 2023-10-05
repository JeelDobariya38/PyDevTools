import pytest
from Pyutils.Math import math

# Testing the add function
def test_add_integers():
    result = math.add(1, 2, 3, 4)
    assert result == 10

def test_add_floats():
    result = math.add(1.5, 2.5, 3.5)
    assert result == 7.5

def test_add_mixed_types():
    result = math.add(1, 2.5, 3, 4.5)
    assert result == 11.0

def test_add_empty():
    result = math.add()
    assert result == 0

def test_add_single_value():
    result = math.add(35,80)
    assert result == 115

def test_add_double_value():
    result = math.add(42,55)
    assert result == 97

# Testing the subtract function
def test_subtract_integers():
    result = math.subtract(1, 2, 3, 4)
    assert result == -8

def test_subtract_floats():
    result = math.subtract(1.5, 2.5, 3.5)
    assert result == -4.5

def test_subtract_mixed_types():
    result = math.subtract(1, 2.5, 3, 4.5)
    assert result == -9

def test_subtract_empty():
    result = math.subtract()
    assert result == 0

def test_subtract_single_value():
    result = math.subtract(42)
    assert result == 42

def test_subtract_double_value():
    result = math.subtract(80,35)
    assert result == 45

# Testing the multiply function
def test_multiply_integers():
    result = math.multiply(1, 2, 3, 4)
    assert result == 24

def test_multiply_floats():
    result = math.multiply(1.5, 2.5, 3.5)
    assert result == 13.125

def test_multiply_mixed_types():
    result = math.multiply(1, 2.5, 3, 4.5)
    assert result == 33.75

def test_multiply_empty():
    result = math.multiply()
    assert result == 1

def test_multiply_single_value():
    result = math.multiply(42)
    assert result == 42

def test_multiply_double_value():
    result = math.multiply(70,5)
    assert result == 350

# Testing the divide function
def test_divide_integers():
    result = math.divide(10, 2)
    assert result == 5.0

def test_divide_floats():
    result = math.divide(10.5, 2.0)
    assert result == 5.25

def test_divide_mixed_types():
    result = math.divide(10, 2.5)
    assert result == 4.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = math.divide(10,0)

def test_divide_empty():
    result = math.divide()
    assert result == 1  # Dividing by nothing should result in 1

def test_divide_single_value():
    result = math.divide(42)
    assert result == 42

def test_divide_double_value():
    result = math.divide(70,35)
    assert result == 2