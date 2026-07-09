from util import find_runner_up

def main():
    n = int(input("Enter the number of students: "))

    scores = list(map(int, input("Enter the scores: ").split()))

    find_runner_up(scores)

if __name__ == "__main__":
    main()