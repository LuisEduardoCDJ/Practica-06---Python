""""Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma. Usando funciones"""

arreglo=[]
def lista():
  for x in range (10):
    enteros=int(input(f"Ingrese su numero {x+1}:\n -> "))
    arreglo.append(enteros,)
lista()
mostar=arreglo
print(f"Su 10 digitos son:\n {arreglo}")

