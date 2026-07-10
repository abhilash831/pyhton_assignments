import numpy
from util import get_floor_ceil_rint

def main():
    arr = numpy.array(input().split(), float)
    result = get_floor_ceil_rint(arr)
    print(result)

if __name__ == '__main__':
    main()