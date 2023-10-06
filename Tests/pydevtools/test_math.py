import pytest
from pydevtools import math

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

# Testing the sub function
def test_sub_integers():
    result = math.sub(1, 2, 3, 4)
    assert result == -8

def test_sub_floats():
    result = math.sub(1.5, 2.5, 3.5)
    assert result == -4.5

def test_sub_mixed_types():
    result = math.sub(1, 2.5, 3, 4.5)
    assert result == -9

def test_sub_empty():
    result = math.sub()
    assert result == 0

def test_sub_single_value():
    result = math.sub(42)
    assert result == 42

def test_sub_double_value():
    result = math.sub(80,35)
    assert result == 45

# Testing the mult function
def test_mult_integers():
    result = math.mult(1, 2, 3, 4)
    assert result == 24

def test_mult_floats():
    result = math.mult(1.5, 2.5, 3.5)
    assert result == 13.125

def test_mult_mixed_types():
    result = math.mult(1, 2.5, 3, 4.5)
    assert result == 33.75

def test_mult_empty():
    result = math.mult()
    assert result == 1

def test_mult_single_value():
    result = math.mult(42)
    assert result == 42

def test_mult_double_value():
    result = math.mult(70,5)
    assert result == 350

# Testing the div function
def test_div_integers():
    result = math.div(10, 2)
    assert result == 5.0

def test_div_floats():
    result = math.div(10.5, 2.0)
    assert result == 5.25

def test_div_mixed_types():
    result = math.div(10, 2.5)
    assert result == 4.0

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = math.div(10,0)

def test_div_empty():
    result = math.div()
    assert result == 1  # Dividing by nothing should result in 1

def test_div_single_value():
    result = math.div(42)
    assert result == 42

def test_div_double_value():
    result = math.div(70,35)
    assert result == 2