# Utilizando un ciclo while, calcula el factorial de un número entero n
# introducido por el usuario y muestra el resultado.

numero = int(input("Por favor ingrese un numero entero: "))
numero_original = numero

factorial = 1

while numero > 0:
    factorial *= numero
    numero -= 1

print(f"El factorial del número {numero_original} es: {factorial}")






