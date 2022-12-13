Insert = input()
#numbers = Insert.split(' ')
x = int(Insert)
if x == 1:
    print('0')
elif x % 2 == 0:
    print(int(x/2))
else:
    print(int(x))
