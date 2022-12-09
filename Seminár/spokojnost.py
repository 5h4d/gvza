from tkinter import Canvas
c=Canvas(width=500, height=300, bg='grey')
c.pack()
c.create_text(250, 50, text='Boli ste spokojní s týmto tu?', font='comicsans 20')
c.create_rectangle(20,160,120,230,fill='blue')
c.create_rectangle(380,160,480,230,fill='blue')
c.create_text(70,195,text='yea', font='arial 30')
c.create_text(430,195,text='ne',font='arial 30')
yee=open('spokojnost.txt','w')
yee.close()
def bruh(xy):
    yee=open('spokojnost.txt','a')
    if 20<=xy.x<=120 and 160<=xy.y<=230:
        yee.write('spokojny typek \n')
    elif 380<=xy.x<=480 and 160<=xy.y<=230:
        yee.write('nespokojny typek \n')
    yee.close()
c.bind('<Button-1>', bruh)
