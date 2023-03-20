def add():
    print("\n")
    a=float(input("ENTER BIG NUMBER: "))
    b=float(input("ENTER ANOTHER NUMBER: "))
    c=a+b
    print("\nYOUR ANSWER: \n",a,"+",b,"=",c)
    print("\n\n")

def difference():
    print("\n\n")
    a=float(input("ENTER BIG NUMBER: "))
    b=float(input("ENTER ANOTHER NUMBER: "))
    c=a-b
    print("\nYOUR ANSWER: \n",a,"-",b,"=",c)
    print("\n\n")
choise=0
while(choise!=3):
    choise=int(input("MAIN MENU - \n\t1) SUM. \n\t2) DIFFERENCE. \n\t3) EXIT \n\nYOUR INPUT[1/2/3]: "))

    if(choise==1):
        add()
        continue
    elif(choise==2):
        difference()
        continue
    elif(choise==3):
        print("YOU ARE EXIT NOW !!!")
        break
    else:
        print("YOU ENTERED WRONG INPUT  !!!")
        continue
    
