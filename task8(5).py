Insert = input()
numbers = Insert.split(' ')
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
if a * b == c:
    print('YES')
else:
    print('NO')
