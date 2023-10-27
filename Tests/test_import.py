def test_imports():
    import pydevtools
    import pydevtools.math
    import pydevtools.math.math

def test_from_imports():
    from pydevtools import math
    from pydevtools.math import math
    from pydevtools.math.math import add

def test_from_imports_alias():
    import pydevtools as pytool
    import pydevtools.math as mathpkg
    import pydevtools.math.math as mathmod
