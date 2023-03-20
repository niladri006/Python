startsection=int(input("ENTER STARTING CLASS IN YOUR SCHOOL: "))
endsection=int(input("ENTER ENDING CLASS IN YOUR SCHOOL: "))
totalstudent=0
male=0
female=0
for i in range(startsection,endsection+1):
    print("\nCLASS NO:",i)
    student=int(input("HOW MANY STUDENTS IN THIS CLASS: "));
    j=1
    for j in range(1,student+1):
        name=(input("\tENTER STUDENT's FULL NAME: "))
        sex=int(input("\t\t1. Male. \n\t\t2. Female. "))
        if(sex==1):
            male=male+1
        else:
            female=female+1
        j=j+1
        totalstudent=totalstudent + 1
i=i+1
print("\nTotal Number of Students in all Classes(",startsection,"to",endsection,") is",totalstudent)
print("Total Male Number Of Studets is:",male)
print("Total Female Number Of Studets is:",female)
