print("AI: ENTER A NUMBER ?")
n=int(input("YOU: "))
x=0
y=1
z=0
loop=0
print("\nAI: YOUR RESULT IS - ")
while(loop!=n):
    print(z,end="  ")
    x=y
    y=z
    z=x+y
    loop=loop+1
