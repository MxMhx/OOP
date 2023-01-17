text_input = input()

def count_minus(str):
    str = str.split()
    neg_list = [number for number in str if int(number) < 0]
    return len(neg_list)

print(count_minus(text_input))