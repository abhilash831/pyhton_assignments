import numpy

numpy.set_printoptions(legacy='1.13')

def compute_mean_var_std(arr):
    mean_val = numpy.mean(arr, axis=1)
    var_val = numpy.var(arr, axis=0)
    std_val = round(numpy.std(arr, axis=None), 11)
    
    return f"{mean_val}\n{var_val}\n{std_val}"