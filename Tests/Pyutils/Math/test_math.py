from Pyutils.Math import math

def test_sum_integers():
    result = math.sum(1, 2, 3, 4)
    assert result == 10

def test_sum_floats():
    result = math.sum(1.5, 2.5, 3.5)
    assert result == 7.5

def test_sum_mixed_types():
    result = math.sum(1, 2.5, 3, 4.5)
    assert result == 11.0

def test_sum_empty():
    result = math.sum()
    assert result == 0

def test_sum_single_value():
    result = math.sum(42)
    assert result == 42
