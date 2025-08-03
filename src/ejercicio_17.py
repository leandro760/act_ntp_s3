# Con un ciclo for, solicita al usuario que ingrese un número
# entero positivo y calcula la suma de sus dígitos, mostrando el 
# resultado final.

numero = input("Ingresa un numero entero positivo: ")

total = 0

for digito in numero:
    total += int(digito)

print(f"La suma de los digitos del numero {numero} es: {total}")




    