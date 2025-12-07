import math
from typing import TypeVar, Generic

# Definición del tipo genérico (int o float)
T = TypeVar('T', int, float)

class FiguraGeometrica(Generic[T]):
    """Clase Genérica Base: Figura Geométrica"""
    def area(self) -> float:
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def perimetro(self) -> float:
        raise NotImplementedError("Este método debe ser implementado por la subclase")

class Rectangulo(FiguraGeometrica[T]):
    """Clase Rectángulo que hereda de FiguraGeometrica"""
    def __init__(self, base: T, altura: T):
        self.base = base
        self.altura = altura

    def area(self) -> T:
        try:
            return self.base * self.altura
        except Exception as e:
            raise Exception(f"Error al calcular área del rectángulo: {e}")

    def perimetro(self) -> T:
        try:
            return 2 * (self.base + self.altura)
        except Exception as e:
            raise Exception(f"Error al calcular perímetro del rectángulo: {e}")

class Circulo(FiguraGeometrica[T]):
    """Clase Círculo que hereda de FiguraGeometrica"""
    def __init__(self, radio: T):
        self.radio = radio

    def area(self) -> float:
        try:
            if self.radio < 0:
                raise ValueError("El radio no puede ser negativo")
            return math.pi * (self.radio ** 2)
        except ValueError as ve:
            raise ArithmeticError(f"Error de valor en Círculo: {ve}")
        except Exception as e:
            raise Exception(f"Error inesperado al calcular área del círculo: {e}")

    def perimetro(self) -> float:
        try:
            if self.radio < 0:
                raise ValueError("El radio no puede ser negativo")
            return 2 * math.pi * self.radio
        except Exception as e:
            raise Exception(f"Error al calcular perímetro del círculo: {e}")

def main():
    try:
        # --- Pruebas con Enteros (Rectángulo) ---
        print("--- Rectángulo (Enteros) ---")
        rect_int = Rectangulo[int](10, 5)
        print(f"Base: {rect_int.base}, Altura: {rect_int.altura}")
        print("Área: ", rect_int.area())
        print("Perímetro: ", rect_int.perimetro())
        print()

        # --- Pruebas con Flotantes (Círculo) ---
        print("--- Círculo (Flotantes) ---")
        circ_float = Circulo[float](5.5)
        print(f"Radio: {circ_float.radio}")
        print("Área: ", "{:.2f}".format(circ_float.area()))
        print("Perímetro: ", "{:.2f}".format(circ_float.perimetro()))
        
    except Exception as error:
        print(f"Ocurrió un error en la ejecución principal: {error}")

if __name__ == "__main__":
    main()
