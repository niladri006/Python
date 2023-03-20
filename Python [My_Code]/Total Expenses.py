n=""
ans=1
total=0
i=int(input("HOW MANY ITEMS: "))
j=1
while(j<=i):
    print(j,end=") ")
    n=float(input("ENTER ITEM PRICE: "))
    total=total+n
    j=j+1
if(total>1000):
    ans=total*(90/100)
    print("TOTAL  -",ans)
    print("YOUR ITEM IS MORE THAN 1000. \nTHEN YOU 10% AND YOUR ITEM PRICE IS",ans)
else:
    print("YOUR ITEM PRICE IS",ans)
