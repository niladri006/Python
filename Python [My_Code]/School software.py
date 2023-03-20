import os
print("\n\n\n")
print("\t\t\t*********************************************")
print("\t\t\t||                 WELLCOME                ||")
print("\t\t\t||    KHARAR SRI AUROBINDO VIDHAYMANDIR    ||")
print("\t\t\t*********************************************")
print("\t\t\t       ======  STD-1972  ===== ")

# NAME ENTERY FUNCTION
def name_entry():
    totalstudent=0
    male=0
    female=0
    print("\n")
    print("\t\t\t**********************************")
    print("\t\t\t||     NAME ENTRY OF STUDENTS   ||")
    print("\t\t\t**********************************\n")
    loop6=0
    while loop6 != 2:
       choise3=int(input("SELECT BELLOW ONE OF THEM:- \n\t 1. GIVE NAME ENTRY TO THE CLASS STUDENTS's. \n\t 2. EXIT.  \n\nYOUR INPUT(1/2): "))
       if(choise3 == 1):
           print("\t\t   GIVE NAME ENTRY TO THE CLASS STUDENTS's")
           print("\t\t*********************************************\n")
           classroom=int(input("ENTER CLASS NUMBER(1-12): "))
           student=int(input("HOW MANY STUDENTS IN THIS CLASS: "))
           j=1
           while(j<=student):
               print("\t",j, end=") ")
               name=(input("ENTER STUDENT's FULL NAME: "))
               gender=int(input("SELECT GENDER: \n\t\t1. Male \n\t\t2. Female      \nYOUR INPUT(1/2): "))
               if(gender==1):
                   male=male+1
               else:
                    female=female+1
               j=j+1
               totalstudent=totalstudent + 1
           print("\nTotal Male Number Of Studets is:",male)
           print("Total Female Number Of Studets is:",female)
           print("\n\tPROCESS DONE!\n\n")

       elif(choise3 == 2):
           break

       else:
           print("YOU ENTERED WRONG INPUT! TRY AGAIN\n")
           continue

#EXAM NUMBER GIVE TO A CLASS THAT's FUNCTUON
def mask_entry():
    print("\n")
    print("\t\t\t*********************************")
    print("\t\t\t||     EXAM NUMBER ENTRY       ||")
    print("\t\t\t*********************************\n")
    loop1=0
    while loop1 != 2:
        choise1=int(input("SELECT BELLOW ONE OF THEM:- \n\t 1. GIVE NUMBER TO A CLASS STUDENTS. \n\t 2. EXIT.  \n\nYOUR INPUT(1/2): "))
        if(choise1==1):
            print("\n\n")
            print("\t\t\t    GIVE NUMBER TO A CLASS STUDENTS")
            print("\t\t\t****************************************\n")
            clas=int(input("ENTER CLASS NUMBER WHICH YOU GIVE EXAM NUMBER(1-12): "))
            students=int(input("HOW MANY STUDENTS IN THIS CLASS(1-n): "))
            subject=int(input("HOW MANY SUBJECTS IN THIS CLASS(1-n): "))
            sub_num=int(input("ENTER EACH SUBJECT TOTAL NUMBER: "))
            total_musk=subject*sub_num
            loop2=1
            while(loop2<=students):
                print("\nSTUDENT NUMBER:",loop2)
                name1=input("ENTER STUDENT NAME: ")
                total=0
                loop3=1
                while(loop3<=subject):
                    print("\tSUBJECT NUMBER:",loop3)
                    number=float(input("\t\t\tENTER SUBJECT NUMBER OF THIS STUDENT: "))
                    total=total+number
                    loop3=loop3+1
                parsentage= (total*100)/total_musk
                print("\n\t\tTOTAL NUMBER OF THIS STUDENT IS:",total)
                print("\t\tPARSENTAGE IS:",parsentage,"%")
                loop2=loop2+1
            print("\n\tNUMBER ENTERY IS COMPLETED!\n\n")
        
        elif(choise1 == 2):
            break
        else:
            print("YOU ENTER WRONG INPUT.....\n")
            continue

#TEACHER SALARY FUNCTION
def teacher_salary():
    print("\n")
    print("\t\t\t*********************************")
    print("\t\t\t||    TEACHERS SALARY ENTRY    ||")
    print("\t\t\t*********************************\n")
    cash=0
    loop7=0
    while loop7 != 2:
        choise4=int(input("SELECT BELLOW ONE OF THEM:- \n\t 1. GIVE TEACHER SALARY SARVEY. \n\t 2. EXIT.  \n\nYOUR INPUT(1/2): "))
        if(choise4 == 1):
            print("\n\t\t    GIVE TEACHER SALARY SARVEY")
            print("\t\t\t************************************\n")
            sir_num=int(input("\tENTER TOTAL NUMBERS OF TEACHERS: "))
            loop5=1
            while(loop5<=sir_num):
                teacher_name=input("\n\t\tENTER TEACHER NAME: ")
                salary=float(input("\t\tENTER THIS TEACHER's SALARY: "))
                cash=cash+salary
                loop5=loop5+1
            print("\nALL THE TEACHERS TOTAL CASH IS:",cash)
            print("\n\n\tALL TEACHERS SLARY PROCESS COMPLETED!\n\n")
        elif(choise4 == 2):
            break
        else:
            print("YOU ENTER WRONG INPUT.....\n")
            continue

# MAIN MENU PART 
loop4=0
while(loop4 != 3):
    choise2=int(input("\n\nMAIN MENU :- \n\t1. NAME ENTRY OF STUDENTS. \n\t2. EXAM NUMBER ENTRY. \n\t3. TEACHERS SALARY ENTRY. \n\t4. EXIT    \n\nYOUR INPUT(1-4): "))
    if(choise2 == 1):
        name_entry()
        os.system("cls")
        continue
    elif(choise2 == 2):
        mask_entry()
        os.system("cls")
        continue
    elif(choise2 == 3):
        teacher_salary()
        os.system("cls")
        continue
    elif(choise2 == 4):
        print("\nTHANKS! WE WILL BE MEET AGAIN.\nHAVE A GOOD DAY ")
        break
    else:
        print("\nSORRY !\nYOU ENTERED WRONG INPUT. TRY AGAIN....")
        continue
    loop4 = loop4 + 1
