import numpy
from src.mean_var_std.util import compute_mean_var_std

def test_compute_mean_var_std():
    arr = numpy.array([
        [1, 2],
        [3, 4]
    ])
    
    expected_output = "[ 1.5  3.5]\n[ 1.  1.]\n1.11803398875"
    assert compute_mean_var_std(arr) == expected_output