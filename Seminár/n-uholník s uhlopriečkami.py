from tkinter import Canvas
from math import sin, cos, radians
n=int(input("n: "))

c=Canvas(height=500,width=500,bg='white')
c.pack()

ang=360/n
curang=0
bodi=[]
for i in range(n+1):
    bodi.append((250+200*cos(radians(curang)),250-200*sin(radians(curang))))
    curang+=ang

for i,j in bodi:
    zvysk=[x for x in bodi] """táto časť je vpodstate nepotrebná, následujúci loop by mohol vpohode pracovať
                               aj s celým bodi len by tam boli čiary ukazujúce samé na seba, čo sa deje aj
                               teraz keď sa nad tým zamýšľam"""
    zvysk.remove((i,j))
    for x,y in zvysk:
        c.create_line(i,j,x,y)
