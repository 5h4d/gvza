import tkinter
import random
canvas = tkinter.Canvas(height=20, width=130)
canvas.pack()
canvas.create_text(10, 10, text=random.randint(1, 49))
canvas.create_text(30, 10, text=random.randint(1, 49))
canvas.create_text(50, 10, text=random.randint(1, 49))
canvas.create_text(70, 10, text=random.randint(1, 49))
canvas.create_text(90, 10, text=random.randint(1, 49))
canvas.create_text(110, 10, text=random.randint(1, 49))

#Nepovedal by som že by sa to dalo v lotérií použiť keďže nie je možné vytvoriť skutočne náhodný program a dalo by sa ten algorytmus uhádnuť
