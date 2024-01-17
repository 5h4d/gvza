from tkinter import Canvas

c=Canvas(height=336,width=336)
c.pack()

stverce=[(x+1,y+1,x+41,y+41) for x in range(0,337, 42) for y in range(0,337,42)]
a=0
for stverc in stverce:
    if a==0:
        c.create_rectangle(stverc, fill='black')
        a=1
    else:
        c.create_rectangle(stverc, fill='white')
        a=0
        
c.mainloop()