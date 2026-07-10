from util import get_valid_emails

def main():
    n = int(input())
    emails = [input() for _ in range(n)]
    
    result = get_valid_emails(emails)
    print(result)

if __name__ == '__main__':
    main()