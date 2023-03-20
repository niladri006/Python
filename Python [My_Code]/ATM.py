cash=100000
ch=''
while(ch!=4):
    print("\tMAIN MANU :-")
    print("\t\t 1. ATM Cash")
    print("\t\t 2. Cash Withdraw")
    print("\t\t 3. Cash Deposite")
    print("\t\t 4. Exit")
    ch=int(input("Your choise: "))
    if(ch==1):
        print("\t\t ATM Cash")
        password=int(input("\tEnter Password: "))
        if(password==123456):
            print("\tTotal Cash = $",cash)
            f=int(input("\tWant to entry cash in ATM ? \t(1.Yes  2.No) \n\tYour Choise- "))
            if(f==1):
                x=int(input("Enter Cash:- $ "))
                cash=cash+x
                print("After Adding Total Cash - $",cash,"\n")
            else:
                print()
        else:
            print("Wrong Passdord !\n")
    elif(ch==2):
        print("\t\t Cash Withdraw")
        if(cash>10000):
            name=input("\tEnter Your First Name: ")
            password1=int(input("\tEnter Password: "))
            if(password1==len(name)):
                print("\n\tPassword Correct !")
                c_w=float(input("\tEnter Amount To Withdraw($500-10000): "))
                cash=cash-c_w
                print("Amount Withdraw !\n")
            else:
                print("\tWrong Password !")
        else:
            print("\tSorry! ATM Has Not Enough Cash...\n")
    elif(ch==3):
        print("\t\t Cash Deposite")
        name=input("\tEnter Your Name: ")
        password2=int(input("\tEnter Password: "))
        if(password2==len(name)):
            print("\tPassword Correct !")
            c_d=float(input("\tEnter Amount To Deposit($500-10000): "))
            cash=cash+c_d
            print("\tCash Deposited !")
            print("\n")
    elif(ch==4):
        print("\t\t Exit")
        break
    else:
        print("\tWrong Enter !")
        continue
