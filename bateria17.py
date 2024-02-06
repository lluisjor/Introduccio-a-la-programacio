resultat = 0
suma_numeros = 0
quantitat_numero = 0
while True:
    num = int(input("Digues un numero: "))
    if num == 0:
        break
    quantitat_numero += 1
    suma_numeros += num
resultat = suma_numeros / quantitat_numero
print(resultat)
