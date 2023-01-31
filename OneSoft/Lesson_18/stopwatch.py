from tkinter import *
from datetime import datetime


def tick():
    global user_time, after_id
    after_id = window.after(1000, tick)
    user_time_format = datetime.utcfromtimestamp(user_time).strftime('%M:%S')
    stopwatch_label.config(text=user_time_format)
    user_time += 1


def start_stopwatch():
    start_button.grid_forget()
    stop_button.grid(row=1, columnspan=2)
    tick()


def stop_stopwatch():
    stop_button.grid_forget()
    continue_button.grid(row=1, column=0)
    reset_button.grid(row=1, column=1)
    window.after_cancel(after_id)


def continue_stopwatch():
    continue_button.grid_forget()
    reset_button.grid_forget()
    stop_button.grid(row=1, columnspan=2)
    tick()


def reset_stopwatch():
    global user_time
    user_time = 0
    stopwatch_label.config(text="00:00")
    continue_button.grid_forget()
    reset_button.grid_forget()
    start_button.grid(row=1, columnspan=2)


user_time = 0
after_id = ''

window = Tk()
window.title('Stopwatch')
window.bind('q', exit)

stopwatch_label = Label(window, width=5, font=('Comic Sans MS', 100), text='00:00')
stopwatch_label.grid(row=0, columnspan=2)

start_button = Button(window, text='start', font=('Comic Sans MS', 30), command=start_stopwatch)
stop_button = Button(window, text='stop', font=('Comic Sans MS', 30), command=stop_stopwatch)
continue_button = Button(window, text='continue', font=('Comic Sans MS', 30), command=continue_stopwatch)
reset_button = Button(window, text='reset', font=('Comic Sans MS', 30), command=reset_stopwatch)

start_button.grid(row=1, columnspan=2)

window.mainloop()
