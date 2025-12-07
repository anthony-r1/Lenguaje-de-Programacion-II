class Animal: # clase base
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        pass

class Perro(Animal): # clase derivada
   def hacerSonido(self):
        return "¡Guau,Guau!"

class Gato(Animal):
    def hacerSonido(self):
        return "¡Miauuu!"

perro = Perro("Henry")
print(f"{perro.nombre} dice {perro.hacerSonido()}")

gato = Gato("Luz")
print(f"{gato.nombre} dice {gato.hacerSonido()}")
