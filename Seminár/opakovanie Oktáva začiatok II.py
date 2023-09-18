import tkinter as tk
from random import choice as pick
from random import randrange as rng
from time import sleep
c=tk.Canvas(width=500,height=500,bg='white')
c.pack()


farbi=['red','yellow','blue','magenta','green']
def lodenky():
    c.create_rectangle(0,250,500,500,fill='lightblue',outline='lightblue')
    c.bind('<Button-1>',balonka)
def balonka(xy):
    x=xy.x
    y=xy.y
    if y>250:
        c.create_rectangle(x-15,y,x+15,y+10,fill='brown',outline='brown')
        c.create_rectangle(x-7,y,x-12,y-40,fill='brown',outline='brown')
        c.create_polygon(x-7,y-40,x-7,y-20,x+20,y-30,fill=pick((farbi)),outline='black')
    else:
        c.create_oval(x-30,y-30,x+30,y+30,fill=pick((farbi)),outline='black')
        c.create_polygon(x-13,y+38,x+13,y+38,x+7,y+53,x-7,y+53,fill='brown',outline='brown')
        a=x-40
        while a<x+30:
            a+=10
            c.create_line(a,y,x,y+38,fill='black',width=3)

##########################################################################################
#####################################  ŠETRIČ  ###########################################
##########################################################################################

def res(xy):
    global a,angle,stop
    c.delete('setritka')
    a=3
    angle=0
    stop=1
def setrofka():
    global coje, angle, a,stop
    c.create_text(rng(500),rng(500),text=coje.get(),font='arial '+str(a),tags='setritka',angle=angle,fill=pick(farbi))
    angle+=10
    a+=2
    c.update()
    sleep(.5)
    if stop!=1:
        setrofka()
def setric():
    global coje, a, angle,stop
    coje=tk.Entry()
    coje.pack()
    c.update()
    c.pack()
    c.bind('<Button-1>',res)
    a=3
    angle=0
    stop=0
    setrofka()


################################################################
##################TITULKY ČI ČO TO BOLO#########################
################################################################

