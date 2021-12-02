import tkinter as tk
c=tk.Canvas(height=500,width=50)
c.pack()
y=0
def perkele():
    global y
    c.delete('all')
    c.create_oval(20, y, 30, y+10,fill='red')
    y+=5
    if y==500:
        y=0
    c.after(1,perkele)
perkele()
