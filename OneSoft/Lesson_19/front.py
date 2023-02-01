# from tkinter import *
# from typing import Union
# from abc import ABCMeta, abstractmethod
#
#
# class WindowInterface(metaclass=ABCMeta):
#     @abstractmethod
#     def create_user_interface(self):
#         pass
#
#
# class WindowEntryInterface(metaclass=ABCMeta):
#     @abstractmethod
#     def get_user_credentials(self):
#         pass
#
#
# class MainWindow(Tk, WindowInterface):
#     def __init__(self):
#         super().__init__()
#         self.geometry('300x250')
#         self.resizable(False, False)
#         self.title('Account manager')
#
#         self.create_user_interface()
#
#     def create_user_interface(self):
#         Label(self, text='Select your choice', bg='blue', fg='white', width='300', height='2', font=('Calibri', 13)).\
#             place(relx=0.5, rely=0.1, anchor=CENTER)
#         Button(self, text='Login', height='2', width='30', command=self.call_login_window)\
#             .place(relx=0.5, rely=0.4, anchor=CENTER)
#         Button(self, text='Register', height='2', width='30', command=self.call_register_window)\
#             .place(relx=0.5, rely=0.7, anchor=CENTER)
#
#     def call_login_window(self):
#         LoginWindow(self)
#
#     def call_register_window(self):
#         RegisterWindow(self)
#
#
# class LoginWindow(Toplevel, WindowInterface, WindowEntryInterface):
#     def __init__(self, root_window):
#         super().__init__(master=root_window)
#         self.title('Login')
#         self.geometry('300x250')
#         self.resizable(False, False)
#
#         self.login = StringVar()
#         self.password = StringVar()
#
#         self.login_entry: Union[Entry, None] = None
#         self.password_entry: Union[Entry, None] = None
#
#         self.create_user_interface()
#
#     def create_user_interface(self):
#         Label(self, text='Please enter details bellow to login').\
#             place(relx=0.5, rely=0.1, anchor=CENTER)
#
#         Label(self, text='Username *')\
#             .place(relx=0.5, rely=0.3, anchor=CENTER)
#         self.login_entry = Entry(self, textvariable=self.login)
#         self.login_entry.place(relx=0.5, rely=0.4, anchor=CENTER)
#
#         Label(self, text='Password *') \
#             .place(relx=0.5, rely=0.6, anchor=CENTER)
#         self.password_entry = Entry(self, textvariable=self.password, show='*')
#         self.password_entry.place(relx=0.5, rely=0.7, anchor=CENTER)
#
#         Button(self, text='Login', width=10, height=1, command=self.get_user_credentials)\
#             .place(relx=0.5, rely=0.9, anchor=CENTER)
#
#     def get_user_credentials(self):
#         print(self.login.get())
#         print(self.password.get())
#         self.login_entry.delete(0, END)
#         self.password_entry.delete(0, END)
#         # self.destroy()
#
#
# class RegisterWindow(Toplevel, WindowInterface, WindowEntryInterface):
#     def __init__(self, root_window):
#         super().__init__(master=root_window)
#         self.title('Register')
#         self.geometry('300x400')
#         self.resizable(False, False)
#
#         self.login = StringVar()
#         self.password = StringVar()
#         self.password_repeat = StringVar()
#
#         self.login_entry: Union[Entry, None] = None
#         self.password_entry: Union[Entry, None] = None
#         self.password_repeat_entry: Union[Entry, None] = None
#
#         self.create_user_interface()
#
#     def create_user_interface(self):
#         Label(self, text='Please enter data bellow to registration').\
#             place(relx=0.5, rely=0.1, anchor=CENTER)
#
#         Label(self, text='Username *')\
#             .place(relx=0.5, rely=0.2, anchor=CENTER)
#         self.login_entry = Entry(self, textvariable=self.login)
#         self.login_entry.place(relx=0.5, rely=0.3, anchor=CENTER)
#
#         Label(self, text='Password *') \
#             .place(relx=0.5, rely=0.4, anchor=CENTER)
#         self.password_entry = Entry(self, textvariable=self.password, show='*')
#         self.password_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
#
#         Label(self, text='Repeat password *') \
#             .place(relx=0.5, rely=0.6, anchor=CENTER)
#         self.password_repeat_entry = Entry(self, textvariable=self.password_repeat, show='*')
#         self.password_repeat_entry.place(relx=0.5, rely=0.7, anchor=CENTER)
#
#         Button(self, text='Registration', width=10, height=1, command=self.get_user_credentials)\
#             .place(relx=0.5, rely=0.8, anchor=CENTER)
#
#     def get_user_credentials(self):
#         print(self.login.get())
#         print(self.password.get())
#         print(self.password_repeat.get())
#
#         self.login_entry.delete(0, END)
#         self.password_entry.delete(0, END)
#         self.password_repeat_entry.delete(0, END)
#
#         # self.destroy()
#
#
# main_window = MainWindow()
# main_window.mainloop()
#

# print(set(('a', 'b', 'c')).intersection(set(('c', 'd', 'e'))))

