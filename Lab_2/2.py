def count_char_in_string(x,c):
    d = []
    count = 0
    [d.append(i.count(c)) for i in x]
    return d

print(count_char_in_string(['abba', 'babana', 'ann'],'a'))