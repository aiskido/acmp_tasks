Input = input()
numbers = Input.split()
a1 = int(numbers[0])
a2 = int(numbers[1])
n = int(numbers[2])
d = int(a2-a1)
an = int(a1+(n-1)*d)
print(an)