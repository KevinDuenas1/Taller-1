import math
def pri(a, b, c):
    return a * b * c
def pir(a, b, c):
    return a * b * c / 3
def con(a, b, c):
    return 1/3 * math.pi * a *  b**2 + c**2 + b*c
def cil(a, b):
    return math.pi * a**2 * b
 
while True:
    print("escojer figura")
    print("1. prisma")
    print("2. piramide")
    print("3. cono truncado")
    print("4. cilindro")

    eleccion = input("escojer numero de la figura: ")
    n1 = float(input("numero 1: "))
    n2 = float(input("numero 2: "))
    n3 = float(input("numero 3: "))

    if eleccion=="1":
        print("el volumen del prisma es: ",pri(n1,n2,n3))
    elif eleccion=="2":
        print("el volumen de la piramide es: ",pir(n1,n2,n3))
    elif eleccion=="3":
        print("el volumen del cono truncado es: ",con(n1,n2,n3))
    elif eleccion=="4":
        print("el volumen del cilindro es: ", cil(n1,n2))
    else:
        print("opcion invalida")

