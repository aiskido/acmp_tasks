Input = input()
numbers = Input.split()
a = int(numbers[0])
b = int(numbers[1])
h = int(numbers[2])
S = 2*(a*h+b*h)
if(S/16>int(S/16)):
	Amount = int(int(S/16)+1)
else:
	Amount = int(S/16)
print(Amount)