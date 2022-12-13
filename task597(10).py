Input = input()
words = Input.split()
r1 = int(words[0])
r2 = int(words[1])
r3 = int(words[2])
D1 = 2*r1
D2 = 2*r2
D3 = 2*r3
if D1>=(D2+D3):
    print("YES")
else:
    print("NO")