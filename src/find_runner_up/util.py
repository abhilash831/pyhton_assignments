def find_runner_up(scores):
    highest_score = scores[0]

    for mark in scores:
        if mark > highest_score:
            highest_score = mark

    second_highest = []

    for mark in scores:
        if mark < highest_score:
            second_highest.append(mark)

    second_highest_score = second_highest[0]

    for mark in second_highest:
        if mark > second_highest_score:
            second_highest_score = mark

    print(f"The runner-up score is {second_highest_score}")















































# n=int(input("Enter the number of students:"))
# A=[]
# for item in range(n):
#     marks=int(input("Enter the marks of the student:"))
#     A.append(marks)
# highest_score=0
# for mark in A:
#     if mark >highest_score:
#         highest_score=mark
# second_highest=[]
# for mark in A:
#     if mark<highest_score:
#         second_highest.append(mark)
# second_highest_score=0
# for item in second_highest:
#     if item>second_highest_score:
#         second_highest_score=item
# print(f"The second highest score is {second_highest_score}")