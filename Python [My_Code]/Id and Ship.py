n=""
while(n!=0):
    n=input("\nENTER CLASS ID: ")
    if(n=="B" or n=="b"):
        print("\tBattleShip")
    elif(n=="C" or n=="c"):
        print("\tCruise")
    elif(n=="D" or n=="d"):
        print("\tDestroyer")
    elif(n=="F" or n=="f"):
        print("\tFrigate")
    elif(n==0):
        break
    else:
        print("\nYOU ENTERED WRONG ID!!!")
        continue
        
