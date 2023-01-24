def is_plusone_dictionary(d):
    sum = 0
    for number in d.keys():
        if d[number] - number != 1:
            return False
            break
    return True

d = {1:2, 3:10, 5:6, 7:8}
print(is_plusone_dictionary(d))