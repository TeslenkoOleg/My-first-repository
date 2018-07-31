from tkinter import *
import random

WIDTH=900
HEIGHT=300
BALL_RADIUS=20
BALL_X_CHANGE=20
BALL_Y_CHANGE=0
PLAYER_1=0
PLAYER_2=0

PAD_W=10
PAD_H=100

root = Tk()
root.title('Ping-pong')
c=Canvas(root, width=WIDTH, height=HEIGHT, background='blue')
c.pack()
#Левая граница поля
c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill='white')
#Правая граница поля
c.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill='white')
#Разделитель игрового поля
c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill='white')
#ball
BALL=c.create_oval(WIDTH/2-BALL_RADIUS, HEIGHT/2-BALL_RADIUS, WIDTH/2+BALL_RADIUS, HEIGHT/2+BALL_RADIUS, fill='red')
#ракетки
#левая ракетка
LEFT_PAD=c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill='orange')
#правая ракетка
RIGHT_PAD = c.create_line(WIDTH-(PAD_W/2), 0, WIDTH-(PAD_W/2), PAD_H, width=PAD_W, fill='orange')

text_pl1 = c.create_text(35, 20, text=PLAYER_1, font='Helvetica 20', fill='white')
text_pl2 = c.create_text(850, 20, text=PLAYER_2, font='Helvetica 20', fill='white')

#Скорость ракеток
PAD_SPEED=20
LEFT_PAD_SPEED=0
RIGHT_PAD_SPEED=0
#Увеличение скорости мяча с каждым ударов
BALL_SPEED_UP=1.00
#Максимальная скорость мяча
BALL_MAX_SPEED=30
#Начальная скорость по горизонтали
BALL_X_SPEED=10
#Начальная скорость по вертикали
BALL_Y_SPEED=10
#Растояние от правого края
right_line_distance=WIDTH-PAD_W
INITIAL_SPEED=20

#Cчет
def score(player):
    global PLAYER_1,PLAYER_2
    if player == 'right':
        PLAYER_1 += 1
        c.itemconfig(text_pl1, text=PLAYER_1)
    else:
        PLAYER_2 += 1
        c.itemconfig(text_pl2, text=PLAYER_2)

#Respawn
def spawn():
    global BALL_X_SPEED, INITIAL_SPEED
    c.coords(BALL, WIDTH / 2 - BALL_RADIUS,
             HEIGHT / 2 - BALL_RADIUS,
             WIDTH / 2 + BALL_RADIUS,
             HEIGHT / 2 + BALL_RADIUS)
    BALL_X_SPEED = -(BALL_X_SPEED * -INITIAL_SPEED)/abs(BALL_X_SPEED)


#Функция отскока мяча
#def bounce(action):
   # global BALL_X_SPEED, BALL_Y_SPEED
    #if action == 'strike':
       # BALL_Y_SPEED = random.randrange(-10, 10)
       # if abs(BALL_X_SPEED)<BALL_MAX_SPEED:
      #      BALL_X_SPEED *= -BALL_SPEED_UP
      #  else:
      #      BALL_X_SPEED = -BALL_X_SPEED
    #else:
      #  BALL_Y_SPEED = -BALL_Y_SPEED
def bounce():
    ball_left, ball_right, ball_top, ball_bot = c.coords(BALL)
    if ball_right == right_line_distance:
        B


#функция движения ракеток
def move_pads():
    PADS={LEFT_PAD:LEFT_PAD_SPEED, RIGHT_PAD:RIGHT_PAD_SPEED}
    for pad in PADS:
        c.move(pad, 0, PADS[pad])
        if c.coords(pad)[1]<0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad) [3]>HEIGHT:
            c.move(pad, 0, HEIGHT-c.coords(pad)[3])



#функция движения мяча
def move_ball():
    global RIGHT_PAD, LEFT_PAD
    ball_left, ball_right, ball_top, ball_bot = c.coords(BALL)
    ball_center=(ball_bot+ball_top)/2
    #Вертикальный отскок
    if ball_right+BALL_X_SPEED < right_line_distance and ball_left+BALL_X_SPEED > PAD_W:
        c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
    elif ball_right == right_line_distance or ball_left == PAD_W:
        bounce('strike')
        score('left')
        spawn()

    else:
        if ball_right>WIDTH/2:
            c.move(BALL, right_line_distance-ball_right, BALL_Y_SPEED)
        else:
            c.move(BALL, -ball_left+PAD_W, BALL_Y_SPEED)

    if ball_top+BALL_Y_SPEED<0 or ball_bot+BALL_Y_SPEED>HEIGHT:
        bounce('ricochet')
bounce('strike')

def main():
    move_ball()
    move_pads()
    #Вызываем саму себя
    root.after(30, main)

#Фокус на канвас(реакция на клавиши)
c.focus_set()

#Обработка нажатий
def handler(event):
    global RIGHT_PAD_SPEED, LEFT_PAD_SPEED
    if event.keysym == 'w':
        LEFT_PAD_SPEED=-PAD_SPEED
    elif event.keysym=='s':
        LEFT_PAD_SPEED=PAD_SPEED
    elif event.keysym=='Up':
        RIGHT_PAD_SPEED=-PAD_SPEED
    elif event.keysym=='Down':
        RIGHT_PAD_SPEED=PAD_SPEED
#Привязка к канвасу
c.bind('<KeyPress>', handler)

def stop_pads(event):
    global RIGHT_PAD_SPEED, LEFT_PAD_SPEED
    if event.keysym in 'ws':
        LEFT_PAD_SPEED=0
    elif event.keysym in ('Up','Down'):
        RIGHT_PAD_SPEED=0

c.bind('<KeyRelease>', stop_pads)

main()








root.mainloop()