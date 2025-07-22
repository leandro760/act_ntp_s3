# Con un ciclo for, imprime la tabla de multiplicar del 7, 
# es decir, 7 × 1, 7 × 2, …, 7 × 10, cada resultado en una línea.

print("Tabla de multiplicar del 7: ")
print("")

for i in range(1 , 11):
  resultado = 7 * i
  print(f"7 x {i} = {resultado}")
