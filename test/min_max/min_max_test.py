import numpy
from src.min_max.util import compute_min_max

def test_compute_min_max():
    arr = numpy.array([
        [2, 5],
        [3, 7],
        [1, 3],
        [4, 0]
    ])
    
    assert compute_min_max(arr) == "3"