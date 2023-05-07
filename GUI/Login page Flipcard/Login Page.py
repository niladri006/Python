from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# Commend def here
def handel_login():
    email = email_input.get()
    password = password_input.get()
    
    if email == 'niladri@gmail.com' and password == '1234':
        messagebox.showinfo('Flipkart','Login Succesful!')
    else:
        messagebox.showerror('Flipkart','Login Failed!')



# Basic GUI Box creation
root = Tk()
root.title('Login From')
root.iconbitmap('favicon.ico')
root.geometry('350x500')
root.configure(background='#0096dc')




# Flipkart logo img heading 
img = Image.open('flipkart_icon.png')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img)
img_label.pack(pady=(10,10))




# Flipkart text heading
text_label = Label(root, text="Flipkart", fg="white", bg="#0096dc")
text_label.pack()
text_label.config(font=('verdana', 24))





# Email text & entry box create
email_label = Label(root, text="Enter Email", fg="white", bg="#0096dc")
email_label.pack(pady=(20,5))
email_label.config(font=('verdana', 18))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1,15))




# Password text & entry box create
password_label = Label(root, text="Enter Password", fg="white", bg="#0096dc")
password_label.pack(pady=(20,5))
password_label.config(font=('verdana', 18))

password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1,15))



# Login button creation
login_btn = Button(root, text="Login Here", bg='white', fg='black', width=20, height=2, command=handel_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))


root.mainloop()