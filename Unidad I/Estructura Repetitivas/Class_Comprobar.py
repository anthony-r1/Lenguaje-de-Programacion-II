class Comprobar:
    def __init__(self):
        pass

    def respuesta(self):
        print("Verificar numeros")
        self.numero = float(input("Ingrese un numero: "))
        while True:
            respuesta = input("Desea realizar otra operacion? (s/n): ").lower()
            if respuesta in ['s', 'n']:
                return respuesta
            else:
                print("Por favor, ingrese 's' para si o 'n' para no.")

def main():
    comprobar = Comprobar()
    comprobar.respuesta()

if __name__ == "__main__":
    main()