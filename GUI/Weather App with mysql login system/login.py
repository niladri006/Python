from tkinter import *
from tkinter import messagebox
import mysql.connector

background="#06283d"
framebg='#ededed'
framefg='#06283d'

root=Tk()
root.title('  Login System')
root.geometry("1250x700+210+50")
root.config(bg=background)
root.resizable(False,False)

global trial_no
trial_no=0
def trial():
    global trial_no
    trial_no +=1
    print(f'trail no is {trial_no}')
    if (trial_no==3):
        messagebox.showwarning('Warning',f'You tried {trial_no} times')
        root.destroy()


def loginuser():
    username = user.get()
    password = code.get()
    
    if (username == '' or username == 'Username') or (password=='' or password == 'Password'):
        messagebox.showerror('Entry Error', 'Type username & Password!')
        
    else:
        
        try:
            mydb=mysql.connector.connect(host='localhost', user='root', password='nil@2001', database='studentregistration')
            mycursor=mydb.cursor()
            print('Connected To Database')
        except:
            messagebox.showerror('Connection', 'Database connection not stablish!')
            return
        
        command="use studentregistration"
        mycursor.execute(command)
        
        command ='select * from login where Username=%s and Password=%s'
        mycursor.execute(command,(username, password))
        myresult=mycursor.fetchone()
        print(myresult)
        
        if myresult==None:
            messagebox.showerror('Invalid', 'Invalid username & Password!')
            
            trial()
        else:
            root.destroy()
            import main
    

def register():
    root.destroy()
    import register


#icon image
root.iconbitmap('icon.ico')

#background image
frame=Frame(root, bg='red')
frame.pack(fill=Y)


backgroundimage=PhotoImage(file='LOGIN.png')
Label(frame,image=backgroundimage).pack()


#user entry
def user_entry(e):
    user.delete(0,'end')

def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user=Entry(frame,width=18, fg='#fff',border=0,bg='#375174', font=('Arial Bold', 24))
user.insert(0,'Username')
user.bind('<FocusIn>', user_entry)
user.bind('<FocusOut>', user_leave)
user.place(x=500, y=315)

#Password entry
def password_entry(e):
    code.delete(0,'end')

def password_leave(e):
    if code.get()=='':
        code.insert(0,'Password')


code=Entry(frame,width=18, fg='#fff',border=0,bg='#375174', font=('Arial Bold', 24))
code.insert(0,'Password')
code.bind('<FocusIn>', password_entry)
code.bind('<FocusOut>', password_leave)
code.place(x=500, y=410)



# hide & show button
button_mode =True

def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye, activebackground='white')
        code.config(show='*')
        button_mode=False
    else:
        eyeButton.config(image=openeye,activebackground='white')
        code.config(show='')
        button_mode=True

openeye=PhotoImage(file='openeye.png')
closeeye=PhotoImage(file='close eye.png')
eyeButton=Button(frame,image=openeye,bg='#375174', bd=0, cursor='hand2', command=hide)
eyeButton.place(x=780,y=410)




loginButton=Button(root, text='LOGIN', fg='white', bg='#1f5675', width=10, height=1, font=('Arial',16,'bold'), bd=0, cursor='hand2', command=loginuser)
loginButton.place(x=570, y=600)

label=Label(root, text="Don't have an account?", fg='#fff',bg='#00264d', font=('Microsoft YaHei UI Light', 9))
label.place(x=500, y=500)


registerButton=Button(root, width=10, text="Add new user", border=0, bg='#00264d', cursor='hand2', fg='#57a1f8', command=register)
registerButton.place(x=650, y=500)






root.mainloop()