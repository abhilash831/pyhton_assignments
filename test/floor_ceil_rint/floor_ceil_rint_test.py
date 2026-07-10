import numpy
from src.floor_ceil_rint.util import get_floor_ceil_rint

def test_get_floor_ceil_rint():
    arr = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
    
    expected_output = (
        "[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]\n"
        "[  2.   3.   4.   5.   6.   7.   8.   9.  10.]\n"
        "[  1.   2.   3.   4.   6.   7.   8.   9.  10.]"
    )
    
    assert get_floor_ceil_rint(arr) == expected_output