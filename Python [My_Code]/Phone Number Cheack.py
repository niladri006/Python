i=""
while(i!=0):
    num=input("Enter Phone Number: ")
    x=num
    if(len(x)==10 and x.isdigit()==True and x.isspace()!=True):
        print("\tRESULT STATUS:- VARIFIED\n")
    else:
        print("\tINVALID PHONE NUMBER !!\n")
