from tkinter import Canvas
c=Canvas(width=20,height=100)
c.pack()
hepi=engi=0
yee=open('spokojnost.txt', 'r')
aaa=yee.readlines()
sumec=len(aaa)
for i in range(sumec):
    if aaa[i] == 'spokojny typek' or aaa[i] == 'spokojny typek \n':
        hepi+=1
    else:
        engi+=1
print('Počet zákazníkov: '+str(sumec))
hepipro=100-(hepi/sumec*100)
engipro=100-(engi/sumec*100)
c.create_line(5,100,5,hepipro,width=10,fill='green')
c.create_line(15,100,15,engipro,width=10,fill='red')
yee.close()
print('Spokojních bolo '+str(hepipro//1)+'%')
print('Nespokojných bolo'+str(engipro//1)+'%')
