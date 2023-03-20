a=[]
total_itme= int(input("Enter The Total Numbers of items: "))
i=0
while( i < total_itme):
    n=int(input("Enter: "))
    a.append(n)
    i=i+1
a.sort()
print("\nYour Array is :", end=" ")
print(a)

for j in a:
    if(a.count(j) == 1):
        continue
    else:
        x=a.index(j)
        del a[x]

print("\nAfter Deliting All Copy Items in the array :", end=" ")
print(a)