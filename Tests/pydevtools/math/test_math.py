import pytest
from pydevtools.math import math

# Testing the add function
class Test_Add_Function:
    def test_add_integers(self):
        result = math.add(1, 2, 3, 4)
        assert result == 10

    def test_add_floats(self):
        result = math.add(1.5, 2.5, 3.5)
        assert result == 7.5

    def test_add_mixed_types(self):
        result = math.add(1, 2.5, 3, 4.5)
        assert result == 11.0

    def test_add_empty(self):
        result = math.add()
        assert result == 0

    def test_add_single_value(self):
        result = math.add(35,80)
        assert result == 115

    def test_add_double_value(self):
        result = math.add(42,55)
        assert result == 97

# Testing the sub function
class Test_Sub_Function:
    def test_sub_integers(self):
        result = math.sub(1, 2, 3, 4)
        assert result == -8

    def test_sub_floats(self):
        result = math.sub(1.5, 2.5, 3.5)
        assert result == -4.5

    def test_sub_mixed_types(self):
        result = math.sub(1, 2.5, 3, 4.5)
        assert result == -9

    def test_sub_empty(self):
        result = math.sub()
        assert result == 0

    def test_sub_single_value(self):
        result = math.sub(42)
        assert result == 42

    def test_sub_double_value(self):
        result = math.sub(80,35)
        assert result == 45

# Testing the mult function
class Test_Mult_Function:
    def test_mult_integers(self):
        result = math.mult(1, 2, 3, 4)
        assert result == 24

    def test_mult_floats(self):
        result = math.mult(1.5, 2.5, 3.5)
        assert result == 13.125

    def test_mult_mixed_types(self):
        result = math.mult(1, 2.5, 3, 4.5)
        assert result == 33.75

    def test_mult_empty(self):
        result = math.mult()
        assert result == 1

    def test_mult_single_value(self):
        result = math.mult(42)
        assert result == 42

    def test_mult_double_value(self):
        result = math.mult(70,5)
        assert result == 350

# Testing the div function
class Test_Div_Function:
    def test_div_two_integers(self):
        result = math.div(10, 2)
        assert result == 5
    
    def test_div_integers(self):
        result = math.div(10, 2, 7)
        assert result == 0.7142857142857143

    def test_div_floats(self):
        result = math.div(10.5, 2.0)
        assert result == 5.25

    def test_div_mixed_types(self):
        result = math.div(10, 2.5)
        assert result == 4.0

    def test_div_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            result = math.div(10,0)

    def test_div_empty(self):
        result = math.div()
        assert result == 1  # Dividing by nothing should result in 1

    def test_div_single_value(self):
        result = math.div(42)
        assert result == 42

    def test_div_double_value(self):
        result = math.div(70,35)
        assert result == 2

class Test_Rem_Function:
    def test_rem_integers(self):
        result = math.rem(10, 2)
        assert result == 0

    def test_rem_floats(self):
        result = math.rem(10.5, 2.0)
        assert result == 0.5

    def test_rem_mixed_types(self):
        result = math.rem(10, 2.5)
        assert result == 0.0

    def test_rem_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            result = math.rem(10,0)

    def test_rem_double_value(self):
        result = math.rem(70,35)
        assert result == 0