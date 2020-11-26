import tkinter
canvas = tkinter.Canvas(height=390, width=430)
canvas.pack()


#Znaczka prva
    #vrch
canvas.create_oval(10, 10, 210, 210, fill='white')
#outline
canvas.create_oval(15, 15, 205, 205, fill='red')
#czerveny keruh
canvas.create_oval(40, 40, 180, 180, fill='white')
#fill
canvas.create_text(110, 110, text='80', font='arial 75 bold')
#text

    #spodek
canvas.create_rectangle(10, 210, 210, 330, fill='black')
#vonkajshko obdoliznik
canvas.create_rectangle(12.4, 212.4, 207.5, 327.5, fill='white')
#vnutrajshko obdoliznik
canvas.create_text(110, 270, text='22:00-06:00', font='arial 25 bold')
#text
canvas.create_rectangle(105, 330, 115, 380, fill='grey')
#tichken


#Znaczka druha
    #vrch
canvas.create_oval(220, 10, 420, 210, fill='white')
#outline
canvas.create_oval(225, 15, 415, 205, fill='red')
#czerveny kruh
canvas.create_oval(250, 40, 390, 180, fill='white')
#fill
canvas.create_text(320, 110, text='80', font='arial 75 bold')
#text


    #spodek
canvas.create_rectangle(220, 210, 420, 330, fill='black')
#vonkajshko obdoliznik
canvas.create_rectangle(222.4, 212.4, 417.5, 327.5, fill='white')
#vnutrajshko obdoliznik
        #oblak
canvas.create_oval(240, 240, 285, 285, fill='black')
#kruh1
canvas.create_oval(265, 225, 325, 285, fill='black')
#kruh 2
canvas.create_oval(305, 230, 355, 285, fill='black')
#kruh 3
canvas.create_oval(340, 245, 390, 285, fill='black')
#kruh 4
canvas.create_rectangle(240, 280, 390, 285, fill='white', outline='white')
#biely obdoliznik
canvas.create_line(250, 285, 242, 302.5, width=5)
#dazd 1
canvas.create_line(266.25, 285, 251.25, 320, width=5)
#dazd 2
canvas.create_line(282.5, 285, 274.5, 302.5, width=5)
#dazd 3
canvas.create_line(298.75, 285, 283.75, 320, width=5)
#dazd 4
canvas.create_line(315, 285, 307, 302.5, width=5)
#dazd 5
canvas.create_line(331.25, 285, 316.25, 320, width=5)
#dazd 6
canvas.create_line(347.5, 285, 339.5, 302.5, width=5)
#dazd 7
canvas.create_line(364.25, 285, 349.25, 320, width=5)
#dazd 8
canvas.create_line(380, 285, 372, 302.5, width=5)
#dazd 9
canvas.create_rectangle(320, 330, 330, 380, fill='grey')
#tichken
