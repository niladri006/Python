even=0
odd=0
a=[]
y=int(input("How many elements: "))
for i in range(y):
    s=int(input("Enter element: "))
    a.append(s)
print("\n\nList is =",a)
print("Min number is =",min(a))
print("Max number is =",max(a))
a.sort()
print("List after Sorting =",a)
for j in range(len(a)):
    if(a[j]%2==0):
        even=even+1
    else:
        odd=odd+1
print("Total Even Numbers =",even)
print("Total Odd Numbers =",odd)
