from tkinter import Canvas


x = int(input("x = "))
y = int(input("y = "))
r = int(input("r = "))
k = int(input("k = "))

c=Canvas(height=700, width=700, bg='white')
c.pack()

for i in range(r//3):
    c.create_oval(x-r+i, y-r+i, x+r-i, y+r-i)