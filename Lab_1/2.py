text = input()
count_upper = 0
count_lower = 0
for i in text:
    if i.isupper():
        count_upper += 1
    elif i.islower():
        count_lower += 1
print(count_lower)
print(count_upper)