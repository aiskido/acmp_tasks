sum1 = 0
sum2 = 0
i = 1
while i < 5:
    Insert = input()
    numbers = Insert.split(' ')
    sum1 = sum1 + int(numbers[0])
    sum2 = sum2 + int(numbers[1])
    i = i+1
if sum1 > sum2:
    print('1')
elif sum1 < sum2:
    print('2')
else:
    print('DRAW')
