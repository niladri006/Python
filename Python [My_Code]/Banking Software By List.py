ch = ''
while (ch != 7):
    print("\n\nMAIN MENU")
    print("\t[1] NEW ACCOUNT")
    print("\t[2] DEPOSIT AMOUNT")
    print("\t[3] WITHDRAW AMOUNT")
    print("\t[4] BALANCE ENQUIRY")
    print("\t[5] CLOSE AN ACCOUNT")
    print("\t[6] CHANGE PASSWORD")
    print("\t[7] EXIT")
    ch = int(input("Input: "))
    if (ch == 1):
        name_list = []
        pass_list = []
        type_list = []
        amo_list = []
        print("\t\t***********************")
        print("\t\t*     NEW ACCOUNT     *")
        print("\t\t***********************")
        name = input("\tENTER NAME: ")
        name_list.append(name)
        acc_num = input("\tENTER YOUR PASWORD: ")
        rt = pass_list.count(acc_num)
        if (rt != 1):
            pass_list.append(acc_num)
        else:
            print("THIS PASSWORD IS ALREADY USED !")
        acc_type = input("\tENTE THE TYPE OF ACCOUNT [C/S] : ")
        if (acc_type == "C" or acc_type == "c" or acc_type == "CURRENT" or acc_type == "current"):
            type_list.append("CURRENT")
        else:
            type_list.append("SAVINGS")
        deposit = int(
            input("\tENTER THE INITIAL AMOUNT(>=500) FOR SAVING & (>=1000) FOR CURRENT : "))
        amo_list.append(deposit)
        print("\n\tACCOUNT CREATED!\n\n")

    elif (ch == 2):
        print("\t\t***********************")
        print("\t\t*   DEPOSIT AMOUNT    *")
        print("\t\t***********************")
        password1 = input("\tENTER YOUR PASSWORD: ")
        if (pass_list.count(password1) == 0):
            print("\n\tYOU ENTER WRONG PASSWORD...")
            print("\tPLEASE TRY AGAIN....")
            continue
        else:
            x = pass_list.index(password1)
            print("\n\tWELLCOME ", name_list[x])
            d_c = int(input("\tENTER DEPOSITE AMOUNT: $"))
            if (d_c > 0):
                amo_list[x] = amo_list[x] + d_c
                print("\n\tAMOUNT DEPOSITE !\n")
            elif (d_c == 0):
                print("NOTHING TO ADD")
            else:
                print("NOTHING TO ADD")

    elif (ch == 3):
        print("\t\t***********************")
        print("\t\t*   WITHDRAW AMOUNT   *")
        print("\t\t***********************")
        password2 = input("\tENTER YOUR PASSWORD: ")
        if (pass_list.count(password2) == 0):
            print("\n\tYOU ENTER WRONG PASSWORD...")
            print("\tPLEASE TRY AGAIN....")
            continue
        else:
            x1 = pass_list.index(password2)
            print("\n\tWELLCOME", name_list[x1])
            w_c = int(input("\tENTER WITHDRAW AMOUNT: $"))
            if (w_c > 0):
                amo_list[x1] = amo_list[x1] - w_c
                print("\n\tAMOUNT WITHDRAW !\n")
            elif (w_c == 0):
                print("NOTHING TO WITHDRAW!")
            else:
                print("NOTHING TO WITHDRAW!")

    elif (ch == 4):
        print("\t\t***********************")
        print("\t\t*   BALANCE ENQUIRY   *")
        print("\t\t***********************")
        password3 = input("\tENTER YOUR PASSWORD: ")
        if (pass_list.count(password3) == 0):
            print("\n\tYOU ENTER WRONG PASSWORD...")
            print("\tPLEASE TRY AGAIN....")
            continue
        else:
            x2 = pass_list.index(password3)
            print("\tPASSWORD MACHED !")
            print("\tAccount Owner -", name_list[x2])
            print("\tAccount Type -", type_list[x2])
            print("\tAccount Amount - $", amo_list[x2])

    elif (ch == 5):
        print("\t\t***********************")
        print("\t\t*  CLOSE AN ACCOUNT   *")
        print("\t\t***********************")
        password4 = input("\tENTER YOUR PASSWORD: ")
        if (pass_list.count(password4) == 0):
            print("\n\tYOU ENTER WRONG PASSWORD...")
            print("\tPLEASE TRY AGAIN....")
            continue
        else:
            x3 = pass_list.index(password4)
            print("\tAccount Owener -", name_list[x3])
            print("\tAccount Type -", type_list[x3])
            print("\tAccount Amount - $", amo_list[x3])
            del name_list[x3]
            del pass_list[x3]
            del type_list[x3]
            del amo_list[x3]
            print("\n\tACCOUNT DELETE !\n")

    elif (ch == 6):
        print("\t\t***********************")
        print("\t\t*  CHENGE PASSWORD    *")
        print("\t\t***********************")
        password5 = input("\tENTER YOUR PASSWORD: ")
        if (pass_list.count(password5) == 0):
            print("\n\tYOU ENTER WRONG PASSWORD...")
            print("\tPLEASE TRY AGAIN....")
            continue
        else:
            x4 = pass_list.index(password5)
            f1 = input("\n\tENTER NEW PASSWORD: ")
            f2 = input("\tENTER CONFIRM PASSWORD: ")
            if (f1 == f2):
                pass_list[x4] = f2
                print("PASSWORD CHENGED !")
            else:
                print("PLEACE ENTER SAME PASSWORD !.....")
                continue

    elif (ch == 7):
        print("\tTHANK YOU !")
        break

    else:
        continue
