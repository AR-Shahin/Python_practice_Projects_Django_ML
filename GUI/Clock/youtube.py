
from tkinter import *
import time


window = Tk()
window.title("Digital Clock")


def Time():
    timeVar = time.strftime("%I: %M %S %p")
    label.config(text=timeVar)
    label.after(200, Time)


label = Label(window, text="clock", font=('Arial', 100), bg='black', fg='red')
label.pack()
Time()
window.mainloop()
