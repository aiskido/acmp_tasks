Input = input()
Words = Input.split()
k = int(Words[0])
Word = Words[1]
print(Word[0:k-1:1] + Word[k:len(Word):1])