Basic_salary=float(input("ENTER BASIC SALARY: "))
if(Basic_salary<=1500):
    HRA=Basic_salary*(10/100)
    DA=Basic_salary*(90/100)
    Gross_Salary=Basic_salary+DA+HRA
    print("Gross Salary IS =",Gross_Salary)
else:
    HRA=500
    DA=Basic_salary*(98/100)
    Gross_Salary=Basic_salary+DA+HRA
    print("Gross Salary IS =",Gross_Salary)
