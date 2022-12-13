Input = input()
numbers = Input.split()
x = int(numbers[0])
y = int(numbers[1])
z = int(numbers[2])
if ((x+y)<=z) or ((x+z)<=y) or ((y+z)<=x):
	print('NO')
else:
	print('YES')