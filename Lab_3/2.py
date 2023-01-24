def add_score(subject_score, student, subject, score):
	if student not in subject_score.keys():
		subject_score.update({student:{subject : score}})
	else:
		subject_score[student].update({subject : score})
	return subject_score

def calc_average_score(subject_score):
    sum = 0
    for student in subject_score.keys():
        for score in subject_score[student].values():
            sum += score
        sum = sum / len(subject_score[student])
        subject_score[student] = str(round(sum,2))
    return subject_score

dictt = {'65010001' : {'python' : 50} }

dictt = add_score(dictt,'65010001','calculus',60)
print(dictt)
#calc_average_score(add_score({'65010001' : {'python' : 50} },'65010001','calculus',60))
#print(calc_average_score(add_score({'65010001' : {'python' : 50} },'65010001','calculus',60)))