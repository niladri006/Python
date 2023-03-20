n=input("ENTER A NUMBER: ")
count=0
for i in range(len(n)):
    if(i==n[0] or i==(len(n)-1)):
        count=count+n[i]
    else:
        continue

print(count)
