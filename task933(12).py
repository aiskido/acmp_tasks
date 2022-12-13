Input = input()
numbers = Input.split()
A = int(numbers[0])
B = int(numbers[1])
C = int(numbers[2])
T = int(numbers[3])
if T>A:
	Diff = int(T-A)
	Res = A*B+C*Diff
	print(Res)
else:
	Res = T*B
	print(Res)