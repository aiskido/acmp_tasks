Input = input()
numbers = Input.split()
ListA = [int(numbers[0]), int(numbers[1]), int(numbers[2])]
S = 2*(ListA[0]*ListA[1]+ListA[0]*ListA[2]+ListA[1]*ListA[2])
V = ListA[0]*ListA[1]*ListA[2]
print(S,V)