
from tkinter import *
import time


window = Tk()
window.title('Digital Clock')


def Time():

    timeVar = time.strftime("%I: %M: %S %P")
    label.config(text=timeVar)
    label.after(200, Time)


label = Label(window, text="Clock", font=('Arial', 100), bg='black', fg='red')
label.pack()
Time()
window.mainloop()
