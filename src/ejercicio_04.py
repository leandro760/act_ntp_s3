# Utilizando un ciclo while, solicita al usuario que ingrese números. 
# El proceso termina cuando el usuario escriba 0. Al final, 
# muestra la suma total de todos los números ingresados.

suma = 0

while True:
  numero = input("Ingrese un número, (0 para terninar): ")
  if numero == "0":
    break
  suma += float(numero)
print("La suma total de los números ingresados es: ", suma)
    
