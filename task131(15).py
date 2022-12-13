Input = input()
n = int(Input)
List = []
for i in range(0,n,1):
	In = input()
	numbers = In.split()
	List.append(int(numbers[0]))
	List.append(int(numbers[1]))
ListM = []
Max = None
index = -1
for i in range(0,2*n,2):
	if List[i+1]==1:
		if Max==None or Max<List[i]:
			Max = List[i]
			index = int(i/2+1)
print(index)