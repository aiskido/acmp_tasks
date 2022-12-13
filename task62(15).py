Input = input()
L = Input[0]
N = int(Input[1])
LiN = None
if L=='A' or L=='C' or L=='E' or L=='G':
	LiN = 1
else:
	LiN = 2
if (N+LiN)%2==0:
	print("BLACK")
else:
	print("WHITE")