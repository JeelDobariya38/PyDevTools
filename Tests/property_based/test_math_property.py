from pydevtools.math import math
from random import randrange, randint

def test_addition_poperty():
    for i in range(100):
        a = randint(1,999)
        b = randint(1,999)
        c = randint(1,999)

        assert math.add(a, b) == math.add(b, a) # a + b = b + a
        assert math.add(a,(-1 * a)) == 0 # a + (-a) = 0
        assert math.add(a, 0) == a # a + 0 = a
        assert math.add(math.add(a, b), c) == math.add(a, math.add(b,c)) # (a + b) + c = a + (b + c)
        assert a * math.add(b, c) == math.add(a*b, a*c) # a * (b + c) = a*b + a*c

def test_subtraction_poperty():
    for i in range(100):
        a = randint(1,999)
        b = randint(1,999)
        c = randint(1,999)

        if a-b != 0:
            assert math.sub(a, b) != math.sub(b, a) # a - b != b - a
            assert math.sub(a,(-1 * a)) == 2*a # a - (-a) = 2(a)
            assert math.sub(a, 0) == a # a - 0 = a
            assert math.sub(math.sub(a, b), c) != math.sub(a, math.sub(b,c)) # (a - b) - c = a - (b - c)
            assert a * math.sub(b, c) == math.sub(a*b, a*c) # a * (b - c) = a*b - a*c

def test_multiplication_poperty():
    for i in range(100):
        a = randint(1,999)
        b = randint(1,999)
        c = randint(1,999)

        assert math.mult(a, b) == math.mult(b, a) # a * b = b * a
        assert math.mult(a, 0) == 0 # a * 0 = 0
        assert math.mult(math.mult(a, b), c) == math.mult(a, math.mult(b,c)) # (a * b) * c = a * (b * c)

def test_division_poperty():
    for i in range(100):
        a = randint(1,999)
        b = randint(1,999)
        c = randint(1,999)

        assert math.div(a,(-1 * a)) == -1 # a / -1 / a =  -1
