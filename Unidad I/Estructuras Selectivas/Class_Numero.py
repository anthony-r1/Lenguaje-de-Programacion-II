class Numero:
    def __init__(self ,valor):
        self.valor = valor

    def clasificar(self):
        if self.valor == 0:
            return "Nulo"
        elif self.valor %2 == 0:
            return "Par"
        else:
            return "Impar"
        
ejemplo = [Numero(0), Numero(3), Numero(4), Numero(7), Numero(10)]

for numero in ejemplo:
    tipo = numero.clasificar()
    print(f"El número {numero.valor} es: {tipo}")