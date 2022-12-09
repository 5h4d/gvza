from tkinter import Canvas, Button
c=Canvas(width=300, height=150, bg='grey')
c.pack()
c.create_text(150, 40, text='Boli ste spokojní s týmto tu?', font='comicsans 15')
yee=open('spokojnost.txt','w')
yee.close()
def bruh():
    yee=open('spokojnost.txt','a')
    yee.write('spokojny typek \n')
    yee.close()
def briuh():
    yee=open('spokojnost.txt','a')
    yee.write('nespokojny typek \n')
    yee.close()
yae=Button(text='yea',command=bruh)
yae.place(x=25,y=70)
nae=Button(text='ne',command=briuh)
nae.place(x=230,y=70)
