com_name=input("Enter Your Company Name: ")
employ=int(input("Enter how many employs in your Office: "))
male=0
female=0
other=0
total_cash=0
for i in range(1,employ+1):
    emp_name=input("\t\nEnter employ's ful name: ")
    sex=int(input("\t1. Male. \n\t2. Female. \n\t3. Other. "))
    if(sex==1):
        male=male+1
    elif(sex==2):
        female=female+1
    else:
        other=other+1
    salary=float(input("\tEnter his salary:₹ "))
    total_cash=total_cash+salary
print("\n\n")
print("\t\t\tALL AT A GLANCE\n")
print("COMPAY NAME:",com_name)
print("TOTAL MONEY OF ALL EMPLOY IS:₹",total_cash)
print("Total Male =",male,"\nTotal Female =",female,"\nOthers =",other)
