class Verificar:
    def __init__(self):
        pass

    def respuesta(self):
        print("Verificar si un número es nulo, par o impar")
        print("Ponga fin para terminar el programa")
        entrada = ""
        while entrada.lower() != "fin":
            entrada = input("Ingrese un número (o 'fin' para terminar): ")
            if entrada.lower() == "fin":
                print("Programa terminado.")
                break
            try:
                numero = float(entrada)
                if numero == 0:
                    print("El número es nulo.")
                elif numero % 2 == 0:
                    print("El número es par.")
                else:
                    print("El número es impar.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número o 'fin'.")

def main():
    verificador = Verificar()
    verificador.respuesta()

if __name__ == "__main__":
    main()