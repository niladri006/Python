loop=''
while(loop!=3):
    print("\t\t\t INDIAN STEEL COMPANY   \n")
    Hardness=float(input("1) Enter Hardness of the steel: "))
    Carbon_content=float(input("2) Enter Carbon content of the steel: "))
    Tensile_strength=float(input("3) Enter Tensile Strength of the steel: "))
    print("\nResult ---")
    
    if(Hardness > 50 and Carbon_content < 0.7 and Tensile_strength > 5600):
        print("\tGrade is 10")
        print("\n\n")
        continue
    if(Hardness > 50 and Carbon_content < 0.7):
        print("\tGrade is 9")
        print("\n\n")
        continue
    if(Carbon_content < 0.7 and Tensile_strength > 5600):
        print("\tGrade is 8")
        print("\n\n")
        continue
    if(Hardness > 50 and Tensile_strength > 5600):
        print("\tGrade is 7")
        print("\n\n")
        continue
    if(Hardness > 50 or Carbon_content < 0.7 or Tensile_strength > 5600):
        print("\tGrade is 6")
        print("\n\n")
        continue
    else:
        print("\tGrade is 5")
        print("\n\n")
        continue
    
