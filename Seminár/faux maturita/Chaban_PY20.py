from tkinter import Canvas, Entry, Button
from random import randrange as rng
c=Canvas(height=500,width=500)
c.pack()
def pome():
    c.create_text(rng(500),rng(500),text=text.get(),angle=int(uhol.get()),fill=(f'#{format(rng(256), '02x')}{format(rng(256), '02x')}{format(rng(256), '02x')}'))
def preč(Null):
    c.delete('all')
text=Entry()
uhol=Entry()
zrob=Button(text='go',command=pome)
text.pack()
uhol.pack()
zrob.pack()
c.bind('<Button-1>', preč)
c.mainloop()
