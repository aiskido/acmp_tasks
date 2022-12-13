Input1 = input()
Time = Input1.split(':')
Input2 = input()
numbers = Input2.split()
Hr = int(numbers[0])
Min = int(numbers[1])
HR = 0
MIN = None
if (int(Time[1])+Min)>=60:
	HR = 1
	MIN = (int(Time[1])+Min)%60
else:
	MIN = (int(Time[1])+Min)

if int(HR + int(Time[0])+Hr)>=24:
	HR = int(HR + int(Time[0])+Hr)%24
else:
	HR = int(HR + int(Time[0])+Hr)
if HR<10 and MIN>9:
	print('0'+str(HR)+':'+str(MIN))
elif HR>9 and MIN<10:
	print(str(HR)+':'+'0'+str(MIN))
elif HR<10 and MIN<10:
    print('0'+str(HR)+':'+'0'+str(MIN))
else:	
    print(str(HR)+':'+str(MIN))