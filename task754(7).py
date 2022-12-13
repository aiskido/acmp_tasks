Insert = input()
numbers = Insert.split(' ')
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
if a < 94 or b < 94 or c < 94:
    print('Error')
elif a > 727 or b > 727 or c > 727:
    print('Error')
else:
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)