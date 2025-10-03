import tkinter as tk
from tkinter import messagebox

class Zodiaco:
    """Clase que determina el signo zodiacal basándose en el día y mes."""
    def __init__(self, dia, mes):
        self.dia = dia
        self.mes = mes

    def obtener_signo(self):
        # Primero, validar la fecha de forma simple (sin considerar días específicos por mes, 
        # ya que la lógica de tu código original maneja la mayoría de los límites)
        if self.mes < 1 or self.mes > 12 or self.dia < 1 or self.dia > 31:
            return "Fecha inválida"

        # Lógica de signos (copiada del código original)
        if (self.mes == 3 and 21 <= self.dia <= 31) or (self.mes == 4 and 1 <= self.dia <= 19):
            return "Aries ♈"
        elif (self.mes == 4 and 20 <= self.dia <= 30) or (self.mes == 5 and 1 <= self.dia <= 20):
            return "Tauro ♉"
        elif (self.mes == 5 and 21 <= self.dia <= 31) or (self.mes == 6 and 1 <= self.dia <= 20):
            return "Géminis ♊"
        elif (self.mes == 6 and 21 <= self.dia <= 30) or (self.mes == 7 and 1 <= self.dia <= 22):
            return "Cáncer ♋"
        elif (self.mes == 7 and 23 <= self.dia <= 31) or (self.mes == 8 and 1 <= self.dia <= 22):
            return "Leo ♌"
        elif (self.mes == 8 and 23 <= self.dia <= 31) or (self.mes == 9 and 1 <= self.dia <= 22):
            return "Virgo ♍"
        elif (self.mes == 9 and 23 <= self.dia <= 30) or (self.mes == 10 and 1 <= self.dia <= 22):
            return "Libra ♎"
        elif (self.mes == 10 and 23 <= self.dia <= 31) or (self.mes == 11 and 1 <= self.dia <= 21):
            return "Escorpio ♏"
        elif (self.mes == 11 and 22 <= self.dia <= 30) or (self.mes == 12 and 1 <= self.dia <= 21):
            return "Sagitario ♐"
        elif (self.mes == 12 and 22 <= self.dia <= 31) or (self.mes == 1 and 1 <= self.dia <= 19):
            return "Capricornio ♑"
        elif (self.mes == 1 and 20 <= self.dia <= 31) or (self.mes == 2 and 1 <= self.dia <= 18):
            return "Acuario ♒"
        elif (self.mes == 2 and 19 <= self.dia <= 29) or (self.mes == 3 and 1 <= self.dia <= 20):
            return "Piscis ♓"
        else:
            return "Fecha inválida (revisar día para el mes)"

class AppZodiaco(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Signo Zodiacal")
        self.geometry("350x250")
        self.config(padx=10, pady=10)

        # Variables de control para almacenar los datos de entrada y salida
        self.dia_var = tk.StringVar()
        self.mes_var = tk.StringVar()
        self.resultado_var = tk.StringVar(value="Ingresa tu fecha de nacimiento")

        self.crear_widgets()

    def crear_widgets(self):
        # Título
        tk.Label(self, text="¿Cuál es tu Signo Zodiacal?", font=('Arial', 14, 'bold')).pack(pady=10)

        # Contenedor para la entrada de datos
        input_frame = tk.Frame(self)
        input_frame.pack(pady=5)

        # Entrada del Día
        tk.Label(input_frame, text="Día:").grid(row=0, column=0, padx=5, sticky='w')
        tk.Entry(input_frame, textvariable=self.dia_var, width=10, justify='center').grid(row=0, column=1, padx=5)

        # Entrada del Mes
        tk.Label(input_frame, text="Mes (1-12):").grid(row=1, column=0, padx=5, sticky='w')
        tk.Entry(input_frame, textvariable=self.mes_var, width=10, justify='center').grid(row=1, column=1, padx=5)

        # Botón de Cálculo
        tk.Button(self, text="Calcular Signo", command=self.calcular_signo_gui, bg='#AEC6E3', font=('Arial', 10, 'bold')).pack(pady=15)

        # Resultado
        tk.Label(self, textvariable=self.resultado_var, font=('Arial', 12), fg='darkblue').pack(pady=10)

    def calcular_signo_gui(self):
        """Función que maneja la lógica de la GUI al presionar el botón."""
        try:
            # 1. Obtener y validar las entradas
            dia = int(self.dia_var.get())
            mes = int(self.mes_var.get())
            
            if not (1 <= mes <= 12 and 1 <= dia <= 31):
                messagebox.showerror("Error de Entrada", "Por favor, ingresa un día (1-31) y un mes válido (1-12).")
                self.resultado_var.set("Fecha inválida")
                return

            # 2. Crear instancia y realizar el cálculo
            persona = Zodiaco(dia, mes)
            signo = persona.obtener_signo()

            # 3. Mostrar el resultado en la GUI
            self.resultado_var.set(f"Tu signo es: {signo}")

        except ValueError:
            # Manejar el caso donde el usuario no ingresa números
            messagebox.showerror("Error de Entrada", "Solo se permiten números enteros para el día y el mes.")
            self.resultado_var.set("Error de entrada")
        except Exception as e:
            # Manejar cualquier otro error inesperado
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    app = AppZodiaco()
    app.mainloop()