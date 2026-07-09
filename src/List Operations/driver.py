from util import perform_operation

def main():
    arr = []

    n = int(input("Enter the number of commands: "))

    for _ in range(n):
        cmd = input("Enter command: ").split()
        perform_operation(arr, cmd)

if __name__ == "__main__":
    main()