from random import randrange
from math import sqrt
import tkinter as tk
c=tk.Canvas(height=300,width=500)
c.pack()

v=n=d=x=0
y=randrange(270)
while x<500:
    xx=x+randrange(100)
    yy=randrange(270)
    c.create_line(x,y,xx,yy)
    if yy>y:
        n+=yy-y
        d+=sqrt(((xx-x)**2)+((yy-y)**2))
    else:
        v+=y-yy
        d+=sqrt(((xx-x)**2)+((y-yy)**2))
    x=xx
    y=yy
c.create_text(50,270,text='Stúpanie: '+str(v)+'m')
c.create_text(48,280,text='Klesanie: '+str(n)+'m')
c.create_text(74,290,text='Prejdená cesta: '+str(d//1)+'m')
