import tkinter as tk
from time import strftime
from typing import Union


time_label: Union[tk.Label, None] = None
day_label: Union[tk.Label, None] = None
date_label: Union[tk.Label, None] = None


def update_clock():
    global time_label, day_label, date_label

    time_format = strftime('%H:%M:%S')
    time_label.config(text=time_format)

    day_format = strftime('%A')
    day_label.config(text=day_format)

    date_format = strftime('%B %d, %Y')
    date_label.config(text=date_format)
    window.after(1000, update_clock)


def create_clock():
    global time_label, day_label, date_label

    time_label = tk.Label(window, font=('Arial', 50), fg='#00ffff', bg='black')
    day_label = tk.Label(window, font=('Comic Sans MS', 25))
    date_label = tk.Label(window, font=('Comic Sans MS', 15))

    time_label.pack()
    day_label.pack()
    date_label.pack()


window = tk.Tk()
window.title('Clock')
window.resizable(False, False)
window.bind('<Escape>', exit)

create_clock()

update_clock()

window.mainloop()
