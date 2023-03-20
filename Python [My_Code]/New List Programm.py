a=[]
ch=''
print("To Exit press 0(zero)")
while(ch!="0"):  
    ch=input("Enter element? =  ")
    a.append(ch)
del a[len(a)-1]
print(a)
