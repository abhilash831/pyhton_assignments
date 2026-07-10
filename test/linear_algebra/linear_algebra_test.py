import numpy
from src.linear_algebra.util import compute_determinant

def test_compute_determinant():
    arr = numpy.array([
        [1.1, 1.1],
        [1.1, 1.1]
    ])
    
    assert compute_determinant(arr) == "0.0"