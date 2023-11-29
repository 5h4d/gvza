from tkinter import Canvas
from math import sin, cos, radians
n=int(input("n: "))

c=Canvas(height=500,width=500,bg='white')
c.pack()

bodi=[(250+200*cos(radians(i*360/n)),
       250-200*sin(radians(i*360/n))) for i in range(n+1)]

for i,j in bodi:
    for x,y in bodi:
        c.create_line(i,j,x,y)

c.mainloop()
