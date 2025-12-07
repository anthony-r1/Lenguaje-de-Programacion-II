class Nadador: # clase base 1
    def nadar(self):
        print("Nadando en el agua")

class Volador: # clase base 2
    def volar(self):
        print("Volando por el aire")

class Pato(Nadador, Volador):
    def graznar(self):
        print("¡Cuac!")

class Cisne(Nadador, Volador):
    def graznar(self):
        print("¡Graa Graa Graa!")

pato = Pato()
pato.nadar()
pato.volar()
pato.graznar()
cisne = Cisne()
cisne.nadar()
cisne.volar()
cisne.graznar()
