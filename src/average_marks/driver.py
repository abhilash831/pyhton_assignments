from util import calculate_average

def main():
    n = int(input())
    headers = input().split()
    data = []
    
    for i in range(n):
        row = input().split()
        data.append(row)
        
    result = calculate_average(headers, data)
    print(result)

if __name__ == '__main__':
    main()