#1
try:
    num1 = float(input("Posa un numero: "))
    num2 = float(input("Posa un altre numero: "))
    resultat: num1 / num2
    print(resultat)
except:
  print("Error")
#2
num1 = input("Dime un numero :")
try:
    resultat: int(num1)
    print(resultat)
except:
    print("Error")

#3
try:
    valor1 = float(input("introdueix un numero"))
    valor2 = float(input("Introdueix un numero"))
    resultat = valor1 + valor2
    print(resultat)
except:
    print("Error")

#4
llista = [1,3,5,6]
try:
    num = int(input("Fica el numero de la llista"))
    print(llista[num])
except:
    print("Error")
