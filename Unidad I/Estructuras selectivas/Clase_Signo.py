import tkinter as tk
from tkinter import ttk, messagebox

class Signo:
    def __init__(self, mes, dia):
        self.mes = mes
        self.dia = dia

    def zodiaco(self):
        if (self.mes == "Marzo" and self.dia >= 21 and self.dia <= 31) or (self.mes == "Abril" and self.dia <= 19 and self.dia > 0):
            return "♈ Aries"
        elif (self.mes == "Abril" and self.dia >= 20 and self.dia <= 30) or (self.mes == "Mayo" and self.dia <= 20 and self.dia > 0):
            return "♉ Tauro"
        elif (self.mes == "Mayo" and self.dia >= 21 and self.dia <= 31) or (self.mes == "Junio" and self.dia <= 20 and self.dia > 0):
            return "♊ Géminis"
        elif (self.mes == "Junio" and self.dia >= 21 and self.dia <= 30) or (self.mes == "Julio" and self.dia <= 22 and self.dia > 0):
            return "♋ Cáncer"
        elif (self.mes == "Julio" and self.dia >= 23 and self.dia <= 31) or (self.mes == "Agosto" and self.dia <= 22 and self.dia > 0):
            return "♌ Leo"
        elif (self.mes == "Agosto" and self.dia >= 23 and self.dia <= 31) or (self.mes == "Septiembre" and self.dia <= 22 and self.dia > 0):
            return "♍ Virgo"
        elif (self.mes == "Septiembre" and self.dia >= 23 and self.dia <= 30) or (self.mes == "Octubre" and self.dia <= 22 and self.dia > 0):
            return "♎ Libra"
        elif (self.mes == "Octubre" and self.dia >= 23 and self.dia <= 31) or (self.mes == "Noviembre" and self.dia <= 21 and self.dia > 0):
            return "♏ Escorpio"
        elif (self.mes == "Noviembre" and self.dia >= 22 and self.dia <= 30) or (self.mes == "Diciembre" and self.dia <= 21 and self.dia > 0):
            return "♐ Sagitario"
        elif (self.mes == "Diciembre" and self.dia >= 22 and self.dia <= 31) or (self.mes == "Enero" and self.dia <= 19 and self.dia > 0):
            return "♑ Capricornio"
        elif (self.mes == "Enero" and self.dia >= 20 and self.dia <= 31) or (self.mes == "Febrero" and self.dia <= 18 and self.dia > 0):
            return "♒ Acuario"
        elif (self.mes == "Febrero" and self.dia >= 19 and self.dia <= 29) or (self.mes == "Marzo" and self.dia <= 20 and self.dia > 0):
            return "♓ Piscis"
        else:
            return "Día invalido"


# ---------------- Tkinter UI ---------------- #

def calcular_signo():
    mes = combo_mes.get()
    try:
        dia = int(entry_dia.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese un día válido (número entero).")
        return

    if not mes:
        messagebox.showerror("Error", "Seleccione un mes de nacimiento.")
        return

    signo = Signo(mes, dia).zodiaco()
    label_resultado.config(text=f"Tu signo es:\n{signo}", foreground="#222", font=("Arial", 18, "bold"))

# Ventana principal
ventana = tk.Tk()
ventana.title("🌌 Calculadora de Signo Zodiacal")
ventana.geometry("450x400")
ventana.config(bg="#f0f4f7")

# Estilo moderno
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TLabel", font=("Arial", 12))

# Título
titulo = tk.Label(ventana, text="✨ Descubre tu Signo Zodiacal ✨", 
                  bg="#f0f4f7", fg="#444", font=("Arial", 16, "bold"))
titulo.pack(pady=15)

# Frame para inputs
frame = tk.Frame(ventana, bg="#f0f4f7")
frame.pack(pady=10)

# Mes
ttk.Label(frame, text="Mes: ").grid(row=0, column=0, padx=5, pady=5, sticky="e")
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
combo_mes = ttk.Combobox(frame, values=meses, state="readonly", font=("Arial", 12))
combo_mes.grid(row=0, column=1, padx=5, pady=5)

# Día
ttk.Label(frame, text="Día: ").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_dia = ttk.Entry(frame, font=("Arial", 12))
entry_dia.grid(row=1, column=1, padx=5, pady=5)

# Botón
btn_calcular = ttk.Button(ventana, text="🔮 Calcular Signo", command=calcular_signo)
btn_calcular.pack(pady=15)

# Resultado
label_resultado = tk.Label(ventana, text="", bg="#f0f4f7", fg="#333", font=("Arial", 14))
label_resultado.pack(pady=20)

# Loop
ventana.mainloop()