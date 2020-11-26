import tkinter
canvas = tkinter.Canvas(width=300, height=300)
canvas.pack()
canvas.create_rectangle(100, 150, 200, 250, fill='red')
#telo
canvas.create_oval(125, 100, 175, 150)
#hlava
canvas.create_oval(135, 130, 165, 135)
#usta
canvas.create_oval(135, 110, 145, 120)
#oko lave
canvas.create_oval(155, 110, 165, 120)
#oko prave
canvas.create_oval(120, 105, 180, 100, fill='black')
#klobuk spodek
canvas.create_rectangle(125, 102.5, 175, 80, fill='black')
#klobuk stredek
canvas.create_oval(125, 65, 175, 95, fill='black')
#klobuk vrchek
canvas.create_oval(139, 114, 141, 116, fill='black')
#zrenica lava
canvas.create_oval(159, 114, 161, 116, fill='black')
#zrenica prava
