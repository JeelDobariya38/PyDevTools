from pydevtools.math import arithmetic

# Test for the add function
def test_add():
    assert arithmetic.add(3, 4) == 7
    assert arithmetic.add(-2, 5) == 3
    assert arithmetic.add(0, 0) == 0

# Test for the sub function
def test_sub():
    assert arithmetic.sub(5, 3) == 2
    assert arithmetic.sub(-2, -5) == 3
    assert arithmetic.sub(0, 0) == 0

# Test for the mul function
def test_mul():
    assert arithmetic.mul(2, 3) == 6
    assert arithmetic.mul(-4, 5) == -20
    assert arithmetic.mul(0, 7) == 0

# Test for the div function
def test_div():
    assert arithmetic.div(8, 2) == 4
    assert arithmetic.div(-9, 3) == -3
    assert arithmetic.div(0, 7) == 0

# Test for the rem function
def test_rem():
    assert arithmetic.rem(8, 3) == 2
    assert arithmetic.rem(-9, 4) == 3
    assert arithmetic.rem(7, 7) == 0

# Test for the pow function
def test_pow():
    assert arithmetic.pow(2, 3) == 8
    assert arithmetic.pow(5, 0) == 1
    assert arithmetic.pow(4, -2) == 0.0625

# Test for the sqrt function
def test_sqrt():
    assert arithmetic.sqrt(9) == 3
    assert arithmetic.sqrt(25) == 5
    assert arithmetic.sqrt(16) == 4

# Test for the cbrt function
def test_cbrt():
    assert arithmetic.cbrt(8) == 2
    assert arithmetic.cbrt(27) == 3
    assert arithmetic.cbrt(64) == 4
