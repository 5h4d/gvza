from math import sqrt

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
try:
    print("x1 = " + str((-b + sqrt(b**2 - 4 * a * c)) / (2 * a)))
except:
    print("riešenie x1 neexistuje")
try:
    print("x2 = " + str((-b - sqrt(b**2 - 4 * a * c)) / (2 * a)))
except:
    print("riešenie x2 neexistuje")
