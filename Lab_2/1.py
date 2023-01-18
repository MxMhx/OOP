number_input = input()
number_input = sorted(list(map(int,number_input.split())))

if number_input[0] == 0:
    for index in range(len(number_input)):
        if number_input[index] != 0:
            number_input[0] = number_input[index]
            number_input[index] = 0
            break
print(''.join(map(str,number_input)))