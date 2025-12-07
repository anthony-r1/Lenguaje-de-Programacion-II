class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dividir(self):
        try:
            resultado = self.a / self.b
            return resultado
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero."
        except Exception as e:
            return f"Ocurrió un error: {e}"
        finally:
            print("Proceso de división concluido.")

valor_a = 10
valor_b = "cero"
operacion = Division(valor_a, valor_b)
print(f"Resultado de la operación: {operacion.dividir()}")
