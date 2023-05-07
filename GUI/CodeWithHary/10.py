from tkinter import *
from PIL import ImageTk, Image

def every_100(text):
    final_text =""
    for i in range(0, len(text)):
        a =+ text[i]
        if i%100 == 0 and i != 0:
            final_text += "\n"
        return final_text
            

root = Tk()
# width x hight
root.geometry("1000x800")
root.title("NEWS")

texts = []
photos = []
for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(text)
        
    image = image.open(f"{i+1}.png")
    #TODO: Resize these images
    
    
    photos.append(ImageTk.PhotoImage(image))
    
f0 = Frame(root, width=800, height=70)
Label(f0, text="Code with harry news", font="lucida 33 bold").pack()
Label(f0, text="Janary 19 2050", font="lucida 13 bold").pack()

f1 = Frame(root, width=900, height=200)
Label(f1, text=texts[0], padx=22, pady=22).pack(side=LEFT)
f1.pack(anchor="w")
    


root.mainloop()