from util import check_stackability

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        blocks = list(map(int, input().split()))
        result = check_stackability(blocks)
        print(result)

if __name__ == '__main__':
    main()