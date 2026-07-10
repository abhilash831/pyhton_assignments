import numpy
from util import compute_determinant

def main():
    n = int(input())
    arr = numpy.array([input().split() for _ in range(n)], float)
    
    result = compute_determinant(arr)
    print(result)

if __name__ == '__main__':
    main()