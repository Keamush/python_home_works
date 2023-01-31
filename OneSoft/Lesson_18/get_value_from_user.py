from tkinter import Tk, Entry, Button, END


def get_user_credentials():
    login = user_login.get()
    print(login)
    user_login.delete(0, END)
    text = ''
    if login != 'root':
        text = 'Incorrect login'
    user_login.insert(0, text)


window = Tk()
window.title('User login')
window.geometry('300x200+500+300')
window.bind('q', exit)

user_login = Entry(window, font=('Comic Sans MS', 15))
user_login.grid(row=0, columnspan=2)

get_login_button = Button(window, text='login', font=('Comic Sans MS', 15), command=get_user_credentials)
get_login_button.grid(row=1, column=1)

window.mainloop()


















