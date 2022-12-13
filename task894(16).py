import math

inp = input()
nums = inp.split()
S = float(nums[0])
R = float(nums[1])

r = ((math.pi * (R ** 2) - S) / math.pi) ** (1 / 2)
print(round(r, 6))
