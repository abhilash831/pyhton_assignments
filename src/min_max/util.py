import numpy

def compute_min_max(arr):
    min_arr = numpy.min(arr, axis=1)
    max_val = numpy.max(min_arr)
    return str(max_val)