import tkinter as tk
import random as rnd

canvas = tk.Canvas(bg='lightgreen', width=500, height=500)
canvas.pack()

#kvetok
    
for i in range(1, 6):
    x = rnd.randrange(1, 440)
    y = rnd.randrange(1, 440)
    clr = rnd.choice(('red', 'green', 'blue', 'yellow', 'purple', 'violet'))
    canvas.create_oval(x, y, x+30, y+30, fill='white') #lavohorny
    canvas.create_oval(x+30, y, x+60, y+30, fill='white') #pravohorny
    canvas.create_oval(x, y+30, x+30, y+60, fill='white') #lavodolny
    canvas.create_oval(x+30, y+30, x+60, y+60, fill='white') #pravodolny
    canvas.create_oval(x+15, y+15, x+45, y+45, fill=clr)#stred
