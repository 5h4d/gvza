import tkinter as tk
import random as rnd
cnv = tk.Canvas(height=700, width=700)
cnv.pack()

#prep
x=rnd.randrange(51, 649)
y=rnd.randrange(250, 700)

#veci
yy=y-105
xx=x-30
for n in range(0,3):
    foo=rnd.choice(('magenta', 'MediumOrchid2', 'orange2', 'SlateBlue2', 'chocolate2', 'mint cream', 'IndianRed1', 'salmon'))
    cnv.create_oval(xx, yy, xx+60, yy-60, outline=foo, fill=foo)
    yy-=45

#kornut
cnv.create_line(x, y, x-20, y-95, x+20, y-95, x, y, width=34, fill='khaki2')
