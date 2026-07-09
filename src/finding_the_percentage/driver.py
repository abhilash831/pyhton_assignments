from util import finding_percentage

def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter the Student name:")
    result=finding_percentage(student_marks,query_name)
    print(f"The average of {query_name} is {result}")

if __name__=='__main__':
    main()