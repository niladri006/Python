a=[]
def creat_list():
    n=int(input("How many elements? "))
    for i in range(1,n+1):
        print(i,end=") ")
        a.append(input("Enter Value/Element: "))
    print("List Created !!")
    return a

def display():
    print("List is =",a)

def delet():
    k=int(input("How many Value/Element Will Delete: "))
    for z in range(0,k):
        x=input("Enter Value/Element to Delete: ")
        b=a.index(x)
        del a[b]
    print("Deletion Completed !")

def update():
    c=input("Enter Value/Element to Update: ")
    d=a.index(c)
    a[d]=input("Enter New Input: ")
    print("List Updated !")

def length():
    print("Lenth of list =",len(a))

def add():
    t=int(input("How eany Value/Element :"))
    for h in range(1,t+1):
        j=input("Enter Value/Element: ")
        a.insert(len(a),j)
    print("List is =",a)
    
def reverse():
    a.reverse() 
    print("List Reversed !")
        
    
ch=""
while(ch!=8):
    print("\n\nMAIN MENU")
    print("\t1. CREAT A NEW LIST.")
    print("\t2. SHOW THE LIST.")
    print("\t3. DELET ANY VALUE/ELEMENT FROM LIST.")
    print("\t4. ADDING VALUE/ELEMENT")
    print("\t5. UPDATE ANY VALUE/ELEMENT FROM LIST.")
    print("\t6. CHECK LENGTH OF LIST.")
    print("\t7. REVERSE LIST.")
    print("\t8. EXIT.")
    ch=int(input("\nYOUR INPUT: "))
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
        break
    else:
        continue
