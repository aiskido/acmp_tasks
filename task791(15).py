num = int(input())
if num%8==1:
	if num==1:
		print(num+1, num+8)
	elif num==57:
		print(num-8, num+1)
	else:
		print(num-8, num+1, num+8)
elif num%8==0:
	if num==8:
		print(num-1, num+8)
	elif num==64:
		print(num-8, num-1)
	else:
		print(num-8, num-1, num+8)
elif num>1 and num<8:
	print(num-1, num+1, num+8)
elif num>57 and num<64:
	print(num-8, num-1, num+1)
else:
	print(num-8, num-1, num+1, num+8)
