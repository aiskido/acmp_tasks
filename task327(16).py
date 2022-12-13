def Check(number):
	first = int(number/1000)
	second = int(number%1000)
	fsum = int(first/100) + int((first/10)%10) + int(first%10)
	ssum = int(second/100) + int((second/10)%10) + int(second%10)
	if fsum==ssum:
		return True

n = int(input())
List = list()
for i in range(n):
	Str = input()
	List.append(Str)
binList = list()
for st in List:
	org = int(st)
	pls = org+1
	mns = org-1
	if Check(pls) or Check(mns):
		binList.append('Yes')
	else:
		binList.append('No')
for i in binList:
	print(i)
