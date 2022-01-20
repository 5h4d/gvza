import tkinter as tk
c = tk.Canvas(width=600,height=600)
c.pack()

def susus(xy):
    x=xy.x
    y=xy.y
    c.create_rectangle(x-40,y,x+40,y-20,width=3,outline='grey',tags='vec')
    c.create_text(x,y-10,text=sus.get(),font='arial 7',tags='vec')
    c.create_line(x,y,x,y+50,width=3,fill='grey',tags='vec')
    if amogus.get() == 'k':
        c.create_line(x-30,y,x+30,y-16,width=3,fill='grey',tags='vec')
def gon():
    c.delete('vec')
        

sus=tk.Entry()
sus.pack()
amogus=tk.Entry()
amogus.pack()
butt=tk.Button(text='Zmaž', command=gon)
butt.pack()
c.bind('<Button-1>',susus)
