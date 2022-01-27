import tkinter as tk
import random
c=tk.Canvas(height=400, width=700)
c.pack()

bruh=int(0)
x=random.randrange(700)
xx=0
f=0
def ඞ():
    global x
    lobda=c.create_oval(x-5,0,x+5,10,fill='red',tags='bda')
def paddle(xx):
    c.create_rectangle(xx-15,370,xx+15,375,fill='blue',tags='shalla')
skoe=c.create_text(680,20,text=bruh)

def kruhek():
    global x
    x=random.randrange(700)
    c.delete('bda')
    ඞ()
    mvmnt()
def kurzir(buhr):
    global xx
    xx=buhr.x
    c.delete('shalla')
    paddle(xx)
def mvmnt():
    global x, padlo_x, xx, f, bruh
    c.move('bda',0,10)
    f+=1
    if f==37:
        if xx-15<x<xx+15:
            bruh+=1
            skoe
            f=0
            c.after(500,kruhek)
        else:
            bruh-=5
            c.create_text(350,200,text='L',font='arial 40',tags='yis')
            c.after(100, c.delete('yis'))
            f=0
            skoe
            kruhek()
    else:
        c.after(10,mvmnt)
mvmnt()
c.bind('<Motion>',kurzir)
