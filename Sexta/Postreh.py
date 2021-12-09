import tkinter as tk
import random
c=tk.Canvas(height=700, width=700)
rng=random.randrange
c.pack()

c.create_text(350, 10, text="wespe!")
score=0
vitu=0
c.create_text(660,10,text=score,tags='sc')
def burh():
    global x,y,vitu
    c.delete('crcl')
    c.create_line(x+10,y+10,x+40,y+40,fill='red',width=3,tags='geki')
    c.create_line(x+40,y+10,x+10,y+40,fill='red',width=3,tags='geki')
def ba():
    global x,y,score,vitu
    x=rng(0,650)
    y=rng(10,650)
    c.delete('crcl')
    c.create_oval(x,y,x+50,y+50,fill='lightblue',outline='blue',width=3,tags='crcl')
    c.after(1000,ba)
    c.delete('geki')
def check(xy):
    global x,y,score
    lock=1
    if xy.x>x and xy.x<x+50 and xy.y>y and xy.y<y+50:
        vitu=1
        c.delete('crcl')
        c.create_text(x+25,y+25,text=random.choice(('300','激')),fill='blue',font='arial 10',tags='geki')
        c.delete('sc')
        score+=300
        c.create_text(660,10,text=score,tags='sc')
    else:
        burh()
ba()
c.bind('<Button-1>',check)
