n = int(input())
Arr = list()
for i in range(n):
	Input = input()
	numbers = Input.split()
	Arr.append(int(numbers[0]))
	Arr.append(int(numbers[1]))
for i in range(0,n*2,2):
	n = Arr[i]
	m = Arr[i+1]
	d = int(19*m+((n+239)*(n+366))/2)
	print(d)
