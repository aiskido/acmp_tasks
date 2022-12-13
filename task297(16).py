inp = input()
count = 0
for i in inp:
    if i == '6' or i == '9' or i == '0':
        count += 1
    elif i == '8':
        count += 2
print(count)