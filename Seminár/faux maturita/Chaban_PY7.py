from tkinter import Canvas, Entry
c=Canvas(height=500,width=500,bg='white')
c.pack()

def tlačítko(xy):
    x=xy.x
    y=xy.y
    r=int(polomer.get())
    c.create_oval(x-r,y-r,x+r,y+r,fill='red',outline='red')
    
polomer=Entry()
polomer.pack()

c.bind('<Button-1>',tlačítko)
c.mainloop()