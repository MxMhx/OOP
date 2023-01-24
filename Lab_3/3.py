def is_plusone_dictionary(d):
    num_list = []
    for num in d.keys():
        num_list.append(num)
        num_list.append(d[num])
    for index in range(len(num_list)):
        if index == len(num_list) - 1:
            return True
        if num_list[index+1] - num_list[index] != 1:
            return False
            break

d = {1:2,3:4,5:6,8:9}
#print(is_plusone_dictionary(d))
print(is_plusone_dictionary(d))