pal = input("Reťazec: ")
test = "".join(pal.lower().split())
print(pal + " je palindróm" if test == test[::-1] else pal + " nie je palindróm")
