from tkinter import *


def dan_to_n():
    dan = float(decanewton_input.get())
    n = dan * 10
    newton_result_label.config(text=f"{n}")


window = Tk()
window.title("Convert Decanewton to Newton")
window.config(padx=20, pady=20)

decanewton_input = Entry(width=7)
decanewton_input.grid(column=1, row=0)

decanewton_label = Label(text="Decanewton")
decanewton_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

newton_result_label = Label(text="0")
newton_result_label.grid(column=1, row=1)

newton_label = Label(text="Newton")
newton_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=dan_to_n)
calculate_button.grid(column=1, row=2)

window.mainloop()
