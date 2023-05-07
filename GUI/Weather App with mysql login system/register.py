from tkinter import *
from tkinter import messagebox
import mysql.connector

background ="#06283D"
framebg = "#EDEDED"
framefg ="#06283D"

root = Tk()
root.title("New User Registeration")
root.geometry("1250x700+150+20")
root.config(bg=background)
root.resizable(False, False)

def login():
    root.destroy()
    import login

def register():
    username=user.get()
    password=code.get()
    admincode=adminaccess.get()
    
    # print(username, password, admincode)
    
    if admincode=="nil":
        if(username == "" or username == "UserId") or (password=="" or password=="Password"):
            messagebox.showerror("Entry error", "Type Username and Password!")
            

        else:
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", password="nil@2001")
                mycursor=mydb.cursor() 
                print("Connection Stablished!")
                 
            except:
                messagebox.showerror("Connection", "Database connection not stablished!")
                
                
            try:
                command="create database StudentRegistration"
                mycursor.execute(command)
                
                command="use StudentRegistration"
                mycursor.execute(command)
                
                command="create table login (user int auto_increment key not null, Username varchar(50), Password varchar(100))"
                mycursor.execute(command)
                
            
            except:
                mycursor.execute("use StudentRegistration")
                mydb = mysql.connector.connect(host="localhost", user="root", password="nil@2001", database="StudentRegistration")
                mycursor=mydb.cursor()
                
                command="insert into login(Username, Password) values(%s,%s)"
                mycursor.execute(command, (username, password))
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Register", "New user added Sucessfully!")            
    else:
        messagebox.showerror("Admin code", "Input Corret admin code to add new user")    



# Icon Image
root.iconbitmap("icon.ico")

# Background Image
frame= Frame(root, bg="red")
frame.pack(fill=Y)


backgroundimage= PhotoImage(file="register.png")
Label(frame,image=backgroundimage).pack()

adminaccess= Entry(frame, width=15, fg="#000", border=0, bg="#e8ecf7", font=("Arial Bold",20), show="*")
adminaccess.focus()
adminaccess.place(x=550, y=280)


# <<====================== User Id =============================>>
def user_enter(e):
    user.delete(0,"end")

def user_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"UserId")



user=Entry(frame,width=18, fg="#fff", bg="#375174", border=0, font=("Arial Bold",20))
user.insert(0,"UserId")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=500, y=380)




# <<====================== Password Id =============================>>

def password_enter(e):
    code.delete(0,"end")

def password_leave(e):
    if code.get()=="":
        code.insert(0,"Password")

code=Entry(frame,width=18, fg="#fff", bg="#375174", border=0, font=("Arial Bold",20))
code.insert(0,"Password")
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=500, y=470)

# <<===================================================>>

button_mode = True

def hide():
    global button_mode
    if button_mode:
        eyebutton.config(image=closeeye, activebackground="white")
        code.config(show="*")
        button_mode=False
    else:
        eyebutton.config(image=openeye, activebackground="white")
        code.config(show="")
        button_mode=True


openeye=PhotoImage(file="openeye.png")
closeeye=PhotoImage(file="close eye.png")

eyebutton = Button(root, image=openeye, bg="#375174", bd=0, cursor="hand2", command=hide)
eyebutton.place(x=780, y=470)

# <<===================================================>>

regis_button=Button(root, text="ADD NEW USER", bg="#455C88", fg="white", width=13, height=1, font=("Arial",16,"bold"), bd=0, cursor="hand2", command=register)
regis_button.place(x=530,y=600)


backbuttonimage=PhotoImage(file="backbutton.png")
Backbutton=Button(root, image=backbuttonimage, fg="#deeefb", command=login)
Backbutton.place(x=20, y=15)


root.mainloop()