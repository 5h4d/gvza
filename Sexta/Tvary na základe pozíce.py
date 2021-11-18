import tkinter as tk
c = tk.Canvas(height=400, width=400)
c.pack()

c.create_line(0, 200, 400, 200, width=4)

def bruh(xy):
    x=xy.x
    y=xy.y
    if y<200:
        c.create_rectangle(x, y, x+20, y+20, fill='blue', outline='blue',tags='yes')
    else:
        c.create_oval(x, y, x+20, y+20, fill='yellow', outline='yellow', tags='yes')

def gon(nah):
    c.delete('yes')

c.bind('<Button-1>',bruh)
c.bind_all('r',gon)
print('rkom odstrániť')
