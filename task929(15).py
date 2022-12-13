Input = input()
number = int(Input)
Div = int(number/6)
Min = Div + (7-number%6)%7
Max = number*6
print(Min, Max)