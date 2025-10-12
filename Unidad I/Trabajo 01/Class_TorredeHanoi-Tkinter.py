import tkinter as tk
from tkinter import messagebox
import time


class TorresDeHanoi:
    """
    Clase para resolver el problema de las Torres de Hanoi
    con visualización gráfica usando Tkinter
    """
    
    def __init__(self, num_discos, canvas, ventana):
        """
        Constructor que inicializa las torres y la interfaz gráfica
        
        Args:
            num_discos (int): Número de discos
            canvas (tk.Canvas): Canvas de Tkinter para dibujar
            ventana (tk.Tk): Ventana principal de Tkinter
        """
        self.num_discos = num_discos
        self.canvas = canvas
        self.ventana = ventana
        
        # Inicializar las tres torres (listas)
        # Torre 1 tiene todos los discos (de mayor a menor)
        self.torres = {
            1: list(range(num_discos, 0, -1)),
            2: [],
            3: []
        }
        
        # Configuración gráfica
        self.ancho_canvas = 800
        self.alto_canvas = 400
        self.base_y = 350
        self.torre_x = {1: 150, 2: 400, 3: 650}
        self.altura_disco = 20
        self.ancho_disco_base = 150
        self.movimientos = 0
        
        # Dibujar estado inicial
        self.dibujar_torres()
    
    def dibujar_torres(self):
        """
        Dibuja el estado actual de las torres en el canvas
        """
        self.canvas.delete("all")
        
        # Dibujar bases y postes
        for i in range(1, 4):
            x = self.torre_x[i]
            # Poste
            self.canvas.create_rectangle(
                x - 5, self.base_y - 200, x + 5, self.base_y,
                fill="brown", outline="black"
            )
            # Base
            self.canvas.create_rectangle(
                x - 100, self.base_y, x + 100, self.base_y + 10,
                fill="saddlebrown", outline="black"
            )
            # Etiqueta de torre
            self.canvas.create_text(
                x, self.base_y + 30,
                text=f"Torre {i}",
                font=("Arial", 14, "bold")
            )
        
        # Dibujar discos
        colores = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
        
        for torre_num, discos in self.torres.items():
            x_torre = self.torre_x[torre_num]
            for idx, disco in enumerate(discos):
                # Calcular ancho del disco proporcionalmente
                ancho = (disco * self.ancho_disco_base) // self.num_discos
                y_pos = self.base_y - (idx + 1) * self.altura_disco
                
                color = colores[(disco - 1) % len(colores)]
                
                self.canvas.create_rectangle(
                    x_torre - ancho // 2, y_pos,
                    x_torre + ancho // 2, y_pos + self.altura_disco,
                    fill=color, outline="black", width=2
                )
                
                # Número del disco
                self.canvas.create_text(
                    x_torre, y_pos + self.altura_disco // 2,
                    text=str(disco),
                    font=("Arial", 10, "bold"),
                    fill="white"
                )
    
    def mover_disco(self, origen, destino):
        """
        Mueve el disco superior de una torre a otra
        
        Args:
            origen (int): Torre de origen (1, 2 o 3)
            destino (int): Torre de destino (1, 2 o 3)
        """
        if self.torres[origen]:
            disco = self.torres[origen].pop()
            self.torres[destino].append(disco)
            self.movimientos += 1
    
    def mostrar_estado(self):
        """
        Muestra el estado actual de las torres en consola
        """
        print(f"\nMovimiento #{self.movimientos}")
        print(f"Torre 1: {self.torres[1]}")
        print(f"Torre 2: {self.torres[2]}")
        print(f"Torre 3: {self.torres[3]}")
    
    def resolver(self, n, origen, destino, auxiliar):
        """
        Método recursivo que resuelve el problema de las Torres de Hanoi
        
        Args:
            n (int): Número de discos a mover
            origen (int): Torre de origen
            destino (int): Torre de destino
            auxiliar (int): Torre auxiliar
        """
        if n > 0:
            # Mover n-1 discos de origen a auxiliar usando destino
            self.resolver(n - 1, origen, auxiliar, destino)
            
            # Mover el disco más grande de origen a destino
            self.mover_disco(origen, destino)
            self.mostrar_estado()
            self.dibujar_torres()
            self.ventana.update()
            time.sleep(0.5)  # Pausa para visualizar el movimiento
            
            # Mover n-1 discos de auxiliar a destino usando origen
            self.resolver(n - 1, auxiliar, destino, origen)
    
    def iniciar_resolucion(self):
        """
        Inicia el proceso de resolución del problema
        """
        self.movimientos = 0
        print(f"\n{'=' * 50}")
        print(f"Resolviendo Torres de Hanoi con {self.num_discos} discos")
        print(f"{'=' * 50}")
        self.resolver(self.num_discos, 1, 3, 2)
        messagebox.showinfo(
            "¡Completado!",
            f"Torres de Hanoi resueltas en {self.movimientos} movimientos"
        )


def crear_interfaz():
    """
    Crea la interfaz gráfica con Tkinter
    """
    ventana = tk.Tk()
    ventana.title("Torres de Hanoi - Visualización")
    ventana.geometry("820x550")
    ventana.resizable(False, False)
    
    # Frame superior para controles
    frame_control = tk.Frame(ventana, bg="lightgray", height=80)
    frame_control.pack(fill=tk.X, padx=10, pady=10)
    
    # Etiqueta
    label = tk.Label(
        frame_control,
        text="Torres de Hanoi - Solución Recursiva",
        font=("Arial", 16, "bold"),
        bg="lightgray"
    )
    label.pack(pady=5)
    
    # Canvas para dibujar las torres
    canvas = tk.Canvas(ventana, width=800, height=450, bg="white")
    canvas.pack(padx=10, pady=5)
    
    # Variable para almacenar el objeto TorresDeHanoi
    torres_obj = None
    
    def iniciar():
        """Función para iniciar la resolución"""
        nonlocal torres_obj
        try:
            num_discos = int(entry_discos.get())
            if num_discos < 1 or num_discos > 8:
                messagebox.showerror("Error", "Ingrese un número entre 1 y 8")
                return
            
            btn_iniciar.config(state=tk.DISABLED)
            entry_discos.config(state=tk.DISABLED)
            
            # Crear objeto y resolver
            torres_obj = TorresDeHanoi(num_discos, canvas, ventana)
            torres_obj.iniciar_resolucion()
            
            btn_iniciar.config(state=tk.NORMAL)
            entry_discos.config(state=tk.NORMAL)
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")
    
    # Controles
    frame_input = tk.Frame(frame_control, bg="lightgray")
    frame_input.pack()
    
    tk.Label(
        frame_input,
        text="Número de discos:",
        font=("Arial", 12),
        bg="lightgray"
    ).pack(side=tk.LEFT, padx=5)
    
    entry_discos = tk.Entry(frame_input, width=5, font=("Arial", 12))
    entry_discos.insert(0, "4")
    entry_discos.pack(side=tk.LEFT, padx=5)
    
    btn_iniciar = tk.Button(
        frame_input,
        text="Resolver",
        command=iniciar,
        font=("Arial", 12, "bold"),
        bg="green",
        fg="white",
        padx=20
    )
    btn_iniciar.pack(side=tk.LEFT, padx=10)
    
    # Dibujar estado inicial con 4 discos
    torres_inicial = TorresDeHanoi(4, canvas, ventana)
    
    ventana.mainloop()


# Ejecutar la aplicación
if __name__ == "__main__":
    crear_interfaz()