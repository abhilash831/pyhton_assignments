from util import get_word_order

def main():
    n = int(input())
    words = []
    
    for _ in range(n):
        words.append(input().strip())
        
    result = get_word_order(words)
    print(result)

if __name__ == '__main__':
    main()