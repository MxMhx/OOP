def char_count(str):
    char_count_dict = {}
    for x in str:
        if str.count(x) > 0:
            char_count_dict[x] = str.count(x)
    print(char_count_dict)
char_count('language')