Input = input()
n = int(Input)
Sum = 0
for i in range(1, n+1, 1):
	Sum = Sum+i
Sum = int(Sum)
for i in range(1, n+1, 1):
	if(n%i!=0):
		Sum = Sum-i
print(Sum)
