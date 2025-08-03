# Utilizando un ciclo while, solicita al usuario que ingrese edades
# una a una. El proceso termina cuando se introduzca -1.
# Al final, muestra la edad mayor que se haya ingresado.

while True:
    edad = int(input("Ingrese una edad (-1 para salir): "))
    if edad == -1:
        break
    if 'mayor' not in locals() or edad > mayor:
        mayor = edad

print("La edad mayor ingresada es:", mayor)




