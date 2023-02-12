from tkinter import *
import os
from tkinter import messagebox
from typing import Union
from werkzeug.security import generate_password_hash, check_password_hash
import json
from json import JSONDecodeError
from typing import List, Dict
import pickle

from OneSoft.Lesson_20.auth_new.front.interfaces import WindowInterface, WindowEntryInterface

def init_db(filename: str):
    if os.path.exists(filename):
        return True
    with open(filename, 'w') as file:
        pass

class MainWindow(Tk, WindowInterface):
    def __init__(self):
        super().__init__()
        self.geometry('300x250')
        self.resizable(False, False)
        self.title('Account manager')

        self.create_user_interface()

    def create_user_interface(self):
        Label(self, text='Select your choice', bg='blue', fg='white', width='300', height='2', font=('Calibri', 13)).\
            place(relx=0.5, rely=0.1, anchor=CENTER)
        Button(self, text='Login', height='2', width='30', command=self.call_login_window)\
            .place(relx=0.5, rely=0.4, anchor=CENTER)
        Button(self, text='Register', height='2', width='30', command=self.call_register_window)\
            .place(relx=0.5, rely=0.7, anchor=CENTER)

    def call_login_window(self):
        LoginWindow(self)

    def call_register_window(self):
        RegisterWindow(self)


class LoginWindow(Toplevel, WindowInterface, WindowEntryInterface):
    login = False

    def __init__(self, root_window):
        super().__init__(master=root_window)
        self.title('Login')
        self.geometry('300x250')
        self.resizable(False, False)
        self.grab_set()

        self.login = StringVar()
        self.password = StringVar()

        self.login_entry: Union[Entry, None] = None
        self.password_entry: Union[Entry, None] = None

        self.create_user_interface()

    def create_user_interface(self):
        Label(self, text='Please enter details bellow to login').\
            place(relx=0.5, rely=0.1, anchor=CENTER)

        Label(self, text='Username *')\
            .place(relx=0.5, rely=0.3, anchor=CENTER)
        self.login_entry = Entry(self, textvariable=self.login)
        self.login_entry.place(relx=0.5, rely=0.4, anchor=CENTER)

        Label(self, text='Password *') \
            .place(relx=0.5, rely=0.6, anchor=CENTER)
        self.password_entry = Entry(self, textvariable=self.password, show='*')
        self.password_entry.place(relx=0.5, rely=0.7, anchor=CENTER)

        Button(self, text='Login', width=10, height=1, command=self.get_user_credentials)\
            .place(relx=0.5, rely=0.9, anchor=CENTER)

    def get_user_credentials(self):
        print(self.login.get())
        print(self.password.get())
        self.login_entry.delete(0, END)
        self.password_entry.delete(0, END)
        # self.destroy()

    def read_user_credential(self, filename: str):
        with open(filename, 'r') as file:
            try:
                credentials = json.load(file)
            except JSONDecodeError:
                return []
        return credentials

    # @property
    # def log_pass(self):
    #     with open("data.json", "r") as f:
    #         data = f.read()
    #         json_data = json.load(data)
    #         return json_data
    #     f.close()
    #     if self.login.get() in a:
    #         if generate_password_hash(self.password.get()) == a[self.login.get()]:
    #             messagebox.showinfo("Вход выполнен", "Добро пожаловать!")
    #         else:
    #             messagebox.showerror("Ошибка", "Неверные данные. Повторите снова.")
    #     else:
    #         messagebox.showerror("Ошибка", "Неверный логин")


class RegisterWindow(Toplevel, WindowInterface, WindowEntryInterface):
    def __init__(self, root_window):
        super().__init__(master=root_window)
        self.title('Register')
        self.geometry('300x400')
        self.resizable(False, False)
        self.grab_set()

        self.login = StringVar()
        self.password = StringVar()
        self.password_repeat = StringVar()
        self.show_pass = IntVar()

        self.login_entry: Union[Entry, None] = None
        self.password_entry: Union[Entry, None] = None
        self.password_repeat_entry: Union[Entry, None] = None
        self.show_pass_checkbox: Union[Checkbutton, None] = None
        self.label_error: Union[Label, None] = None

        self.create_user_interface()

    def check_is_password_strong(self, password: str):
        if len(password) <= 8:
            return False
        self.show_message()
        return True

    def show_message(self, error: str = ''):
        self.label_error['text'] = error

    def on_invalid(self):
        self.show_message('Weak password')

    def write_user_credential(self, filename: str, credentials: List[Dict[str, str]]):
        with open(filename, 'w') as file:
            json.dump(credentials, file, indent=4)

    # def save(self):
    #     login_pass_save = [{
    #         "login": self.login.get(),
    #         "password": generate_password_hash(self.password.get())}]
    #     json_obj = json.load(login_pass_save)
    #     with open("data.json", "w") as f:
    #         f.write(json.dump(json_obj, indent=2, ensure_ascii=False))
    #     f.close()
    #     LoginWindow()
    #
    # def add_to_json(self):
    #     login_pass_save = [{
    #         "login": self.login.get(),
    #         "password": generate_password_hash(self.password.get())
    # }]
    #     data = json.load(open("data.json"))
    #     data.append(login_pass_save)
    #     with open("data.json", "w") as file:
    #         json.dump(data, file, indent=2, ensure_ascii=False)


    def create_user_interface(self):
        validate_password = (self.register(self.check_is_password_strong), '%P')
        invalid_password = (self.register(self.on_invalid),)

        Label(self, text='Please enter data bellow to registration').\
            place(relx=0.5, rely=0.05, anchor=CENTER)

        Label(self, text='Username *')\
            .place(relx=0.5, rely=0.15, anchor=CENTER)
        self.login_entry = Entry(self, textvariable=self.login)
        self.login_entry.place(relx=0.5, rely=0.25, anchor=CENTER)

        self.label_error = Label(self, fg='red')
        self.label_error.place(relx=0.6, rely=0.32)

        Label(self, text='Password *') \
            .place(relx=0.5, rely=0.35, anchor=CENTER)
        self.password_entry = Entry(self,
                                    textvariable=self.password,
                                    validate='focusout',
                                    validatecommand=validate_password,
                                    invalidcommand=invalid_password,
                                    show='*')
        self.password_entry.place(relx=0.5, rely=0.45, anchor=CENTER)

        Label(self, text='Repeat password *') \
            .place(relx=0.5, rely=0.55, anchor=CENTER)
        self.password_repeat_entry = Entry(self,
                                           textvariable=self.password_repeat,
                                           validate='focusout',
                                           validatecommand=validate_password,
                                           invalidcommand=invalid_password,
                                           show='*')
        self.password_repeat_entry.place(relx=0.5, rely=0.65, anchor=CENTER)

        self.show_pass_checkbox = Checkbutton(self,
                                              text='Show password',
                                              command=self.change_show_password,
                                              variable=self.show_pass)
        self.show_pass_checkbox.place(relx=0.3, rely=0.75)

        Button(self, text='Registration', width=10, height=1, command=self.get_user_credentials)\
            .place(relx=0.5, rely=0.9, anchor=CENTER)

    def change_show_password(self):
        state = '' if self.show_pass.get() else '*'
        self.password_entry.config(show=state)
        self.password_repeat_entry.config(show=state)

    def get_user_credentials(self):
        print(self.login.get())
        password_hash = generate_password_hash(self.password.get())
        print(check_password_hash(password_hash, '123456'))
        print(generate_password_hash(self.password_repeat.get()))

        self.login_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.password_repeat_entry.delete(0, END)

        # self.destroy()

def main(username: str, pass_hash: str, filename: str):
    init_db(filename)
    credentials = LoginWindow.read_user_credential(filename)
    new_user = {
        'username': username,
        'pass_hash': pass_hash
    }
    credentials.append(new_user)
    RegisterWindow.write_user_credential(filename, credentials)

DB_NAME = 'user.json'

if __name__ == '__main__':
    nick_name = 'pocker'
    user_pass_hash = '260000$LEKlPHCXsoS67dsU$e01f6a7d737fde785aba8a6a8a5a94117a689cb3c217c56b1b424a0478adbf60'
    main(nick_name, user_pass_hash, DB_NAME)