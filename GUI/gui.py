from tkinter import *

window = Tk()


def btn_click():
    Label(window, text="Hello World!").pack()


def window_screen():
    window.geometry("800x500")
    window.title("User Interface")
    Label(window, text="Shahin").pack()
    btn = Button(window, text="Click Me!", bg="teal",
                 fg="#fff", command=btn_click).pack()
    window.mainloop()


window_screen()
