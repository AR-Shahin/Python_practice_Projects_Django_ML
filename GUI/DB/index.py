
import random
from tkinter import *


window = Tk()
window.title("GUI with Database")
window.geometry("800x500")
window.configure(bg='#2f3640')

data = [{
    'id': 1,
    'name': "Shahin",
    "roll": 101
}, {
    'id': 2,
    'name': "Nipa",
    "roll": 102
}
]


def delete_row(key):
    global data
    data.pop(0)
    print(data)
    print_data()


def handle_submit():
    print(get_display_data())
    clear_window()


def get_display_data():
    return {
        'name': name.get(),
        'roll': roll.get(),
        'id': random.randint(20, 30)
    }


def clear_window():
    name.delete(0, END)
    roll.delete(0, END)


def print_data():
    global data
    i = 3
    j = 0
    for d in data:
        name = "name_{}".format(d['id'])
        name = Label(window, text=d['name']).grid(row=i, column=j, pady=5)

        roll = "roll_{}".format(d['id'])
        roll = Label(window, text=d['roll']).grid(row=i, column=j+1, padx=5)

        btn = "btn_{}".format(d['id'])
        btn = Button(window, text="Delete", command=lambda: delete_row(d)).grid(
            row=i, column=j+2)
        i += 1
        j = 0


def handle_submit():
    global data
    # data.append({
    #     'id': 3,
    #     "name": "Omi",
    #     "roll": 103
    # })
    data.append(get_display_data())
    clear_window()
    print_data()


label = Label(window, text="Email : ")
label.grid(row=0, column=0, pady=5)
name = Entry(window)
name.grid(row=0, column=1)

label2 = Label(window, text="Roll : ")
label2.grid(row=1, column=0)
roll = Entry(window)
roll.grid(row=1, column=1)

submit = Button(window, text="Submit", bg='teal',
                command=handle_submit).grid(row=2, pady=5)


window.mainloop()
