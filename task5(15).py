n = int(input())
List = list()
inp = input()
nums = inp.split()
for i in range(n):
	List.append(int(nums[i]))
Elist = list()
Estr = ''
Olist = list()
Ostr = ''
for i in List:
	if i%2==0:
		Elist.append(i)
		Estr += str(i) + ' '
	else:
		Olist.append(i)
		Ostr += str(i) + ' '
print(Ostr)
print(Estr)
if len(Elist)>=len(Olist):
	print('YES')
else:
	print('NO')