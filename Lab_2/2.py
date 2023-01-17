def count_char_in_string(x,s):
    d = []
    [d.append(i.count(s)) for i in x]
    return d

print(count_char_in_string(['abba', 'babana', 'ann'],'a'))