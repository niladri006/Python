n=''
total=0
print(" TO EXIT PRESS - 0\n\n")
while(n!=0):
    n=float(input("ENTER ITEM AMOUNT = "))
    total=total+n
if(total>=1500):
    s=total*(90/100)
    t=total*(10/100)
    print("\nTOTAL PRICE - $",total)
    print("DISSCOUNT CASH - $",t)
    print("AFTER 10% DISSCOUNT - $",s)
else:
    print("\n\tTOTAL PRICE - $",total)
