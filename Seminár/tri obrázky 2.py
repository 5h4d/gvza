from tkinter import Canvas
from tkinter import Toplevel
from random import randint as rng

"""HVIEZDY"""

c=Canvas(height=500, width=500, bg='blue')
c.pack()

for i in range(500):
    x=rng(20,480)
    y=rng(20,480)
    c.create_polygon(x-10,y+25,x,y,x+10,y+25,x-15,y+10,x+15,y+10,fill='gold')

"""ŠTVORCE"""

c=Canvas(Toplevel(),height=500,width=500)
c.pack()

x=int(input("x: "))
y=int(input("y: "))
a1=int(input("a1: "))
a2=int(input("a2: "))

c.create_rectangle(x,y,x+a1,y+a1,fill='red')
c.create_rectangle(x+(a1-a2)/2,y+(a1-a2)/2,x+(a1-a2)/2+a2,y+(a1-a2)/2+a2,fill='slateblue')
c.create_text(x-5,y-5,text="A")
c.create_text(x+a1+5,y-5,text="B")
c.create_text(x+a1+4,y+a1+4,text="C")
c.create_text(x-4,y+a1+4,text="D")
c.create_text(x+a1+13,y+a1/2,text=a1)
c.create_text(x+a1/2,y+(a1-a2)/2+a2+5,text=a2)

"""VIAC ŠTVORCE"""

c=Canvas(Toplevel(),height=500,width=500)
c.pack()
print()
print()

n=int(input("n: "))
bl=[f*3+3 for f in range(n)]
wh=[f*3+2 for f in range(n)]
for i in range(n):
    if i in bl or i == 0:
        cl="blue"
    elif i in wh:
        cl="white"
    else:
        cl="red"
    c.create_rectangle(245-n*5+i*5,245-n*5+i*5,255+n*5-i*5,255+n*5-i*5,fill=cl)
