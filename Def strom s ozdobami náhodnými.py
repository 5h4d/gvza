import tkinter as tk
import random as rnd
canvas = tk.Canvas(width=100, height=260)
canvas.pack()

def trojuholnik():
    canvas.create_line(20, y, 50, y-30, 80, y, 20, y, fill='green', width=30)

y=50
for i in range(1, 5):
    trojuholnik()
    a = rnd.randrange(20, 80)
    b = rnd.randrange(y-30, y)
    c = rnd.randrange(20, 80)
    d = rnd.randrange(y-30, y)
    clra=rnd.choice(('red', 'lightgreen', 'blue', 'yellow', 'orange', 'purple'))
    clrb=rnd.choice(('red', 'lightgreen', 'blue', 'yellow', 'orange', 'purple'))
    canvas.create_oval(a, b, a+5, b+5, fill=clra)
    canvas.create_oval(c, d , c+5, d+5, fill=clrb)
    y = y+45

canvas.create_rectangle(40, 200, 60, 240, fill='brown', outline='brown')
