def second_largest(list):
    list.sort()
    return list[-2]

li=[]
n=int(input("Enter size of list: "))
for i in range(1,n+1):
    print(i,end=") ")
    e=int(input("Enter element of list: "))
    li.append(e)

print("second largest in ",li,"is",second_largest(li))
          
