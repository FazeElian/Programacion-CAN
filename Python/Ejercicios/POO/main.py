#Método Encapsulamiento:
class Coche:
  potenciaMotor = 120
  carroceria = "Ergonómica"
  velocidadConstante = 50
  velocidadMaxima = 250

  def _init_(self, carroceria):
    self.carroceria = carroceria

Coche = Coche("Tesla Model 3")

#Atributos
Coche.carroceria.potenciaMotor(120)
Coche.carroceria.carroceria("Ergonómica")
Coche.carroceria.velocidadConstante(50)
Coche.carroceria.velocidadMaxima(250)

#Método Herencia:
#Creamos clase padre
class Coche:
  potenciaMotor = 120
  carroceria = "Ergonómica"
  velocidadConstante = 50
  velocidadMaxima = 250

#Creamos clase hija
class Carroceria(Coche):
  color = "red"
  forma = "Ergonómica"
  diseño = "Deportivo"

def _init_(self, tipo, marca):
  self.tipo = "Sport"
  self.marca = "Tesla"

#Método Poliformismo:
class Coche:
  def arrancarMotor(self):
    pass #Vacío

  class Motor(Coche):
    def iniciar(self):
      print("Iniciar Motor")

  class Gasolina(Coche):
    def usar(self):
      print("Usar gasolina")

#Método Abstracción
class Coche:
  def prenderMotor():
    print("Prender motor")

  def acelerar():
    print("Presionar pedal para avanzar")

  def frenar():
    print("Presionar pedal de freno")

  #Llamar funciones
  prenderMotor()
  acelerar()
  frenar()