import pytest
from func import scale

def test_scale():
    # with zero to multiples of range
    assert scale(0, 100, 10, 0, 1000) == 100
    assert scale(0, 100, 50, 100, 200) == 150

    # with zero to varying sizes
    assert scale(0, 30, 20, 1, 5) == 3

    # with zero to reverse
    assert scale(0, 30, 10, 30, 0) == 20

    # from non zero to varying range
    assert scale(5, 23, 8, 36, 50) == 38

    # from non zero to varying reverse
    assert scale(5, 23, 8, 50, 36) == 47

    # from different magnitudes of ranges
    assert scale(0, 1000, 500, 0, 10) == 5
    assert scale(0, 1, 0, 0, 1000) == 0

    # edge cases
    assert scale(0, 100, 100, 10, 20) == 20
    assert scale(0, 100, 0, 20, 67) == 20

    # scale a midpoint within the same range
    assert scale(0, 50, 25, 0, 100) == 50
    assert scale(0, 50, 25, 0, 200) == 100

    # scale at the upper bound
    assert scale(10, 50, 50, 0, 100) == 100
    assert scale(10, 50, 50, 50, 100) == 100

    # scale at the lower bound
    assert scale(10, 50, 10, 0, 100) == 0
    assert scale(10, 50, 10, 50, 100) == 50

