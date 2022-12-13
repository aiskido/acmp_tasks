inp = input()
nums = inp.split()
N = int(nums[0])
a = int(nums[1])
b = int(nums[2])
Mid = int(N/2-1)
x = int(abs(a-b)-1)
res = x
if x > Mid:
    res = N-x-2
print(res)