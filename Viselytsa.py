from tkinter import *
import random

root = Tk()
root.title("Висилеца")

canvas = Canvas(root, width = 600, height = 600)
canvas.pack ()


def but():
    y = 0
    while y <600:
        x = 0
        while x < 600:
            canvas.create_rectangle(x, y, x+30, y+30, fill = 'white', outline = 'blue')
            x = x+30
        y = y+30



faq = """                            Привет, Игрок! 

Правила игры: 
Смотрели "Поле-Чудес"? 
Здесь тоже самое - угадай все буквы в слове и выиграй!!!
Или будешь П О В Е Ш А Н!!!"""
canvas.create_text(300, 230, text = faq, fill = 'red', font=('Helvetica','10'))

btn1 = Button(root, text = 'Начать', width = 10, height = 2, command=lambda :arr())
btn1.place(x = 280, y = 500)
btn1["bg"] = 'red'

words = ["Висилеца", "смартфон", "мегагерц", "креветка", "микрофон", "маргарин", "страница"]

def arr():
    but()
    word = random.choice(words)
    wor = word[1:-1]
    wo = []
    for i in wor:
        wo.append(i)
    a0 = canvas.create_text(345, 135, text = word [0], fill = 'orange', font=("Helvetica","25"))
    a1 = canvas.create_text(375, 130, text = "_", fill = 'orange', font =("Helvetica","25"))
    a2 = canvas.create_text(405, 130, text = "_", fill = 'orange', font =("Helvetica","25"))
    a3 = canvas.create_text(435, 130, text = "_", fill = 'orange', font =("Helvetica","25"))
    a4 = canvas.create_text(465, 130, text="_", fill='orange', font=("Helvetica","25"))
    a5 = canvas.create_text(495, 130, text="_", fill='orange', font=("Helvetica","25"))
    a6 = canvas.create_text(525, 130, text="_", fill='orange', font=("Helvetica","25"))
    a6 = canvas.create_text(555, 135, text=word[-1], fill='orange', font=("Helvetica","25"))
    list1 = [1, 2, 3, 4, 5, 6]
    alfabet = "абвгдежзклмнопрстчцхфийяюьщш"
    er = []
    win = []
    if word == "Висилеца":
        canvas.create_text(390, 170, text="Подсказка: это настольная игра!")
    elif word == "смартфон":
        canvas.create_text(390, 170, text="Подсказка: это штука из мира гаджетов!")
    elif word == "мегагерц":
        canvas.create_text(390, 170, text="Подсказка: еденица измерения частоты!")
    elif word == "креветка":
        canvas.create_text(390, 170, text="Подсказка: это морепродукт!")
    elif word == "микрофон":
        canvas.create_text(390, 170, text="Подсказка: это используется в музыке!")
    elif word == "маргарин":
        canvas.create_text(390, 170, text="Подсказка: это используется в кулинарии!")
    elif word == "страница":
        canvas.create_text(390, 170, text="Подсказка: это очень легкое слово!)))")
    else:
        canvas.create_text(390, 170, text="Подсказка: else")

    def a(v):
        ind_alf = alfabet.index(v)
        key = alfabet[ind_alf]

        if v in wo:

            ind = wo.index(v)
            b2 = list1[ind]
            wo[ind] = '1'

            def kord():
                if b2 == 1:
                    x1, y1 = 375, 135
                if b2 ==2:
                    x1, y1 =405, 135
                if b2 ==3:
                    x1, y1 =435, 135
                if b2 == 4:
                    x1, y1 = 465, 135
                if b2 ==5:
                    x1, y1 =495, 135
                if b2 ==6:
                    x1, y1 =525, 135
                return x1, y1

            x1, y1 = kord()
            win.append(v)
            a2 = canvas.create_text(x1, y1, text=wor[ind], fill='orange', font=('Helvetica','23'))
            btn[key]["bg"] = 'green'

            if not v in wo:
                btn[key]["state"] = "disabled"

            if v in wo:
                win.append(v)
                ind2 =wo.index(v)
                b2 = list1[ind2]
                x1, y1 = kord()
                canvas.create_text(x1, y1, text=wo[ind2], fill='orange', font=('Helvetica', '23'))
            if len(win) ==6:
                canvas.create_text(280, 80, text = 'You are winner!', fill='red', font=('Helvetica','30'))
                for i in alfabet:
                    btn[i]["state"]="disabled"

        else:
            er.append(v)
            btn[key]["bg"]=["red"]
            btn[key]["state"]="disabled"
            if len(er)==1:
                head()
            elif len(er)==2:
                body()
            elif len(er)==3:
                hands()
            elif len(er)==4:
                legs()
            elif len(er)==5:
                first_v()
            elif len(er) ==6:
                second_v()
                canvas.create_text(280,80, text='You are loser', fill='red', font=('Helvetica','30'))
                for i in alfabet:
                    btn[i]["state"]='disabled'

    btn = {}

    def gen(u, x, y):

        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))
        btn[u].place(x=str(x), y=str(y))
    x=330
    y=210
    for i in alfabet[0:8]:
        gen(i, x, y)
        x=x+33
    x=330
    y=240
    for i in alfabet[8:16]:
        gen(i, x, y)
        x=x+33
    x=330
    y=270
    for i in alfabet[16:24]:
        gen(i, x, y)
        x+=33
    x=330
    y=300
    for i in alfabet[24:]:
        gen(i,x,y)
        x+=33


def head():
    canvas.create_oval(100, 100, 145, 150, width='3')
    root.update()


def body():
    canvas.create_oval(110, 150, 135, 250, width='3')
    root.update()


def hands():
    canvas.create_line(110, 170, 75, 240, width='3')
    canvas.create_line(135, 170, 170, 240, width='3')
    root.update()


def legs():
    canvas.create_line(115, 245, 75, 330, width='4')
    canvas.create_line(130, 245, 165, 330, width='4')
    root.update()


def first_v():
    canvas.create_line(20, 30, 20, 350, width='20')
    canvas.create_line(20, 50, 145, 30, width='20')
    root.update()


def second_v():
    canvas.create_line(123, 30, 123, 100, width='3')
    root.update()











root.mainloop()