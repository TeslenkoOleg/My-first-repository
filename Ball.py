import tkinter
import random

WIDTH = 600
HEIGHT = 450
BG_COLOR = 'white'
ZERO = 0
COLORS = ['yellow', 'aqua', 'brown', 'black', 'pink', 'gold', 'red']


#Balls class
class Balls():
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x=x
        self.y=y
        self.r=r
        self.color=color
        self.dx=dx
        self.dy=dy


    def draw(self):
        canvas.create_oval(self.x - self.r, self.y-self.r,self.x+self.r,
                           self.y+self.r, fill=self.color, outline=self.color if self.color != 'red' else 'black')

    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r,
                           self.y + self.r, fill=BG_COLOR, outline=BG_COLOR)

    def is_collision(self, ball):
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a * a + b * b) ** 0.5 <= self.r + ball.r

    def move(self):
        #otskok
        if (self.x+self.r+self.dx >=WIDTH) or (self.x-self.r+self.dx <=ZERO):
            self.dx = -self.dx
        if (self.y+self.r+self.dy >=HEIGHT) or (self.y-self.r+self.dy <=ZERO):
            self.dy = -self.dy

        for ball in balls:
            if self.is_collision(ball):
                if ball.color != 'red':
                    ball.hide()
                    balls.remove(ball)
                    self.dx = -self.dx
                    self.dy = -self.dy
                else:
                    self.dx=self.dy=0
                    canvas.create_text(WIDTH/2, HEIGHT/2, text='YOU LOST', fill='red', font='25')
        self.hide()
        self.x += self.dx
        self.y +=self.dy
        self.draw()



#mouse event
def mouse_click(event):
    global main_ball
    if event.num==1:
        if 'main_ball' not in globals():
           main_ball=Balls(event.x, event.y, 30, 'blue',1,1)
           main_ball.draw()
        else:# turn left
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
    elif event.num == 3: # turn right
        if main_ball.dx * main_ball.dy > 0:
            main_ball.dx = -main_ball.dx
        else:
            main_ball.dy = -main_ball.dy



    else:
        main_ball.hide()

#main cicle game
def main():

    if 'main_ball' in globals():
        main_ball.move()
    if len(balls) - num_of_bad_balls ==0:
        canvas.create_text(WIDTH/2, HEIGHT/2, text='You won!', fill='blue', font='20')
        main_ball.dx=main_ball.dy=0

    root.after(2, main)

#create list of balls
def list_balls(number):
    list = []
    while len(list) < number:
        balls = Balls(random.choice(range(0, WIDTH)), random.choice(range(0, HEIGHT)),
                      random.choice(range(15, 30)), random.choice(COLORS))
        list.append(balls)
        balls.draw()

    return list

def count_red_balls(list_balls):
    result=0
    for ball in balls:
        if ball.color == 'red':
            result +=1
    return result





root= tkinter.Tk()
root.title("Balls")
canvas = tkinter.Canvas(width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()

canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click)
canvas.bind('<Button-3>', mouse_click)
if 'main_ball' in globals():
    del main_ball

balls=list_balls(6)
num_of_bad_balls = count_red_balls(balls)
main()

root.mainloop()