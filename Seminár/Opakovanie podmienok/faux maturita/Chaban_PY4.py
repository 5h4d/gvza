from tkinter import Canvas, Entry, Button
from random import randrange as rng
c=Canvas(width=700, height=700)
c.pack()
field=Entry()
field.pack()

def butt() -> None:
    r, x, y = (int(rxy) for rxy in str(field.get()).split())
    c.create_oval(x-r, y-r, x+r, y+r, outline='', fill=(f'#{format(rng(256), '02x')}{format(rng(256), '02x')}{format(rng(256), '02x')}'))
    
tlatitko=Button(command=butt, text='kruh')
tlatitko.pack()
c.mainloop()
