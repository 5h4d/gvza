import tkinter
import random
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()
x = random.randrange(440)
y = random.randrange(440)
canvas.create_line(x, y, x+50, y, width=5)
print('Prvý bod čiary je:', x, y)
