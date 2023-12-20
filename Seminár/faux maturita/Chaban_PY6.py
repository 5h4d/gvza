čiselko=int(input())

print(format(čiselko,'b'))
č5=čiselko
a=""
while č5:
    a=str(č5%5)+a
    č5//=5
print(a)
print(format(čiselko,'o'))