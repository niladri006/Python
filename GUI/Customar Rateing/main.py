from tkinter import *
from tkinter import messagebox 


root = Tk()
root.geometry('500x330')  # width x hight
root.title('  Customar Review')
root.iconbitmap("icon.ico")

index = 0
List = []

def submit():
    global List
    global index
    List.append(myslider.get())
    if myslider.get() >= 3:
        while True:
            b = messagebox.askquestion("Customar Review","Can you put your rating in Play Store ?")
            if b == "yes":
                messagebox.showinfo("Customar Review", "Go to the Play Store and give your rating")
                break
            else:
                c = messagebox.askquestion("Customar Review", "Are You Sure ?")
                if c == "yes":
                    messagebox.showerror("Customar Review", "Ok! \nWe will ask you later.")
                    break
                else:
                    messagebox.showinfo("Customar Review","Sorry! \nTry again !")
                    continue
    else:
        a = messagebox.askquestion("Customar Review", "Are You sure ?")
        if (a == "yes"):
            messagebox.showinfo("Customar Review", "We are very sorry! \nWe will try better!")
        else:
            messagebox.showerror("Customar Review", "Please Go Again!")
            

    with open("record.txt",W) as f:
        for i in List:
            f.write(f"Customar give {i} stars\n")
    
    

h1 = Label(root, text="Wellcome", font="Aral 15 bold")
h1.pack(pady=4)

h2 = Label(root, text="How much happy by your service ?", font="Aral 10 bold")
h2.pack(pady=7)

myslider = Scale(root, from_=1, to=5, orient=HORIZONTAL, tickinterval=1, font="arial 10 bold")
myslider.set(4)
myslider.pack(fill=X, padx=30)

btn = Button(root, text="Submit !", command=submit)
btn.config(fg="white", bg="green", font="Arial 10 italic", padx=3, pady=2)
btn.pack(pady=15)

root.mainloop()