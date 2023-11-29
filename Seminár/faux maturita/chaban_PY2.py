from tkinter import Canvas
from random import randint as rng

c = Canvas(height=200, width=200, bg="white")
c.pack()


def kruzko() -> None:
    '''Vyberie náhodné súradnice a ak sa nachádzajú v danej kružnici tak vykreslí krúžok so stredom vo vybranom bode'''
    x: int = rng(50, 150)
    y: int = rng(50, 150)
    if ((x-100)**2 + (y-100)**2)**0.5 <= 40: # Stredová rovnica vnútornej oblasti kružnice so stredom [100,100] a polomerom 40
        c.create_oval(x-10, y-10, x+10, y+10, fill="blue") # Samotný krúžok
    c.after(100, kruzko) # Rekurzia po 0.1 sekunde


kruzko()
c.mainloop()
