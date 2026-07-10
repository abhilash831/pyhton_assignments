from util import mutate_string

def main():
    s = input()
    cmd = input("enter the index and value:").split()
    
    position = int(cmd[0])
    character = cmd[1]
    
    result = mutate_string(s, position, character)
    print(result)

if __name__ == '__main__':
    main()