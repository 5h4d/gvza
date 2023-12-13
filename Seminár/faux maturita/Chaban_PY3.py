čísla: tuple[int,int,int,int,int,int,int] = tuple(int(input()) for x in range(7))

max=čísla[0]
min=čísla[0]
for i in čísla:
    max=i if i>max else max
    min=i if i<min else min
    
print()
print(f'min: {min}')
print(f'max: {max}')