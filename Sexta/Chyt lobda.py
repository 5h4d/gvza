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
    c.create_oval(x-5,0,x+5,10,fill='red',tags='bda')
def paddle(xx):
    c.create_rectangle(xx-15,370,xx+15,375,fill='blue',tags='shalla')
def ඞඞ():
    global bruh
    c.delete('sk')
    c.create_text(680,20,text=bruh,tags='sk')

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
            ඞඞ()
            f=0
            c.after(500,kruhek)
        else:
            bruh-=3
            f=0
            ඞඞ()
            if bruh>=0:
                kruhek()
            else:
                c.delete('all')
                c.create_text(350,200,text='L',font='arial 50')
                
    else:
        c.after(5,mvmnt)
kruhek()
def agin(a):
    c.delete('all')
    f=0
    xx=0
    bruh=int(0)
    kruhek()
c.bind('<Motion>',kurzir)
c.bind_all('r',agin)
