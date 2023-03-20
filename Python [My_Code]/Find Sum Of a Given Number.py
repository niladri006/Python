i=int(input("Enter Number to find sum of Digits: "))
sum=0
while(i>0):
    sum=sum+(i%10)
    i=i//10
print("Sum Of Digits =",sum)
