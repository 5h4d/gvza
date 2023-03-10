from PIL import Image as img
def nowy(w,h,file=None):
    kropotkin=img.new('RGB',(w,h),'white')
    try:
        kropotkin.save(file)
    except ValueError:
        obrazek.show()
def con(old,new):
    hegel=img.open(old)
    hegel.save(new)
def shrink(engels):
    marx=img.open(engels)
    gaddafi=marx.resize((128,int(marx.height*128/marx.width)))
    gaddafi.save(engels[:-3]+'new'+engels[-4:])
