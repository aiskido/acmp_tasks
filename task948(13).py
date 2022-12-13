Input = input()
numbers = Input.split()
x = int(numbers[0])
y = int(numbers[1])
c = int(y/x)
d = int(y-(x*c))
if y%x==0:
	print(c, x)
else:
    print((c+1), (d))