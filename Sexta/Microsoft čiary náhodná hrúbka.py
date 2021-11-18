import tkinter as tk
import random
c=tk.Canvas(height=400, width=400)
c.pack()

def cz(xy):
    x=xy.x
    y=xy.y
    if x<200 and y<200:
        c.create_line(200, 200, x, y, fill='red', width=random.randint(0,9))
    if x<200 and y>200:
        c.create_line(200, 200, x, y, fill='blue', width=random.randint(0,9))
    if x>200 and y<200:
        c.create_line(200,200,x,y,fill='green', width=random.randint(0,9))
    if x>200 and y>200:
        c.create_line(200,200,x,y,fill='yellow',width=random.randint(0,9))

c.bind('<Button-1>',cz)
