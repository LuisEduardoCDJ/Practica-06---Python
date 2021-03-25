#Crear una clase Persona que tenga como atributos el "cedula, nombre, apellido y la edad (definir las propiedades para poder acceder a dichos atributos)". Definir como responsabilidad una cuncion para mostrar ó imprimir. Crear una segunda clase Profesor que herede de la clase Persona. Añadir un atributo sueldo ( y su propiedad) y en la función para imprimir su sueldo. Definir un objeto de la clase Persona y llamar a sus funciones y propiedades. También crear un objeto de la clase Profesor y llamar a sus funciones y propiedades.

personas = []
objetos = []
cuenta=1000
def resposabilidad ():
  print(f"Sus datos son: \n {personas}")
  print(f"Su sueldo es:\n {objetos}")
class Persona:
  def informacion (self):
    self.cedula = int(input('Introduzca su cedula:\n'))
    personas.append (self.cedula)
    self.nombre = input('Digite su nombre:\n')
    personas.append(self.nombre)
    self.apellido = input('Digite su apellido:\n')
    personas.append(self.apellido)
    self.edad = int(input("Introduzca su edad:\n"))
    personas.append(self.edad)

class profesor(Persona):
  def infomae (self): 
    sueldo = float(input("Digite su sueldo: "))
    objetos.append(cuenta-sueldo)



persona1 = Persona()
persona1.informacion()
maestro1 = profesor()
maestro1.infomae()
resposabilidad()
    
