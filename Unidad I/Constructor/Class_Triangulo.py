import math
class TrianguloRectangulo:
    def __init__(self,cata,catb):
        self.cata = cata
        self.catb = catb
    
    def calcular_hipo(self):
        hipotenusa = math.sqrt(self.cata**2 + self.catb**2)
        return hipotenusa
    
    def __del__(self):
        print("Objeto Triangulo Rectangulo fue Destruido")

def main():
    try:
        cateto_a = float(input("Ingrese el valor del cateto a: "))
        cateto_b = float(input("Ingrese el valor del cateto b: "))
        
        triangulo1 = TrianguloRectangulo(cateto_a,cateto_b)
        resultado = triangulo1.calcular_hipo()
        print(f"La hipotenusa del triangulo es: {resultado}")
        
        del triangulo1
        
        try:
            print(triangulo1)
        except NameError:
            print("El objeto triangulo1 ya no existe")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese números.")
        
if __name__ == "__main__":
    main()