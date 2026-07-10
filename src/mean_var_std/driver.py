import numpy
from util import compute_mean_var_std

def main():
    n, m = map(int, input().split())
    arr = numpy.array([input().split() for _ in range(n)], int)
    
    result = compute_mean_var_std(arr)
    print(result)

if __name__ == '__main__':
    main()