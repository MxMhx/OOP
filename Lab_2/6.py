def add2list(lst1,lst2):
    new_list = [lst1[i] + lst2[i] for i in range(len(lst1))]
    return new_list

x = [1,2,3]
y = [4,5,6]

print(add2list(x,y))