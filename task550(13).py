Input = input()
Number = int(Input)
if (Number%400==0) or (Number%4==0 and Number%100!=0):
	if Number>999:
		print('12/09/' + Input)
	elif 99<Number and Number<1000:
	    print('12/09/0' + Input)
	elif 9<Number and Number<100:
		print('12/09/00' + Input)
	else:
		print('12/09/000' + Input)
else:
	if Number>999:
		print('13/09/' + Input)
	elif 99<Number and Number<1000:
	    print('13/09/0' + Input)
	elif 9<Number and Number<100:
		print('13/09/00' + Input)
	else:
		print('13/09/000' + Input)