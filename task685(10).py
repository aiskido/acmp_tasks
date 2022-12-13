Input = input()
numbers = Input.split()
ListA = [int(numbers[0]), int(numbers[1]), int(numbers[2])]
ListB = [int(numbers[3]), int(numbers[4]), int(numbers[5])]
for i in range(3):
    for j in range(3):
        if ListA[i]<ListA[j]:
            Temp = ListA[i]
            ListA[i] = ListA[j]
            ListA[j] = Temp
for i in range(3):
    for j in range(3):
        if ListB[i]<ListB[j]:
            Temp = ListB[i]
            ListB[i] = ListB[j]
            ListB[j] = Temp
result = ListA[2]*ListB[2]+ListA[1]*ListB[1]+ListA[0]*ListB[0]
print(result)