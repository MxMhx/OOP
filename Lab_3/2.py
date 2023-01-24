def add_score(subject_score, student, subject, score):
    student_dict = subject_score[student]
    student_dict[subject] = score
    subject_score[student] = student_dict
    print(subject_score)

add_score({'65010001' : {'python' : 50} },'65010001','calculus',60)
