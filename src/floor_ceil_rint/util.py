import numpy

numpy.set_printoptions(legacy='1.13')

def get_floor_ceil_rint(arr):
    f = numpy.floor(arr)
    c = numpy.ceil(arr)
    r = numpy.rint(arr)
    return f"{f}\n{c}\n{r}"