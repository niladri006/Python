from tkinter import *

root = Tk()
root.geometry("444x233")
root.title("Niladri Chatterjee")

# Impotant Label for Option

# Text => adds the Text
# bg => background
# fg => foreground
# font => chenge fonts | fonts=("<font_style_name>", <text_size>, "<text_style_name>")
#1.  font=("conicsansms",15, "bold")
#2.  font=("conicsansms 15 bold")
# padx => x padding
# pady => y padding
# relief =>  border styling => SUNKEN
#                           => RAISED 
#                           => GROOVE
#                           => RIDGE


title_label = Label(text='''From financial transactions to operational decisions and beyond, the core of every business     function relies on an organization’s greatest asset: its human resources. As such, human resources boast significant responsibility for the success or failure of an organization (de Waal, 2007; Haslinda, 2009). The value of human resources is not always widely apparent. In fact, present day perception frequently limits human  resource management (HRM) and human resource development (HRD) to recruitment, compensation, and legalities of managing a workforce (Haslinda, 2009). This review identifies the emergent value of human resources, the transformation from education and training to HRD, and the relative importance of HRD to organizational leaders. Specifically, it outlines the reliance of high performance organizations (HPOs) on HRM and HRD, concluding with the present day critical issues facing HRM and HRD.''', bg="green", relief="sunken", fg="Yellow", padx=5, pady=15, font=("conicsansms 9 bold")
                    )




# Impotant Pack for Option

# anchoer = "nw/ne/sw/se"
# side = TOP, BUTTON, LEFT, RIGHT
 
title_label.pack(side=BOTTOM, fill=X, padx=15, pady=5)

root.mainloop()