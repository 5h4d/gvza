from tkinter import Canvas
from math import sin, cos, radians

hh = radians(360 / 12 * (int(input("počet hodín: ")) % 12) + 90)
mm = radians(360 / 60 * (int(input("počet minút: ")) % 60) + 90)
c = Canvas(height=500, width=500)
c.pack()
c.create_oval(5, 5, 495, 495, fill="white", width=10)
c.create_line(250, 250, 250 - 150 * cos(hh), 250 - 150 * sin(hh), width=7)
c.create_line(250, 250, 250 - 230 * cos(mm), 250 - 230 * sin(mm), width=5)
c.mainloop()
