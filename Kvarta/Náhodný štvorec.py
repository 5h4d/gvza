import tkinter
import random
x =  random.randint(30, 700)
canvas = tkinter.Canvas(height=x+10, width=x+10)
canvas.pack()
canvas.create_rectangle(10, 10, x, x, width=5)
canvas.create_text((x+10)/2, (x+10)/2, text=x)
