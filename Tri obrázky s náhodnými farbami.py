import tkinter as tk
import random as r
#obraztok 1
x = r.randint(0, 370)
y = r.randint(0, 370)
telo = r.choice(('red', 'cyan', 'green', 'black', 'white', 'blue'))
canvas = tk.Canvas(width=500, height=500)
canvas.pack()

#ramik
canvas.create_rectangle(x, y, x+128, y+128, width=2)

#Among Us Crewmate
canvas.create_rectangle(x+69, y+119, x+89, y+89, fill=telo, width=2)  #prava noha
canvas.create_rectangle(x+39, y+119, x+59, y+89, fill=telo, width=2)  #lava noha
canvas.create_rectangle(x+19, y+44, x+44, y+94, fill=telo, width=2)  #batoh
canvas.create_oval(x+29, y+9, x+94, y+109, fill=telo, width=2)  #telo
canvas.create_oval(x+54, y+29, x+99, y+59, fill='lightblue', width=2)  #ocenka



#obraztok 2
a = r.randint(0, 250)
b = r.randint(0, 250)
farba = r.choice(('red', 'cyan', 'green', 'black', 'white', 'blue', 'magenta'))
canvas = tk.Canvas(tk.Toplevel(), width=750, height=750)
canvas.pack()

#ramik2
canvas.create_rectangle(a, b, a+498, b+498, width=2)

#hodziny
canvas.create_oval(a+9, b+9, a+489, b+489, width=5)
canvas.create_line(a+249.5, b+274, a+249.5, b+24, width=5, fill=farba)
canvas.create_line(a+234, b+254.5, a+379, b+254.5, width=5, fill=farba)

#chcel som to urobit o dosť zaujímavejšie ale to čo som mal v pláne by bolo trochu moc zložité tak som to nechal takto





#obraztok 3
m = r.randint(0, 450)
n = r.randint(0, 450)
bloon = r.choice(('red', 'cyan', 'green', 'black', 'blue', 'magenta'))   
canvas = tk.Canvas(tk.Toplevel(), width=750, height=750, background='white')
canvas.pack()


#ramik 3
canvas.create_rectangle(m, n, m+298, n+298, width=2)


#balonik ja neviem nenapadá mi nič už

canvas.create_line(m+144.5, n+189, m+154.5, n+189, m+149.5, n+149, m+144.5, n+189, fill=bloon, width=3)
canvas.create_oval(m+74, n+9, m+224, n+174, width=3, outline=bloon, fill='white')
canvas.create_line(m+146, n+175, m+144, n+298, width=3, fill=bloon)


#asi tak nejak
