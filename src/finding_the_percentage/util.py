def finding_percentage(student_marks,student_name):
    sum=0
    for item,value in student_marks.items():
        if item==student_name:
            for marks in value:
                sum=sum+marks
            avg_marks=sum/len(value)
            return avg_marks

# if __name__=="__main__":
#     student_marks={
#     'abhi':[44,24,24],
#     'abks':[25,52,13]
#     }  
#     student_name='abhi'
#     finding_percentage(student_marks,student_name)


