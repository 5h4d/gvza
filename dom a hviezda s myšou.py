import tkinter as tk
import random as rnd
canvas = tk.Canvas()
canvas.pack()

def dom(xy):
    x = xy.x
    y = xy.y
    canvas.create_line(x, y, x, y+10, x+10, y+10, x+10, y, x, y, x+5, y-10, x+10, y, fill=rnd.choice(('red', 'green', 'blue', 'brown')))

def tjhvezdazadubnie(xy):
    x = xy.x
    y = xy.y
    canvas.create_line(x, y, x+5, y-15, x+10, y, x-3, y-8, x+12, y-8, x, y, fill=rnd.choice(('red', 'green', 'blue', 'brown')))

canvas.bind('<Button-3>', dom)
canvas.bind('<Button-1>', tjhvezdazadubnie)
