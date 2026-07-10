from util import find_day

def main():
    month, day, year = map(int, input().split())
    result = find_day(month, day, year)
    print(result)

if __name__ == '__main__':
    main()