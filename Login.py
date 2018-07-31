from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("300x500")
root.title("Вход в систему")
#canvas = Canvas(root)


def registration():
    text1 = Label(text="Для входа в систему - зарегистрируйтесь!")
    text_login = Label(text="Введите логин:")
    registr_login = Entry()
    text_password1 = Label(text="Введите пароль:")
    registr_password1 = Entry()
    text_password2 = Label(text="Повторите пароль:")
    regisrt_password2 = Entry(show="*")
    button = Button(text="Зарегистрироваться!", command = lambda: save())
    text1.pack()
    text_login.pack()
    registr_login.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    regisrt_password2.pack()
    button.pack()

    def save():
        login_pass_save = {}
        login_pass_save[registr_login.get()]=registr_password1.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()

def login():


    text2 = Label(text = "Вход в систему!")
    text_login = Label(text = "Введите логин:")
    enter_login = Entry()
    text_password = Label(text = "Введите пароль:")
    enter_password = Entry()
    button_enter = Button(text = "Войти!", command = lambda: log_pass())
    text2.pack()
    text_login.pack()
    enter_login.pack()
    text_password.pack()
    enter_password.pack()
    button_enter.pack()

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() ==a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен!", "У вас есть новые сообщения")
            else:
                messagebox.showerror("Ошибка", "Вы ввели неверный пароль!")
        else:
            messagebox.showerror("Ошибка!", "Вы ввели неверный логин")

registration()
#login()
root.mainloop()