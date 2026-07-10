import numpy

def compute_determinant(arr):
    det = numpy.linalg.det(arr)
    return str(round(det, 2))