import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    
    def createAccount(self):
        self.accNo= int(input("ENTER THE ACCOUNT NUMBER : "))
        self.name = input("ENTER THE ACCOUNT HOLDER NAME : ")
        self.type = input("ENTE THE TYPE OF ACCOUNT [C/S] : ")
        self.deposit = int(input("ENTER THE INITIAL AMOUNT(>=500) FOR SAVING AND (>=1000) FOR CURRENT : "))
        print("\n\n\nACCOUNT CREATED!")
    
    def showAccount(self):
        print("ACCOUNT NUMBER -",self.accNo)
        print("ACCOUNT HOLDER NAME -", self.name)
        print("TYPE OF ACCOUNT -",self.type)
        print("BALANCE -",self.deposit)
    
    def modifyAccount(self):
        print("ACCOUNT NUMBER : ",self.accNo)
        self.name = input("MODIFY ACCOUNT HOLDER NAME : ")
        self.type = input("MODIFY TYPE OF ACCOUNT : ")
        self.deposit = int(input("MODIFY BALANCE : "))
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    

def intro():
    print("\t\t\t\t**************************")
    print("\t\t\t\t  STATE BANK OF INDIA")
    print("\t\t\t\t**************************")
    print("\n\n")
    print("Press Enter key to continue ...")
    input()



def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else :
        print("NO RECORDS TO DISPLAY!")
        

def displaySp(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("YOUR ACCOUNT BALANCE IS = ",item.deposit)
                found = True
    else :
        print("NO RECORDS TO SEARCH!")
    if not found :
        print("NO EXISTING RECORD WITH THIS NUMBER!")

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("ENTER THE AMOUNT TO DEPOSIT : "))
                    item.deposit += amount
                    print("Your account is updted")
                elif num2 == 2 :
                    amount = int(input("ENTER THE AMOUNT TO WITHDRAW : "))
                    if amount <= item.deposit :
                        item.deposit -= amount
                    else :
                        print("YOU CANNOT WITHDRAW LARGER AMOUNT!")
                
    else :
        print("NO RECORDS TO SEARCH!")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("ENTER THE ACCOUNT HOLDER NAME : ")
                item.type = input("ENTER THE ACCOUNT TYPE : ")
                item.deposit = int(input("ENTER THE AMOUNT : "))
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
        
# start of the program
ch=''
num=0


while ch != 8:
    print("\n\nMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print("\n")
    ch = input("SELECT YOUR OPTION(1-8): ")
    
    if ch == '1':
        print("\n\t NEW ACCOUNT")
        writeAccount()
    elif ch =='2':
        print("\n\t DEPOSIT AMOUNT")
        num = int(input("ENTER THE ACCOUNT NUMBER : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        print("\n\t WITHDRAW AMOUNT")
        num = int(input("ENTER THE ACCOUNT NUMBER : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        print("\n\t BALANCE ENQUIRY")
        num = int(input("ENTER THE ACCOUNT NUMBER : "))
        displaySp(num)
    elif ch == '5':
        print("\n\t ALL ACCOUNT HOLDER LIST")
        displayAll();
    elif ch == '6':
        print("\n\t CLOSE AN ACCOUNT")
        num =int(input("ENTER THE ACCOUNT NUMBER : "))
        deleteAccount(num)
    elif ch == '7':
        print("\n\t MODIFY AN ACCOUNT")
        num = int(input("ENTER THE ACCOUNT NUMBER : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tTHANKS FOR USING STATE BANK OF INDIA !!")
        break
    else :
        print("INVALID CHOICE!")
        
