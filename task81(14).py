Input1 = input()
n = int(Input1)
Input2 = input()
numbers = Input2.split()
Min = None
Max = None
for i in range(0,n,1):
	if Min is None or Min > int(numbers[i]):
		Min = int(numbers[i])
	if Max is None or Max < int(numbers[i]):
		Max = int(numbers[i])
print(Min, Max)