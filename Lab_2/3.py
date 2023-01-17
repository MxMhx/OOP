def delete_minus(x):
    new_list = []
    for member in x:
        temp_list = [number for number in member if number > 0]
        new_list.append(temp_list)
    return new_list

print(delete_minus([ [1, -3, 2], [-8, 5], [-1, -4, -3] ]))