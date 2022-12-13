Input = input()
Res = True
for i in Input:
	if i=='0':
		Res = False
		break
if Res is True:
	print("YES")
else:
	print("NO")