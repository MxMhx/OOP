def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score

def calc_average_score(subject_score):
    sum = 0
    for score in subject_score.values():
        sum += score
    sum = sum / len(subject_score)
    return round(sum,2)

print(calc_average_score(add_score({'python' : 50,'korn' : 45},'calculus',40)))