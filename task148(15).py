Input = input()
numbers = Input.split()
x = int(numbers[0])
y = int(numbers[1])
while y!=0:
	c = y
	y = x%y
	x = c
print(x)