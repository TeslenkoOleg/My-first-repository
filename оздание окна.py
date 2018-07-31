from tkinter import *
import math
root = Tk()

root.title("Create window")
root.geometry('1020x620')

canvas = Canvas(root, width = 1020, height = 620, bg = 'Blue')

#Create vertical line
for y in range(21):
    k = y * 50
    canvas.create_line(10+k, 10, 10+k, 610, fill='green')

#Create vertical line
for x in range(21):
    k = x*50
    canvas.create_line(10, 10+k, 1010, 10+k, fill='green')

#Create x koord
canvas.create_line(10, 620/2, 1010, 620/2, width='2', fill='white', arrow=LAST)
#Create y koord
canvas.create_line(10, 10, 10, 610, width='3', fill='white', arrow=FIRST)

w=0.0209 #циклическая частота
phi=10   #смещение графика по Х
A=200    #амплитуда
dy=310   #смещение по У

xy=[]

for x in range(1000):
    y=math.sin(x*w)
    xy.append(x+phi)
    xy.append(y*A+dy)

sin_line = canvas.create_line(xy, width='2', fill='red')

canvas.pack()

root.mainloop()