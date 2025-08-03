# Mediante un ciclo while, implementa un juego de adivinanza: 
# el programa genera un número aleatorio del 1 al 10 y solicita 
# al usuario que lo adivine. El proceso se repite hasta que el 
# usuario acierte. Muestra un mensaje de felicitación al final.

import random

numero_secreto = random.randint(1,10)
intentos = 0

while True:
    numero_usuario = int(input("Adivina el numero del 1 al 10: "))
    intentos = intentos + 1
    if numero_usuario == numero_secreto:
        print(f"¡Felicidades ganaste!, tomo {intentos} intentos.")
        break