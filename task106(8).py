x = int(input())
i = 0
CoR = 0
CoG = 0
while i<x:
    b = int(input())
    if b==0:
        CoG = CoG+1
    else:
        CoR = CoR+1
    i=i+1
if CoG<CoR:
    print(CoG)
else:
    print(CoR)