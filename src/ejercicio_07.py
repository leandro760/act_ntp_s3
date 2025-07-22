# Con un ciclo for, cuenta cuántas letras “a” (minúscula) hay
# en la cadena texto = "manzana" y muestra el total.

palabra = "manzanas"
contador = 0

for letra in palabra:
    if letra == "a":
        contador +=1
print(F"La palabra manzana tiene {contador} veces la letra a.")

