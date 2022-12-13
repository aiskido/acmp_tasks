Input1 = input()
n = int(Input1)
Input2 = input()
numbers = Input2.split()
Res = False
for i in range(0,n,1):
	if int(numbers[i])<=437:
		print("Crash", (i+1))
		Res = True
		break
if Res is False:
	print("No crash")