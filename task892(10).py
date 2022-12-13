Input = input()
x = int(Input)
if x>2 and x<6:
    print("Spring")
elif x>5 and x<9:
    print("Summer")
elif x>8 and x<12:
    print("Autumn")
elif x==12 or x==1 or x==2:
    print("Winter")
else:
    print("Error")