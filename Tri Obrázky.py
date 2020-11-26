import tkinter as tk
#obraztok 1
canvas = tk.Canvas(width=130, height=130)
canvas.pack()

#ramik
canvas.create_rectangle(1, 1, 129, 129, width=2)

#Among Us Crewmate
canvas.create_rectangle(70, 120, 90, 90, fill='red', width=2)  #prava noha
canvas.create_rectangle(40, 120, 60, 90, fill='red', width=2)  #lava noha
canvas.create_rectangle(20, 45, 45, 95, fill='red', width=2)  #batoh
canvas.create_oval(30, 10, 95, 110, fill='red', width=2)  #telo
canvas.create_oval(55, 30, 100, 60, fill='lightblue', width=2)  #ocenka



#obraztok 2
canvas = tk.Canvas(tk.Toplevel(), width=500, height=500)
canvas.pack()

#ramik2
canvas.create_rectangle(1, 1, 499, 499, width=2)

#hodziny
canvas.create_oval(10, 10, 490, 490, width=5)
canvas.create_line(250.5, 275, 250.5, 25, width=5)
canvas.create_line(235, 255.5, 380, 255.5, width=5)






#obraztok 3

canvas = tk.Canvas(tk.Toplevel(), width=300, height=300, background='white')
canvas.pack()


#ramik 3
canvas.create_rectangle(1, 1, 299, 299, width=2)


#balonik ja neviem nenapadá ma nič už

canvas.create_line(145.5, 190, 155.5, 190, 150.5, 150, 145.5, 190, fill='green', width=3)
canvas.create_oval(75, 10, 225, 175, width=3, outline='green', fill='white')
canvas.create_line(147, 176, 145, 299, width=3, fill='green')


