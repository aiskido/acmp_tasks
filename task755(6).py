Insert = input()
numbers = Insert.split(' ')
Sum = int(numbers[0]) + int(numbers[1])
if int(numbers[2]) > Sum:
    print('Impossible')
else:
    print(Sum - int(numbers[2]))
