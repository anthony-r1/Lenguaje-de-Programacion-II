class Calculadora:
    def __init__(self):
        self.resultado = 0

    def sumar(self):
        print("Calcular la suma de los numeros ingresados")
        print("Escriba 'salir' para finalizar")
        while True:
            entrada = input("Ingrese un numero: ")
            if entrada == "salir":
                break
            try:
                numero = float(entrada)
                self.resultado += numero
            except ValueError:
                print("Por favor, ingrese un numero valido.")
        print("La suma total es:", self.resultado)

def main():
    calculadora = Calculadora()
    calculadora.sumar()

if __name__ == "__main__":
    main()