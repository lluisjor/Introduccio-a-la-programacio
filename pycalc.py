while True:
    print("""Benvinguts a pycalc, introduiu una de les següents opcions:
    0. Sortir
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir""")

    num = int(input("Introdueix un numero de les opcions:"))
    if num == 0:
        break

    if num == 1:
        suma1 = float(input("Introdueix el primer número per sumar: "))
        suma2 = float(input("Introduce el segundo número per sumar: "))
        suma = suma1 + suma2
        print("El resutat es, suma)

    if num == 2:
        rest1 = float(input("Introdueix el primer número per restar: "))
        rest2 = float(input("Introduce el segundo número per restar: "))
        resta = rest1 - rest2
        print( "El resutat es, resta")

    if num == 3:
        mult1 = float(input("Introdueix el primer número per multiplicar: "))
        mult2 = float(input("Introduce el segundo número per multiplicar: "))
        multiplicacio = mult1 * mult2
        print(multiplicacio)

    if num == 4:
        mult1 = float(input("Introdueix el primer número per multiplicar: "))
        mult2 = float(input("Introduce el segundo número per multiplicar: "))
        if mult2 == 0:
            print("El resultat es infinit.")
        else:
            multiplicacio = mult1 * mult2
            print(multiplicacio)
