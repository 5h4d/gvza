from tkinter import Canvas
from random import randrange as rng

with open('cisla.txt') as cisla:
    čísla: list[int]=[]
    for line in cisla:
        čísla.append(int(line))

c=Canvas(width=460, height=max(čísla)*8+20, bg='white')
c.pack()
for i in range(15):
    c.create_rectangle(10+i*30, max(čísla)*8+20-(10+čísla[i]*8), 30+i*30, max(čísla)*8+10, fill=(f'#{format(rng(256), '02x')}{format(rng(256), '02x')}{format(rng(256), '02x')}'))
    
c.mainloop()