class ConversorTemperatura:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    @staticmethod
    def celsius_a_fahrenheit(c):
        return (c * 9/5) + 32

    @classmethod
    def desde_celsius(cls, c):
        f = cls.celsius_a_fahrenheit(c)
        return cls(f)

temp_obj = ConversorTemperatura.desde_celsius(25)
print(f"Objeto creado con temperatura en F: {temp_obj.fahrenheit}")

f_calc = ConversorTemperatura.celsius_a_fahrenheit(0)
print(f"0°C en Fahrenheit es: {f_calc}")
