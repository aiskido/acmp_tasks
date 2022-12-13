inp = input()
nums = inp.split()
x = int(nums[0])
y = int(nums[1])
xmin = int((x+1)/2)
ymin = int((y+1)/2)
prnt = ''
if xmin<ymin:
	prnt += str(ymin)
else:
	prnt += str(xmin)
prnt += ' '
if x>y:
	prnt += str(y)
else:
	prnt += str(x)
print(prnt)