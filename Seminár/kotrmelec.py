import tkinter as tk
c = tk.Canvas(height=100,width=900)
c.pack()

def sus():
    c.delete('txt')
    x=50
    r=0
    a=360/(len(davaj.get())-1)
    c.delete('yes')
    for i in range(len(davaj.get())):
         c.create_text(x,50,text=davaj.get()[i],angle=r,font='arial 20',tags='txt')
         x+=30
         r+=a

davaj=tk.Entry()
davaj.pack()
w=tk.Button(text='O',command=sus)
w.pack()
