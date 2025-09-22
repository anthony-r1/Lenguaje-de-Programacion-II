class Calculadora:
    def suma(self, a, b):
        self.a = a  
        self.b = b 
        return self.a + self.b

calc = Calculadora()

suma = calc.suma(1, 3)

print(f"La suma de los parámetros {calc.a} y {calc.b} es: {suma}")