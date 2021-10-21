import tkinter
import random
import math
w = random.randint(1, 15)
x = random.randrange(350)
y = random.randrange(350)
a = x+random.randrange(350)
b = y+random.randrange(350)
canvas = tkinter.Canvas(height=700, width=700)
canvas.pack()
canvas.create_line(x, y, a, b, width=w)
print('Dĺžka =', math.sqrt((a-x)*(a-x)+(b-y)*(b-y)))
print('Hrúbka =', w)
