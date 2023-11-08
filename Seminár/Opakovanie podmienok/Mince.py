from tkinter import Canvas
from random import randint

k = int(input("k = "))
pokusy: list[list[tuple[int, int]]] = []  # Zoznam obsahujúci všetkých 10 pokusov

for i in range(
    10
):  # Vytvorenie individuálnych mincí v dvojiciach po hodnote a horizontálnej pozícií
    mince: list[tuple[int, int]] = []
    x = 2
    while sum(minca[0] for minca in mince) < k:
        mince.append((randint(1, 4), x))
        x += 22
    pokusy.append(mince)

c = Canvas(height=222, width=max(x[-1][1] for x in pokusy) + 100)
c.pack()

for i in range(len(pokusy)):  # Vykreslenie
    y = 2 + i * 22
    for minca in pokusy[i]:
        x = minca[1]
        c.create_oval(x, y, x+20, y+20, fill="white")
        c.create_text(x+10, y+10, text=minca[0], font="arial 12")
    if sum(pokusy[i][x][0] for x in range(len(pokusy[i]))) == k:
        c.create_text(
            max(x[-1][1] for x in pokusy)+60,
            y+10,
            text="HURÁ",
            font="arial 15",
            fill="green",
        )
    else:
        c.create_text(
            max(x[-1][1] for x in pokusy)+60,
            y+10,
            text="ŠKODA",
            font="arial 15",
            fill="red",
        )


c.mainloop()  # Zjavne to treba pre neinteraktívny session
