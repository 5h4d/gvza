from tkinter import Canvas
from matplotlib import colors
from random import choice
from math import sqrt

colors = list(colors.cnames.keys())


def trojuholniky(a: tuple[int], b: tuple[int], c: tuple[int]):
    """Rekurzívna funkcia vykresľujúca trojuholníky na základe súradníc najväčšieho"""
    if (
        min(
            sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
            for x, y in ((a, b), (b, c), (c, a))
        )
        >= 30
    ):
        can.create_polygon(a, b, c, fill=choice(colors))
        Sbc = (b[0] + c[0]) // 2, (b[1] + c[1]) // 2
        Sac = (a[0] + c[0]) // 2, (a[1] + c[1]) // 2
        Sab = (a[0] + b[0]) // 2, (a[1] + b[1]) // 2
        trojuholniky(Sbc, Sac, Sab)
    else:
        return None


a = tuple(int(x) for x in input("a: ").split(","))
b = tuple(int(x) for x in input("b: ").split(","))
c = tuple(int(x) for x in input("c: ").split(","))

can = Canvas(width=800, height=800)
can.pack()

trojuholniky(a, b, c)

can.mainloop()
