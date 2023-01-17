def checkpalindrome(num):
    if len(str(num))%2 == 0:
        if num == int(str(num)[::-1]):
            return True

def checkmost(number_list):
    current_most_number = number_list[0]
    for i in number_list:
        if current_most_number < i:
            current_most_number = i
    return current_most_number
        

palindrome_list = []
for i in range(999,99,-1):
    for j in range(999,99,-1):
        num = i*j
        if checkpalindrome(num):
            palindrome_list.append(num)

print(checkmost(palindrome_list))