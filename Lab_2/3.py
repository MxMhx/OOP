def delete_minus(x):
    new_list = []
    new_list = [[number for number in member if number > 0]for member in x]
    return new_list

print(delete_minus([ [1, -3, 2], [-8, 5], [-1, -4, -3] ]))