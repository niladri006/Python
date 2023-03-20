y=int(input("ENTER HOW MANY STUDENTS: "))
d=1
while(d<=y):
    print("\n",d,end=". ")
    n=input("ENTER A NAME: ")
    print(">>> Short Name -  ",end="")
    for i in range(0,3):
        if(n[i].isspace()==True):
            break
        else:
            print(n[i],end="")
    d=d+1
