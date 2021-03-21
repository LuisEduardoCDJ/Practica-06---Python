"""Crear tres clases ClaseA, ClaseB, ClaseC que ClaseB herede de ClaseA y ClaseC herede de ClaseB. Definir un constructor a cada clase que muestre un mensaje. Luego definir un objeto de la clase ClaseC."""
class clasea():
  def constructor1():
    print("Hola, Soy mundo.")
class claseb(clasea):
  def constructor2():
    print("Hola, Manuela es mi amiga.")
class clasec(claseb):
  def constructor3():
    carro = "rojo"
    print("Eline y yo somos hermanos.")
  
llamando=clasea()
clasea.constructor1()
llamando3=claseb()
claseb.constructor2()
llamando2=clasec()
clasec.constructor3()

    