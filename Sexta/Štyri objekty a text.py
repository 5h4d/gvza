import random as rng
import tkinter as tk
canvas = tk.Canvas(height=1000, width=1000)
canvas.pack()


for i in range(1, 5):
    x = rng.randrange(10, 400)
    y = rng.randrange(10, 400)
    w = rng.randrange(5, 70)
    h = rng.randrange(5, 70)
    thicc = rng.randrange(1, 10)
    clr = rng.choice(('green', 'blue', 'red', 'magenta', 'yellow'))    
    canvas.create_oval(x, y, x+w, y+h, fill=clr, width=thicc)

x = rng.randrange(10, 400)
y = rng.randrange(10, 400)
w = rng.randrange(5, 70)
clr = rng.choice(('green', 'blue', 'red', 'magenta', 'yellow'))
canvas.create_text(x, y, text='Æ?, ⸘MEHMET‽', font='arial 20')
