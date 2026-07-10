import numpy
from util import compute_min_max

def main():
    n, m = map(int, input().split())
    arr = numpy.array([input().split() for _ in range(n)], int)
    
    result = compute_min_max(arr)
    print(result)

if __name__ == '__main__':
    main()