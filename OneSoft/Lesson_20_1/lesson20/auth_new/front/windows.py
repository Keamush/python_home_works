import os
from tkinter import *
from typing import Union
from tkinter import messagebox
from werkzeug.security import generate_password_hash, check_password_hash
import json

from OneSoft.Lesson_20_1.lesson20.auth_new.front.interfaces import WindowInterface, WindowEntryInterface


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
        Label(self, text='Select your choice', bg='blue', fg='white', width='300', height='2', font=('Calibri', 13)). \
            place(relx=0.5, rely=0.1, anchor=CENTER)
        Button(self, text='Login', height='2', width='30', command=self.call_login_window) \
            .place(relx=0.5, rely=0.4, anchor=CENTER)
        Button(self, text='Register', height='2', width='30', command=self.call_register_window) \
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
        Label(self, text='Please enter details bellow to login'). \
            place(relx=0.5, rely=0.1, anchor=CENTER)

        Label(self, text='Username *') \
            .place(relx=0.5, rely=0.3, anchor=CENTER)
        self.login_entry = Entry(self, textvariable=self.login)
        self.login_entry.place(relx=0.5, rely=0.4, anchor=CENTER)

        Label(self, text='Password *') \
            .place(relx=0.5, rely=0.6, anchor=CENTER)
        self.password_entry = Entry(self, textvariable=self.password, show='*')
        self.password_entry.place(relx=0.5, rely=0.7, anchor=CENTER)

        Button(self, text='Login', width=10, height=1, command=self.get_user_credentials) \
            .place(relx=0.5, rely=0.9, anchor=CENTER)

    def get_user_credentials(self):
        print(self.login.get())
        print(self.password.get())
        self.check_json(filename='data.json')
        self.login_entry.delete(0, END)
        self.password_entry.delete(0, END)
        # self.destroy()

    def check_json(self, filename):
        path = 'OneSoft/Lesson_20_1/lesson20/auth_new/json_storage'
        filename = 'data'
        if check_cred_from_json(path, filename, self.login.get(), self.password.get()):
            print('successful log in')
        else:
            print('something wrong')

        # with open("data.json", "r") as f:
        #     data = f.read()
        #     json_data = json.load(data)
        #     return json_data
        # f.close()
        # if self.login.get() in a:
        #     if generate_password_hash(self.password.get()) == a[self.login.get()]:
        #         messagebox.showinfo("Вход выполнен", "Добро пожаловать!")
        #     else:
        #         messagebox.showerror("Ошибка", "Неверные данные. Повторите снова.")
        # else:
        #     messagebox.showerror("Ошибка", "Неверный логин")


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

    def create_user_interface(self):
        validate_password = (self.register(self.check_is_password_strong), '%P')
        invalid_password = (self.register(self.on_invalid),)

        Label(self, text='Please enter data bellow to registration'). \
            place(relx=0.5, rely=0.05, anchor=CENTER)

        Label(self, text='Username *') \
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

        Button(self, text='Registration', width=10, height=1, command=self.get_user_credentials) \
            .place(relx=0.5, rely=0.9, anchor=CENTER)

    def change_show_password(self):
        state = '' if self.show_pass.get() else '*'
        self.password_entry.config(show=state)
        self.password_repeat_entry.config(show=state)

    def get_user_credentials(self):
        print(self.login.get())
        password_hash = generate_password_hash(self.password.get())
        # check if pass hash and password itself are the same
        print(check_password_hash(password_hash, self.password.get()))
        # passwords do not match
        print(self.password.get() == self.password_repeat.get())
        print(generate_password_hash(self.password_repeat.get()))

        if (self.password.get() == self.password_repeat.get()):
            self.safe_to_json()
        else:
            ValueError('Passwords do not match')

        self.login_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.password_repeat_entry.delete(0, END)

        # self.destroy()

    def safe_to_json(self):
        path = 'OneSoft/Lesson_20_1/lesson20/auth_new/json_storage'
        filename = 'data'
        create_json_file(path, filename)
        add_cred_to_json(path, filename, self.login.get(), self.password.get())


def create_json_file(path, filename):
    """
    path - путь до файла
    filename - имя файла
    что делает функция?
    Проверяет есть ли такой файл в папке назначения?
    Если да - пишет "файл уже есть"
    Если нет - создаёт пустой JSON файл с именем filename.json
    """
    full_path = path + '/' + filename + '.json'
    if ~(os.path.isfile(full_path)):
        json_content = {}
        save_to_json_file(json_content, full_path)
    pass


def add_cred_to_json(path, filename, login, passw):
    """
    check if this login already in keys?
    If yes - return error: this user already exists in a system
    else - add user and password to credentials Login - key, password - value
    """
    full_path = path + '/' + filename + '.json'
    data = load_json_from_file(full_path)
    if login in data.keys():
        raise ValueError('this login already exists, try another one')
    else:
        data[login] = passw
        save_to_json_file(data, full_path)


def check_cred_from_json(path, filename, login, passw):
    """
    check if this login already in keys?
    If yes - return error: this user already exists in a system
    else
        check if pass correct
        if ok - login
        else - error (wrong passw)
    """
    full_path = path + '/' + filename + '.json'
    data = load_json_from_file(full_path)
    if login in data.keys():
        if passw == data[login]:
            return True
        else:
            raise ValueError('Wrong password')
    else:
        raise ValueError('no such login')


def object_to_json_string(response_dict):
    return json.dumps(response_dict, indent=2, sort_keys=False)


def json_string_to_object(json_text):
    return json.loads(json_text)


def load_json_from_file(path):
    if os.path.isfile(path):
        with open(path, 'r') as f:
            content = f.read()
            json_root_object = json_string_to_object(content)
            return json_root_object
    else:
        raise ValueError(f'cannot load {path} file')


def save_to_json_file(object, path):
    with open(path, 'w') as f:
        json = object_to_json_string(object)
        f.write(json)
