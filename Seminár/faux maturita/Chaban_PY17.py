rč = input("rodné číslo: ")
dd = rč[4:6]
mm = rč[2:4] if int(rč[2:4]) <= 12 else str(int(rč[2:4]) - 50)
yyyy = "19" + rč[:2]
print("dátum narodenia: " + dd + "." + mm + "." + yyyy)
print("pohlavie: {}".format("muž" if int(rč[2:4]) <= 12 else "žena"))
