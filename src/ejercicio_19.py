# Con un ciclo for, cuenta cuántas vocales (sin distinción de 
# mayúsculas/minúsculas) hay en la frase frase = "programacion 
# es divertida" y muestra el total.

frase = "programacion es divertida"
vocales = "aeiou"
contador = 0

for caracter in frase.lower():
    if caracter in vocales:
        contador += 1

print(f"Total de vocales: {contador}")
