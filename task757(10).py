# It's wrong, I could not find why. But I think about
# long long number
Input = input()
numbers = Input.split()
List = [int(numbers[0]), int(numbers[1]), int(numbers[2])]
Spirt = [int(List[0]/2), int(List[1]/6), int(List[2]/1)]
Min = None
for i in range(0,3,1):
    if Min is None or Min > Spirt[i]:
        Min = Spirt[i]
print(Min)