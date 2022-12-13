Input1 = input()
n = int(Input1)
Input2 = input()
numbers = Input2.split()
Sum = 0
for i in range(0,n,1):
	Sum = Sum + int(numbers[i])
Res = int(Sum-(n-1))
print(Res)