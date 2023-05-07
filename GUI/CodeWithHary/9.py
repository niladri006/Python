from tkinter import *

def harry(event):
    print(f"Press at {event.x}, {event.y}")

root = Tk()
# width x hight
root.geometry("633x344")
root.title("Events in Tkinter")


widget = Button(root, text="click me")
widget.pack()

widget.bind("<Button-1>", harry)
widget.bind("<Double-1>", quit)


root.mainloop()