subject=int(input("Enter How Many Subjects: "))
total=0
total_num=1
result=0
loop=1
while(loop<=subject):
    print("\t",loop,end=" ")
    sub_num=float(input("ENTER NUMBER THIS SUBJECT: "))
    total=total+sub_num
    loop=loop+1
    total_num=subject*100
    result=(total*100)/total_num
print("\n\n")
print("TOTAL NUMBER OF",subject,"SUBJECTS: ",total,"/",total_num)
print("YOUR PARSENTAGE IS: ",result,"%")
