Insert = input()
words = Insert.split()
numbers = [int(words[0]), int(words[1]), int(words[2])]
numbers.sort()
print(numbers[2]-numbers[0])