from tkinter import *
b= []

def get_result():
    a=float(num1_entry.get())
    b.append(a)
    if(a%2 == 0):
        result_label.config(text=f"{a} is Even")
        print(f"PRESS! {num1_entry.get()} num is Even")


    else:
        result_label.config(text=f"{a} is Odd")
        print(f"PRESS! {num1_entry.get()} num is Odd")

    with open("record.txt", W) as f:
        f.write(f"Numbers Are: {b}")
        


root = Tk()
# width x hight
root.geometry('450x150')
root.title('ODD & EVEN') 
root.iconbitmap('favicon.ico')
root.resizable(0,0)


# create the widgets
heading = Label(root, text="Checking Odd & Even numbers", fg="green", font="Bahnschrift 16 bold")

num1_label = Label(root, text = "Enter number: ", fg="Blue", font="Bahnschrift 10 italic")
num1_entry = Entry(root, relief='sunken', fg='blue', borderwidth=3, bg='AntiqueWhite3', font='Bahnschrift 10')

button = Button(root, text="CHECK THIS!" ,fg="red", bg="DarkSlateGray2",font="Bahnschrift 10 bold", cursor='hand2' ,command=get_result)

result_label = Label(root, text="Result is :", fg="red", font="Bahnschrift 10")



# layout the widgets
heading.grid(row=0, column=1, pady=5)
num1_label.grid(row=1, column=0)
num1_entry.grid(row=1, column=1, padx=10)
button.grid(row=2, column=1, pady=5)
result_label.grid(row=3, column=1)

root.mainloop()