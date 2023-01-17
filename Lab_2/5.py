text_input = input()

def only_English(string1):
    english_char = [str for str in string1 if 'a' <= str <= 'z' or 'A' <= str <= 'Z']
    return ''.join(english_char)

print(only_English(text_input))