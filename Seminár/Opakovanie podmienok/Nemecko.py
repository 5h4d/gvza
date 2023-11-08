from tkinter import Canvas
from random import randint as rng

c = Canvas(width=360, height=260)
c.pack()

for i in range(10000):
    x = rng(10, 350)
    y = rng(10, 250)
    c.create_oval(
        x - 5,
        y - 5,
        x + 5,
        y + 5,
        outline="",
        fill="black" if y < 90 else "red" if y < 170 else "gold",
    )

c.mainloop()
