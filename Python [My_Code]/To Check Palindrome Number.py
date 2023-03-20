i=int(input("Enter Number To Check Palindrome: "))
rev=0
x=i
while(i>0):
    rev=(rev*10)+(i%10)
    i=i//10
if(x==rev):
    print("\nThis Is Palindrome Number...")
else:
    print("\nThis Is Not Palindrome Number...")
