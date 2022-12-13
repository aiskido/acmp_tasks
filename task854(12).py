Input = input()
numbers = Input.split()
Troom = int(numbers[0])
Tcond = int(numbers[1])
Mode = input()
if Mode == "heat":
	if Troom>=Tcond:
		print(Troom)
	else:
		print(Tcond)
elif Mode == "freeze":
	if Troom<=Tcond:
		print(Troom)
	else:
		print(Tcond)
elif Mode == "auto":
	print(Tcond)
else:
    print(Troom)