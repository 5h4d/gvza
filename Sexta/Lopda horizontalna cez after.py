import tkinter as tk
c=tk.Canvas(height=50,width=500)
c.pack()
x=0
m=0
def yes():
    global x,m
    c.delete('all')
    c.create_oval(x,20,x+10,30,fill='red')
    if x==490:
        m=1
    if x==0:
        m=0
    if m==1:
        x-=5
    if m==0:
        x+=5
    c.after(1,yes)
yes()
