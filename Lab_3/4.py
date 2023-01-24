def char_count(str):
    char_count_dict = {x: str.count(x) for x in str if str.count(x) > 0}
    return char_count_dict

print(char_count('language'))