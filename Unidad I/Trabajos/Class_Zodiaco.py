class Zodiaco:
    def __init__(self, dia, mes):
        self.dia = dia
        self.mes = mes

    def obtener_signo(self):
        if self.mes < 1 or self.mes > 12:
            return "Fecha inválida"

        if (self.mes == 3 and 21 <= self.dia <= 31) or (self.mes == 4 and 1 <= self.dia <= 19):
            return "Aries"
        elif (self.mes == 4 and 20 <= self.dia <= 30) or (self.mes == 5 and 1 <= self.dia <= 20):
            return "Tauro"
        elif (self.mes == 5 and 21 <= self.dia <= 31) or (self.mes == 6 and 1 <= self.dia <= 20):
            return "Géminis"
        elif (self.mes == 6 and 21 <= self.dia <= 30) or (self.mes == 7 and 1 <= self.dia <= 22):
            return "Cáncer"
        elif (self.mes == 7 and 23 <= self.dia <= 31) or (self.mes == 8 and 1 <= self.dia <= 22):
            return "Leo"
        elif (self.mes == 8 and 23 <= self.dia <= 31) or (self.mes == 9 and 1 <= self.dia <= 22):
            return "Virgo"
        elif (self.mes == 9 and 23 <= self.dia <= 30) or (self.mes == 10 and 1 <= self.dia <= 22):
            return "Libra"
        elif (self.mes == 10 and 23 <= self.dia <= 31) or (self.mes == 11 and 1 <= self.dia <= 21):
            return "Escorpio"
        elif (self.mes == 11 and 22 <= self.dia <= 30) or (self.mes == 12 and 1 <= self.dia <= 21):
            return "Sagitario"
        elif (self.mes == 12 and 22 <= self.dia <= 31) or (self.mes == 1 and 1 <= self.dia <= 19):
            return "Capricornio"
        elif (self.mes == 1 and 20 <= self.dia <= 31) or (self.mes == 2 and 1 <= self.dia <= 18):
            return "Acuario"
        elif (self.mes == 2 and 19 <= self.dia <= 29) or (self.mes == 3 and 1 <= self.dia <= 20):
            return "Piscis"
        else:
            return "Fecha inválida"


def main():
    dia = int(input("Ingresa tu día de nacimiento: "))
    mes = int(input("Ingresa tu mes de nacimiento (en número): "))
    persona = Zodiaco(dia, mes)
    print("Tu signo zodiacal es:", persona.obtener_signo())


if __name__ == "__main__":
    main()