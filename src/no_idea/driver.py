from util import calculate_happiness

def main():
    n, m = input().split()
    arr = input().split()
    set_a = set(input().split())
    set_b = set(input().split())
    
    result = calculate_happiness(arr, set_a, set_b)
    print(result)

if __name__ == '__main__':
    main()