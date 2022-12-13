def Binary(num):
	binary = 0
	onecount = 0
	zerocount = 0
	temp = 1
	while num!=0:
		if num%2 == 0:
			zerocount += 1
		else:
			onecount += 1
		binary += int(temp*(num%2))
		temp *= 10
		num = int(num/2)
	return onecount

num = int(input())
print(Binary(num))