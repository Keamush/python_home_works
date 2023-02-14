import os
import tkinter as tk
from tkinter import messagebox


def clip_board(text):
    command = f'echo {text} | clip'
    os.system(command)


def calculate(operation):
    global result_value

    if operation == 'C':
        result_value = ''
    elif operation == 'del':
        result_value = result_value[:-1]
    elif operation == 'X^2':
        try:
            result_value = str(eval(result_value) ** 2)
        except (ZeroDivisionError, SyntaxError):
            messagebox.showerror('Error', 'Use correct values.')
    elif operation == '+/-':
        try:
            result_value = str(eval(result_value) * -1)
        except SyntaxError:
            messagebox.showerror('Error', 'Value cannot be empty')
    elif operation == '=':
        try:
            result_value = str(eval(result_value))
        except (ZeroDivisionError, SyntaxError):
            messagebox.showerror('Error', 'Incorrect operation')
            result_value = '0'
    elif operation == 'Copy':
        clip_board(result_value)
    else:
        if result_value == '0':
            result_value = ''
        result_value += operation
    result_label.configure(text=result_value)


window = tk.Tk()
window.title('Calculator')
window.geometry('500x550+300+200')
window.resizable(False, False)
window.config(bg='black')
window.bind('<Escape>', exit)


result_value = '0'
result_label = tk.Label(text=result_value, font=('Roboto', 30, 'bold'), bg='black', fg='white')
result_label.place(x=11, y=50)

buttons = ['C', 'del', '+', '=', '1', '2', '3', '/', '4', '5', '6', '*', '7', '8', '9', '-',
           '+/-', '0', 'Copy', 'X^2']

pad_x = 18
pad_y = 140

for button in buttons:
    get_value = lambda x = button: calculate(x)
    tk.Button(text=button, bg='salmon', font=('Roboto', 20), command=get_value)\
        .place(x=pad_x, y=pad_y, width=115, height=80)

    pad_x += 115
    if pad_x > 400:
        pad_x = 18
        pad_y += 80

window.mainloop()
