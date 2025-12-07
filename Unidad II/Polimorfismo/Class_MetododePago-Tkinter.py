import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod

# --- 1. CLASES DE PAGO (LÓGICA CENTRAL) ---

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> str:
        """Método polimórfico para realizar el pago, retorna un mensaje de estado."""
        pass

class Yape(MetodoPago):
    def __init__(self, numero_yape: str = "987654321"):
        self.numero_yape = numero_yape
        self.comision = 0.01

    def procesar_pago(self, monto: float) -> str:
        monto_final = monto * (1 + self.comision)
        
        return (f"✅ Pago con Yape a: {self.numero_yape}\n"
                f"Monto base: S/. {monto:.2f}\n"
                f"Comisión ({self.comision*100:.0f}%): S/. {monto * self.comision:.2f}\n"
                f"Monto TOTAL: S/. {monto_final:.2f}\n"
                f"Estado: Aceptado.")

class TarjetaDeCredito(MetodoPago):
    def __init__(self, ultimos_digitos: str = "3456"):
        self.ultimos_digitos = ultimos_digitos

    def procesar_pago(self, monto: float) -> str:
        referencia = "TRX-" + str(hash(monto) % 10000)
        
        return (f"💳 Pago con Tarjeta de Crédito (...{self.ultimos_digitos})\n"
                f"Monto: S/. {monto:.2f}\n"
                f"Referencia: {referencia}\n"
                f"Estado: Verificado y cargado.")

class PayPal(MetodoPago):
    def __init__(self, correo: str = "cliente@ejemplo.com"):
        self.correo = correo

    def procesar_pago(self, monto: float) -> str:
        if monto > 1000:
            return (f"🌐 Pago con PayPal: {self.correo}\n"
                    f"Monto: S/. {monto:.2f}\n"
                    f"Estado: PENDIENTE. Requiere validación por monto alto.")
        else:
            return (f"🌐 Pago con PayPal: {self.correo}\n"
                    f"Monto: S/. {monto:.2f}\n"
                    f"Estado: Completado.")

class Efectivo(MetodoPago):
    def procesar_pago(self, monto: float) -> str:
        return (f"💵 Pago en Efectivo\n"
                f"Monto requerido: S/. {monto:.2f}\n"
                f"Instrucción: Confirmar el recibo físico.\n"
                f"Estado: Pendiente de Recepción.")

# --- 2. APLICACIÓN TKINTER ---

class PagoApp:
    def __init__(self, master):
        self.master = master
        master.title("Simulador de Pagos Polimórfico")
        master.geometry("500x380")
        master.resizable(False, False)

        # Mapeo de nombres a clases para facilitar la instanciación
        self.pago_clases = {
            "Yape": Yape,
            "Tarjeta de Crédito": TarjetaDeCredito,
            "PayPal": PayPal,
            "Efectivo": Efectivo
        }
        
        self.monto_var = tk.DoubleVar(value=100.00)

        # --- Frames y Widgets ---
        main_frame = ttk.Frame(master, padding="15")
        main_frame.pack(fill='both', expand=True)

        # Título
        ttk.Label(main_frame, text="Sistema de Pagos Polimórfico", font=("Arial", 14, "bold"), foreground="#0056b3").pack(pady=10)

        # Entrada de Monto
        monto_frame = ttk.Frame(main_frame)
        monto_frame.pack(pady=5)
        ttk.Label(monto_frame, text="Monto a Pagar (S/):", font=("Arial", 10)).pack(side=tk.LEFT, padx=10)
        ttk.Entry(monto_frame, textvariable=self.monto_var, width=15, justify='right').pack(side=tk.LEFT)

        # Selección de Método
        pago_frame = ttk.Frame(main_frame)
        pago_frame.pack(pady=10)
        ttk.Label(pago_frame, text="Método de Pago:", font=("Arial", 10)).pack(side=tk.LEFT, padx=10)
        
        self.combo_metodo = ttk.Combobox(pago_frame, values=list(self.pago_clases.keys()), state="readonly", width=20)
        self.combo_metodo.set("Seleccione un método...")
        self.combo_metodo.pack(side=tk.LEFT)

        # Botón de Procesar
        ttk.Button(main_frame, text="Procesar Pago", command=self.procesar_pago_click, style="Accent.TButton").pack(pady=15)

        # Área de Resultados (usamos un Text para mostrar varias líneas)
        ttk.Label(main_frame, text="Resultado del Procesamiento:", font=("Arial", 10, "bold")).pack()
        self.resultado_text = tk.Text(main_frame, height=7, width=55, state=tk.DISABLED, relief=tk.GROOVE, bd=1, font=("Courier", 10))
        self.resultado_text.pack(pady=10)

    def actualizar_resultado(self, texto):
        """Habilita, inserta el texto y deshabilita el widget Text."""
        self.resultado_text.config(state=tk.NORMAL)
        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, texto)
        self.resultado_text.config(state=tk.DISABLED)

    def procesar_pago_click(self):
        """Manejador del botón que ejecuta el polimorfismo."""
        metodo_seleccionado = self.combo_metodo.get()
        
        try:
            monto = self.monto_var.get()
            
            if monto <= 0:
                messagebox.showwarning("Error", "Ingrese un monto positivo.")
                return
            
            if metodo_seleccionado not in self.pago_clases:
                messagebox.showwarning("Error", "Seleccione un método de pago válido.")
                return

            # 1. Instanciación Polimórfica (Se crea el objeto específico)
            # Usamos el diccionario para obtener la clase y la instanciamos
            ClasePago = self.pago_clases[metodo_seleccionado]
            metodo_obj = ClasePago() 
            
            # 2. Llamada Polimórfica (Se llama al método, y cada clase sabe cómo responder)
            # El método procesar_pago() de la clase específica se ejecuta aquí
            mensaje_resultado = metodo_obj.procesar_pago(monto)
            
            # 3. Mostrar resultado en la interfaz
            self.actualizar_resultado(mensaje_resultado)

        except ValueError:
            messagebox.showerror("Error de Entrada", "Asegúrese de que el monto sea un número.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")


def main():
    root = tk.Tk()
    app = PagoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()