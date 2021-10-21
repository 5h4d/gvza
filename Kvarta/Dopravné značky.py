import tkinter
canvas = tkinter.Canvas(width=230, height=120)
canvas.pack()


#vec 1
canvas.create_oval(10, 10, 110, 110, fill='white')
#outline
canvas.create_oval(15, 15, 105, 105, fill='red')
#czerveny keruh
canvas.create_oval(25, 25, 95, 95, fill='white')
#fill
canvas.create_text(60, 60, text='80', font='arial 35 bold', fill='black')
#textung 80



#vec 2
canvas.create_rectangle(120, 10, 220, 110, fill='midnightblue')
#background
canvas.create_text(170, 50, text='H',fill='white', font='arial 70 bold')
#Hchko
canvas.create_text(170, 95, text='NEMOCNICA', fill='white', font='arial 11 bold')
#nemocnicapis
