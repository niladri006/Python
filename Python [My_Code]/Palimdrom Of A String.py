i=""
while(i!=0):
    name=input("Enter A Word (Enter all in Lower/Upper Case): ")
    y=name.capitalize()
    b=name[-1: :-1]
    if(b==name):
        print("\t>>>",y,"Is Palindrom\n")
    else:
        print("\t>>>",y,"Is Not Palindrom\n")
