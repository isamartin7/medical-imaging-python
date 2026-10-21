import pytest

def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


def test_divide_by_zero():
   with pytest.raises(ZeroDivisionError) as e:
    num = 1 / 0

    assert 'division by zero' in str(e.value)


# Multiplications test ideas:
# two position integers
# identity: multiply by 1
# zero: multiply by 0
# positive by negative
# negative by negative
# floats


products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]

@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a,b,product):
    assert a * b == product
