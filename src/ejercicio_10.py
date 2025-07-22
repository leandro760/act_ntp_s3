# Mediante un ciclo while, solicita al usuario que escriba palabras. 
# El proceso termina cuando el usuario escriba la palabra “fin”. 
# Al final, muestra cuántas palabras se leyeron (sin contar “fin”).

total = 0

while True:
    palabra = input("Ingrese una palabra ('fin' para salir): ")
    if palabra == "fin":
       break
    total += 1
print(f"El usuario ingreso {total} palabras.")