a=[ ]
def creat_list():
    n=int(input("Enter the sige of List ? \n->  "))
    for i in range(1,n+1):
        print(i,end=") ")
        a.append(int(input("Enter number? ->  ")))
    print("List Created !!")
    return a

def display():
    print("List is =",a)

def delet():
    k=int(input("How many Element Will Delete ? \n-> "))
    for z in range(0,k):
        x=int(input("Enter number to Delete? -> "))
        b=a.index(x)
        del a[b]
    print("Deletion Completed !")

def update():
    c=int(input("Enter Value to Update? \n-> "))
    d=a.index(c)
    a[d]=input("Enter New Input? -> ")
    print("List Updated !")

def length():
    print("Lenth of list =",len(a))

def add():
    t=int(input("How eany Value? \n-> "))
    for h in range(1,t+1):
        j=int(input("Enter Value? -> "))
        a.insert(len(a),j)
    print("List is =",a)
    
def min_max():
    print("Min number is =",min(a))
    print("Max number is =",max(a))

def sort():
    a.sort()
    print("List is sorted by Ascending order !")

def reverse():
    a.reverse() 
    print("List Reversed !")
    
def even_odd():
    even=0
    odd=0
    for cv in range(len(a)):
        if(a[cv]%2==0):
            even=even+1
        else:
            odd=odd+1
    print("Total Even Numbers =",even)
    print("Total Odd Numbers =",odd)    
    
ch=""
while(ch!=11):
    print("\n\n\tMAIN MENU -> ")
    print("1.  CREAT A NEW LIST.           \t2.  SHOW THE LIST.\n")
    print("3.  DELET ANY VALUE FROM LIST.  \t4.  ADDING VALUE IN THE LIST.\n")
    print("5.  UPDATE ANY VALUE FROM LIST. \t6.  CHECK LENGTH OF LIST.\n")
    print("7.  REVERSE THE LIST.           \t8.  REARRANGE BY ASCENDING ORDER.\n")
    print("9.  MAX & MIN NUMBER IN LIST.   \t10. COUNT ODD & EVEN NUMBER IN LIST.\n")
    print("11. EXIT.")
    ch=int(input("\nYOUR INPUT [1-10]:->   "))
    if(ch==1):
        print("\t\t CREAT A NEW LIST.")
        creat_list()
    elif(ch==2):
        print("\t\t SHOW THE LIST.")
        display()
    elif(ch==3):
        print("\t\t DELET ANY ELEMENT FROM LIST.")
        display()
        delet()
    elif(ch==4):
        print("\t\t ADDING VALUE/ELEMENT")
        add()
    elif(ch==5):
       print("\t\t UPDATE ANY ELEMENT FROM LIST.")
       display()
       update()
    elif(ch==6):
        print("\t\t CHECK LENGTH OF LIST.")
        length()
    elif(ch==7):
        print("\t\t REVERSE LIST.")
        reverse()
    elif(ch==8):
        print("\t\t  REARRANGE LIST BY ASCENDING ORDER.")
        sort()
    elif(ch==9):
        print("\t\t CHECK MAX & MIN.")
        min_max()
    elif(ch==10):
        print("\t\t COUNT HOW MANY ODD & EVEN NUMBER.")
        even_odd()
    elif(ch==11):
        break
    else:
        continue
