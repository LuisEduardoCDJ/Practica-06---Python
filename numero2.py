##Crear una clase Contacto . Esta clase deberá tener los atributos "nombre, apellidos, telefono y direccion". También deberá tener una función "SetContacto"  con los parámetros que permita cambiar el valor de los atributos. También tendrá una función "Saludar", que escribirá en pantalla "Hola, soy " seguido de sus datos. Crear también una clase llamada ProbarContacto. Esta clase deberá contener sólo la función principal, que creará dos objetos de tipo Contacto, les asignará los datos del contacto y les pedirá que saluden

datos=[]
datos1=[]
class contacto:
  nombre="Luis Eduardo"
  datos.append(nombre)
  apellido="Castillo de jesus"
  datos.append(apellido)
  telefono= 789654123
  datos.append(telefono)
  direccion="El millon #36"
  datos.append(direccion)
  def SetContacto(self):
    cambiar=int(input("Que deseas cambiar?\n 1.nombre\n 2.apellido\n 3.telefono\n 4.dirrecion\n Digite la opcion aqui: ->"))
    if cambiar == 1:
      datos.remove(self.nombre)
      newname=input("Escriba el nuevo nombre:\n ->")
      datos.append(newname) 
      datos1.append(newname) 
      print(f"Se ha cambiado {self.nombre} por {newname}")
    if cambiar == 2: 
      datos.remove(self.apellido)
      newape=input("Escriba su nuevo apellido:\n ->")
      datos.append(newape)
      datos1.append(newape)
      print(f"Se ha cambiado {self.apellido} por {newape}")
    if cambiar ==3:
      datos.remove(self.telefono)
      newtele=input("Escriba su nuevo numero:\n ->")
      datos.append(newtele)
      datos1.append(newtele)
      print(f"Se ha cambiado {self.telefono} por {newtele}.\n")
    if cambiar ==4:
      datos.remove(self.direccion)
      newadres=input("Escribas su nuevo apellido:\n->")
      datos.append(newadres)
      datos1.append(newadres)
      print(f"Se ha cambiado {self.direccion} por {newadres}.\n")
    else:
      if cambiar < 1 and cambiar >4:
        print("No has cambiado nada.")
  def saludar (self):
    print(f"Hola ,como estas? \n {datos}")
class porbarcontactos ():
  def funcion_principa():
    print(f"Su datos son {datos}")
    print(f"Se han cambiados los datos:\n {datos1}")
    


personas1=contacto()
personas1.SetContacto()
personas1.saludar()  
personas2=porbarcontactos()
porbarcontactos.funcion_principal()
