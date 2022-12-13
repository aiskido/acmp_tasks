Input = input()
words = Input.split()
W = int(words[0])
H = int(words[1])
R = int(words[2])
D = 2*R
if D<=H and D<=W:
    print("YES")
else:
    print("NO")