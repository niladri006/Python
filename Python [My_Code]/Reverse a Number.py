i=int(input("Enter A Number To Reverse: "))
x=i
rev=0
while(i>0):
    rev=(rev*10)+(i%10)
    i=i//10
print("\nYour Number Is",x)
print("Reverse Number is", rev)
