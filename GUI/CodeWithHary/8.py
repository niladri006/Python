from tkinter import *

# "SAVE" Button & pack
def getvalues():
    print(f"register sucssfully")
    
    print(f"{nameValue.get(), phoneValue.get(), genderValue.get(), emergencyValue.get(), paymentmodeValue.get(), foodServiceValue.get()}")
    
    
    with open("records.data","w") as f:
        f.write(f"{nameValue.get(), phoneValue.get(), genderValue.get(), emergencyValue.get(), paymentmodeValue.get(), foodServiceValue.get()}")



root = Tk()
# "width x hight"
root.geometry("355x355")
root.title("  From")
root.iconbitmap("favicon.ico")

# Heading 
Label(root, text="WELLCOME", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

# Text for our from 
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmode = Label(root, text="Payment Mode")

# Pack text for your from
name.grid(row=1, column=2, padx=15)
phone.grid(row=2, column=2, padx=15)
gender.grid(row=3, column=2, padx=15)
emergency.grid(row=4, column=2, padx=15)
paymentmode.grid(row=5, column=2, padx=15)

#Tkinter variable for storing entries
nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emergencyValue = StringVar()
paymentmodeValue = StringVar()
foodServiceValue = IntVar()

# Entries for our from 
nameEntry = Entry(root,textvariable=nameValue)
phoneEntry = Entry(root,textvariable=phoneValue)
genderEntry = Entry(root,textvariable=genderValue)
emergencyEntry = Entry(root,textvariable=emergencyValue)
paymentmodeEntry = Entry(root,textvariable=paymentmodeValue)

# Packing the Entries for your from 
nameEntry.grid(row=1, column=3, padx=5, pady=5)
phoneEntry.grid(row=2, column=3, padx=5, pady=5)
genderEntry.grid(row=3, column=3, padx=5, pady=5)
emergencyEntry.grid(row=4, column=3, padx=5, pady=5)
paymentmodeEntry.grid(row=5, column=3, padx=5, pady=5)

# Checkbox & packing it
foodService = Checkbutton(text="Want to pre book your meals ?", variable= foodServiceValue)
foodService.grid(row=6, column=3,pady=15)


    
Button(text="SAVE", command=getvalues, padx=5, pady=5).grid(row=7, column=3)


root.mainloop()