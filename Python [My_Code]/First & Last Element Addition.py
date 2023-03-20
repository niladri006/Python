a=[]
count=0
n=int(input("ENTER A NUMBER: "))
x=n
while(n>0):
    count=count+1
    n=n//10
for i in range(count):
    y=x%10
    a.append(y)
    x=x//10
a.reverse()
c=a[0]+a[len(a)-1]
print(a[0],"+",a[len(a)-1],"=",c)

