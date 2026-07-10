from collections import namedtuple

def calculate_average(headers, data):
    Student = namedtuple('Student', headers)
    total_marks = 0.0
    
    for row in data:
        student_record = Student(*row)
        total_marks = total_marks + float(student_record.MARKS)
        
    number_of_students = len(data)
    average = total_marks / number_of_students
    
    return f"{average:.2f}"