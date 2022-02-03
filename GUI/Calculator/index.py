

from tkinter import *


window = Tk()
window.title("Calculator")

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
operators = ["+", "-", "*", "/"]

operations = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication",
    "/": "division",
}
first_number = ''
operation = ""


def display_clear():
    display.delete(0, END)


def append_number(num):
    current = display_value()
    display_clear()
    display.insert(0, (current + str(num)))


def btn_click(payload):
    if payload == "C":
        display_clear()
    elif payload == "=":
        calculate()
    elif payload in operators:
        handle_operator(operations[payload])
    else:
        append_number(payload)


def display_value():
    return display.get()


def set_display_value(value):
    display_clear()
    display.insert(0, value)


def handle_operator(operator):
    f_number = display_value()
    global first_number
    global operation
    operation = operator
    first_number = int(f_number)
    display_clear()


def calculate():
    second_number = display_value()
    result = -1
    if operation == 'addition':
        result = first_number + int(second_number)
    if operation == 'subtraction':
        result = first_number - int(second_number)
    if operation == 'multiplication':
        result = first_number * int(second_number)
    if operation == 'division':
        try:
            result = first_number / int(second_number)
        except:
            result = 0
    set_display_value(result)


    # Display
display = Entry(window, width=45, borderwidth=2)
display.grid(row=0, columnspan=4, pady=5, padx=2)
display.insert(0, "")
# Buttons
button_1 = Button(window, text="1", padx=40, pady=20,
                  command=lambda: btn_click("1"))
button_2 = Button(window, text="2", padx=40, pady=20,
                  command=lambda: btn_click("2"))
button_3 = Button(window, text="3", padx=40, pady=20,
                  command=lambda: btn_click("3"))
button_4 = Button(window, text="4", padx=40, pady=20,
                  command=lambda: btn_click("4"))
button_5 = Button(window, text="5", padx=40, pady=20,
                  command=lambda: btn_click("5"))
button_6 = Button(window, text="6", padx=40, pady=20,
                  command=lambda: btn_click("6"))
button_7 = Button(window, text="7", padx=40, pady=20,
                  command=lambda: btn_click("7"))
button_8 = Button(window, text="8", padx=40, pady=20,
                  command=lambda: btn_click("8"))
button_9 = Button(window, text="9", padx=40, pady=20,
                  command=lambda: btn_click("9"))
button_0 = Button(window, text="0", padx=40, pady=20,
                  command=lambda: btn_click("0"))
button_add = Button(window, text="+", padx=40, pady=20,
                    command=lambda: btn_click("+"))
button_equal = Button(window, text="=", padx=40, pady=20,
                      command=lambda: btn_click("="))
button_clear = Button(window, text="C", padx=40,
                      pady=20, command=lambda: btn_click("C"))

button_subtract = Button(window, text="-", padx=41,
                         pady=20, command=lambda: btn_click("-"))
button_multiply = Button(window, text="*", padx=40,
                         pady=20, command=lambda: btn_click("*"))
button_divide = Button(window, text="/", padx=41, pady=20,
                       command=lambda: btn_click("/"))

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)


button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_add.grid(row=4, column=3)


window.mainloop()
