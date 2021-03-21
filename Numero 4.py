"""Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado."""

listas1=[]
listas2=[]
def superposicion():
  for x in range (1,3):
    nombre=input(f"Introduzca su nombre numero {x} para su lista 1:\n")
    listas1.append(nombre)
     
    for x in range (1):
      nombre1=input(f"Introduzca su nombre numero {x+1} para su lista 2:\n")
      listas2.append(nombre1)
  if listas1 == listas2:
    print("Es true porque tiene almenos un mientros en comun las 2 listas.")
  else:
    print("Es false porque no hay nombres iguales.")
      

definir=superposicion()
print(listas1,listas2)




