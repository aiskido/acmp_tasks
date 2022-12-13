Input = input()
words = Input.split()
a1 = int(words[0])
a2 = int(words[1])
a3 = int(words[2])
if a1==(a2+a3):
    print("YES")
elif a2==(a1+a3):
    print("YES")
elif a3==(a2+a1):
    print("YES")
else:
    print("NO")