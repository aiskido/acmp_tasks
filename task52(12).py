Input = input()
number1 = Input[0:3:1]
number2 = Input[3:6:1]
x1 = int(number1[0])+int(number1[1])+int(number1[2])
x2 = int(number2[0])+int(number2[1])+int(number2[2])
if x1==x2:
	print('YES')
else:
	print('NO')