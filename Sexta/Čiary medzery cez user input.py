import tkinter as tk
import random
c=tk.Canvas(height=500,width=500)
c.pack()
def sus(xy):
    x=xy.x
    y=xy.y
    for ඞ in range(0,int(amogus.get())):
        c.create_line(x,y-20,x,y+20,fill='blue')
        x+=int(baka.get())
        y+=int(random.randrange(-1,2))
def gon():
    c.delete('all')
amogus=tk.Entry()
amogus.pack()
baka=tk.Entry()
baka.pack()
butt=tk.Button(text="Zmaž",command=gon)
butt.pack()
c.bind('<Button-1>',sus)
