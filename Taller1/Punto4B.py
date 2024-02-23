while True:
    print("***** robots *****")
    print("1. cilindrico")
    print("2. carteciano")
    print("3. esferico")

    eleccion = input("escoje un robot: ")
    if eleccion == "1":
        print(" el robot es cilindrico")
        print(" tiene 1 articulacion de revolucion y 2 articulaciones prismáticas")
    elif eleccion == "2":
        print(" el robot es carteciano ")
        print( "tine 3 articulaciones prismáticas")
    elif eleccion == "3":
        print(" el robot es esferico ")
        print( "tine 3 articulaciones rotacionales")
    else:
        print("no valido el digito")