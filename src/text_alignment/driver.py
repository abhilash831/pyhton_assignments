from util import generate_logo

def main():
    thickness = int(input())
    output = generate_logo(thickness)
    print(output)

if __name__ == '__main__':
    main()