from tkinter import Canvas
from random import randint as rng

c = Canvas(width=360, height=260)
c.pack()

for i in range(10000):
    x = rng(10, 350)
    y = rng(10, 250)
    if y < 130:
        col = "blue" if x < y else "white"
    else:
        col = "blue" if 260-x > y else "red"
    c.create_oval(x-5, y-5, x+5, y+5, outline="", fill=col)

c.mainloop()
