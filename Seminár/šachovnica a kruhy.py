from tkinter import Canvas, Toplevel
from time import sleep


r=int(input("polomer kruhov: "))
print()
print("Šachovnica")
nx=int(input("počet stĺpcov: "))
ny=int(input("počet riadkov: "))

c=Canvas(height=20+3.2*r,width=20+6.4*r,bg='white')
c.pack()

c.create_oval(10,10,10+2*r,10+2*r,outline='blue',width=15)
c.create_oval(10+1.2*r,10+1.2*r,10+3.2*r,10+3.2*r,outline='yellow',width=15)
c.create_oval(10+2.2*r,10,10+4.2*r,10+2*r,outline='black',width=15)
c.create_oval(10+3.4*r,10+1.2*r,10+5.4*r,10+3.2*r,outline='green',width=15)
c.create_oval(10+4.4*r,10,10+6.4*r,10+2*r,outline='red',width=15)


"""Tá preslávená šachovnica"""
c=Canvas(Toplevel(),height=(ny*33)+2,width=(nx*33)+2,bg='white')
c.pack()

p=0
sach=[(x+3,y+3,x+33,y+33) for x in range(0,nx*33,33) for y in range(0,ny*33,33)]
for i in sach:
    if p==0:
        c.create_rectangle(i,fill='purple')
        p=1
        if (sach.index(i)+1) % ny == 0 and ny % 2 == 0:
            p=0
    else:
        c.create_rectangle(i,fill='black')
        p=0
        if (sach.index(i)+1) % ny == 0 and ny % 2 == 0:
            p=1

