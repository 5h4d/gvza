from tkinter import Canvas


x = int(input("x = "))
y = int(input("y = "))
r = int(input("r = "))
k = int(input("k = "))

c = Canvas(height=700, width=700, bg="white")
c.pack()

counter = 0
for i in range(0, r, 3):
    if r - i > 15:
        c.create_oval(x-r+i, y-r+i, x+r-i, y+r-i, outline="grey" if counter % k == 0 else "black")
    counter += 1


c.mainloop()
