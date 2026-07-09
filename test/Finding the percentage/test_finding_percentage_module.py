from src.finding_the_percentage.util import finding_percentage

def test_finding_percentage_whole_number():
    student_marks = {'Alice': [20, 30, 40]}
    assert finding_percentage(student_marks, 'Alice') == 30.0

def test_finding_percentage_decimal_average():
    student_marks = {'Bob': [25, 26]}
    assert finding_percentage(student_marks, 'Bob') == 25.5

def test_finding_percentage_single_score():
    student_marks = {'Charlie': [85]}
    assert finding_percentage(student_marks, 'Charlie') == 85.0

def test_finding_percentage_multiple_students():
    student_marks = {
        'David': [10, 20], 
        'Eve': [90, 100]
    }
    assert finding_percentage(student_marks, 'Eve') == 95.0