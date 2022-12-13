Input = input()
Changes = Input
Pos = 1
for i in Changes:
	if i=='A' and Pos==1:
		Pos = 2
	elif i=='A' and Pos==2:
		Pos = 1
	elif i=='B' and Pos==2:
		Pos = 3
	elif i=='B' and Pos==3:
		Pos = 2
	elif i=='C' and Pos==1:
		Pos = 3
	elif i=='C' and Pos==3:
		Pos = 1
print(Pos)