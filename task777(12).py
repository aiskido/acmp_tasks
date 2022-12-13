Input = input()
numbers = Input.split()
S = int(numbers[0])
T = int(numbers[1])
if T<S:
	Diff = S-T
	print(int(12-Diff))
else:
	print(int(T-S))