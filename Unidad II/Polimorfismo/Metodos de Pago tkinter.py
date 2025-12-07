import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, Toplevel
from datetime import datetime
import ttkbootstrap as ttk
import pandas as pd
import hashlib
import os

# --- 1. CONFIGURACIÓN DE ARCHIVOS ---
EXCEL_FILE = "registro_prestamos.xlsx"
USERS_FILE = "usuarios.csv"

# --- 2. CLASES DE MÉTODOS DE PAGO (POLIMORFISMO) ---

class MetodoPago:
    """Clase base abstracta para todos los métodos de pago."""
    def pago(self):
        raise NotImplementedError("Subclases deben implementar este método")

class TarjetaCredito(MetodoPago):
    def pago(self):
        return "Tarjeta de Crédito", "Procesando pago con entidad bancaria..."

class Paypal(MetodoPago):
    def pago(self):
        return "Paypal", "Redirigiendo a la plataforma de PayPal..."

class Efectivo(MetodoPago):
    def pago(self):
        return "Efectivo", "Instrucciones: Recibir monto en caja y registrar en sistema."

class Yape(MetodoPago):
    def pago(self):
        qr_code_simulated = f"QR-YAPE-{datetime.now().strftime('%H%M%S')}"
        return "Yape (Pago Móvil)", f"Instrucciones: Escanee el código {qr_code_simulated} y confirme el monto."

METODOS_DISPONIBLES = {
    "Tarjeta de Crédito": TarjetaCredito(),
    "Paypal": Paypal(),
    "Efectivo": Efectivo(),
    "Yape": Yape(),
}

# --- 3. FUNCIONES DE GESTIÓN DE DATOS (EXCEL y USUARIOS) ---

def cargar_usuarios():
    if not os.path.exists(USERS_FILE):
        return pd.DataFrame(columns=['usuario', 'contrasena_hash'])
    try:
        df = pd.read_csv(USERS_FILE)
        return df
    except Exception:
        return pd.DataFrame(columns=['usuario', 'contrasena_hash'])

def registrar_usuario(usuario, contrasena):
    df_usuarios = cargar_usuarios()
    if usuario in df_usuarios['usuario'].values:
        return False
    contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()
    nuevo_usuario = pd.DataFrame([{'usuario': usuario, 'contrasena_hash': contrasena_hash}])
    df_actualizado = pd.concat([df_usuarios, nuevo_usuario], ignore_index=True)
    df_actualizado.to_csv(USERS_FILE, index=False)
    return True

def verificar_usuario(usuario, contrasena):
    df_usuarios = cargar_usuarios()
    if df_usuarios.empty:
        return False
    user_row = df_usuarios[df_usuarios['usuario'] == usuario]
    if not user_row.empty:
        contrasena_hash_ingresada = hashlib.sha256(contrasena.encode()).hexdigest()
        hash_almacenado = user_row.iloc[0]['contrasena_hash']
        return contrasena_hash_ingresada == hash_almacenado
    return False

def cargar_prestamos():
    try:
        return pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=[
            'ID Préstamo', 'Cliente', 'Monto', 'Fecha', 
            'Método Pago', 'Estado', 'Usuario Registrador'
        ])

def guardar_prestamo(data):
    df = cargar_prestamos()
    data['ID Préstamo'] = len(df) + 1
    df_new_row = pd.DataFrame([data])
    df = pd.concat([df, df_new_row], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False)
    return data['ID Préstamo']
    
def exportar_datos(filepath):
    df = cargar_prestamos()
    df.to_excel(filepath, index=False)
    return True

def importar_datos(filepath):
    df_imported = pd.read_excel(filepath)
    df_imported.to_excel(EXCEL_FILE, index=False)
    return len(df_imported)

# --- 4. CLASE PRINCIPAL DE LA APLICACIÓN (TKINTER) ---

class SistemaPrestamos:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Gestión de Préstamos")
        master.geometry("800x600")
        
        self.usuario_actual = None
        self.metodos_disponibles = list(METODOS_DISPONIBLES.keys())

        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(fill="both", expand=True)

        self.verificar_primer_uso()
        self.mostrar_login()

    def verificar_primer_uso(self):
        df_usuarios = cargar_usuarios()
        if df_usuarios.empty:
            messagebox.showwarning(
                "¡PRIMER USO!", 
                "No hay usuarios registrados. Por favor, haga clic en 'Registrar Nuevo Usuario' para comenzar."
            )

    def mostrar_login(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        login_frame = ttk.Frame(self.main_frame, padding=20, width=350, height=200)
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        ttk.Label(login_frame, text="INICIO DE SESIÓN", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        ttk.Label(login_frame, text="Usuario:", font=('Helvetica', 10)).pack(fill='x', pady=5)
        self.user_entry = ttk.Entry(login_frame, bootstyle="info")
        self.user_entry.pack(fill='x', pady=5)
        
        ttk.Label(login_frame, text="Contraseña:", font=('Helvetica', 10)).pack(fill='x', pady=5)
        self.pass_entry = ttk.Entry(login_frame, show='*', bootstyle="info")
        self.pass_entry.pack(fill='x', pady=5)
        
        ttk.Button(login_frame, text="Ingresar", command=self.login, bootstyle="success").pack(fill='x', pady=10)
        ttk.Button(login_frame, text="Registrar Nuevo Usuario", command=self.mostrar_registro, bootstyle="link").pack(fill='x')

    def login(self):
        usuario = self.user_entry.get()
        contrasena = self.pass_entry.get()

        if verificar_usuario(usuario, contrasena):
            self.usuario_actual = usuario
            messagebox.showinfo("Éxito", f"Bienvenido, {usuario}")
            self.mostrar_panel_principal()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas o usuario no registrado.")

    def mostrar_registro(self):
        usuario = simpledialog.askstring("Registro", "Ingrese el nuevo nombre de usuario:")
        if usuario:
            contrasena = simpledialog.askstring("Registro", "Ingrese la contraseña:", show='*')
            if contrasena:
                if registrar_usuario(usuario, contrasena):
                    messagebox.showinfo("Éxito", "Usuario registrado. Ya puede iniciar sesión.")
                else:
                    messagebox.showerror("Error", "El usuario ya existe.")

    def logout(self):
        self.usuario_actual = None
        messagebox.showinfo("Cierre de Sesión", "Sesión cerrada.")
        self.mostrar_login()

    def mostrar_panel_principal(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        top_frame = ttk.Frame(self.main_frame, padding=10, bootstyle="primary")
        top_frame.pack(fill='x')
        ttk.Label(top_frame, text="📊 Panel de Préstamos", font=('Helvetica', 18, 'bold'), bootstyle="inverse-primary").pack(side='left')
        ttk.Label(top_frame, text=f"Usuario: {self.usuario_actual}", bootstyle="inverse-primary").pack(side='right', padx=10)
        ttk.Button(top_frame, text="Salir", command=self.logout, bootstyle="danger-outline").pack(side='right')

        opciones_frame = ttk.Frame(self.main_frame, padding=10)
        opciones_frame.pack(fill='x')
        
        ttk.Button(opciones_frame, text="➕ Registrar Nuevo Préstamo", command=self.mostrar_formulario_registro, bootstyle="success").pack(side='left', padx=5)
        ttk.Button(opciones_frame, text="⬇️ Exportar Datos", command=self.exportar_datos_gui, bootstyle="warning-outline").pack(side='left', padx=5)
        ttk.Button(opciones_frame, text="⬆️ Importar Datos", command=self.importar_datos_gui, bootstyle="warning-outline").pack(side='left', padx=5)
        ttk.Button(opciones_frame, text="🔄 Recargar Tabla", command=self.actualizar_tabla, bootstyle="secondary-outline").pack(side='left', padx=5)

        self.tree = ttk.Treeview(self.main_frame, columns=('ID', 'Cliente', 'Monto', 'Fecha', 'Método', 'Estado'), show='headings', bootstyle="info")
        self.tree.heading('ID', text='ID')
        self.tree.heading('Cliente', text='Cliente')
        self.tree.heading('Monto', text='Monto (S/)')
        self.tree.heading('Fecha', text='Fecha')
        self.tree.heading('Método', text='Método Pago')
        self.tree.heading('Estado', text='Estado')

        self.tree.column('ID', width=50, anchor=tk.CENTER)
        self.tree.column('Monto', width=80, anchor=tk.E)
        self.tree.column('Fecha', width=100, anchor=tk.CENTER)
        self.tree.column('Método', width=120, anchor=tk.CENTER)
        self.tree.column('Estado', width=80, anchor=tk.CENTER)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.actualizar_tabla()

    def actualizar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        try:
            df = cargar_prestamos()
            for index, row in df.iterrows():
                self.tree.insert('', tk.END, values=(
                    row['ID Préstamo'],
                    row['Cliente'],
                    f"{row['Monto']:.2f}",
                    row['Fecha'],
                    row['Método Pago'],
                    row['Estado']
                ))
        except Exception as e:
             messagebox.showerror("Error de Datos", f"No se pudieron cargar los datos: {e}")

    # --- Funciones de Transacción y Ticket ---

    def mostrar_formulario_registro(self):
        # CORRECCIÓN DE ERROR: Creamos la ventana y luego aplicamos transient.
        top = Toplevel(self.master)
        top.transient(self.master) # <-- Corrección del error "-transient"
        top.title("Registrar Nuevo Préstamo") 
        top.geometry("400x450")
        top.grab_set()

        form_frame = ttk.Frame(top, padding=15)
        form_frame.pack(fill="both", expand=True)

        # Nombre del Cliente
        ttk.Label(form_frame, text="Nombre del Cliente:", font=('Helvetica', 10, 'bold')).pack(fill='x', pady=5)
        cliente_entry = ttk.Entry(form_frame, bootstyle="info")
        cliente_entry.pack(fill='x', pady=5)

        # Monto
        ttk.Label(form_frame, text="Monto (Soles):", font=('Helvetica', 10, 'bold')).pack(fill='x', pady=5)
        monto_entry = ttk.Entry(form_frame, bootstyle="info")
        monto_entry.pack(fill='x', pady=5)

        # Método de Pago
        ttk.Label(form_frame, text="Método de Pago:", font=('Helvetica', 10, 'bold')).pack(fill='x', pady=5)
        metodo_var = tk.StringVar(form_frame, value=self.metodos_disponibles[0])
        metodo_combo = ttk.Combobox(form_frame, textvariable=metodo_var, values=self.metodos_disponibles, bootstyle="info")
        metodo_combo.pack(fill='x', pady=5)
        
        # Área de Instrucciones (Se actualiza al cambiar el método de pago)
        ttk.Label(form_frame, text="Instrucciones de Pago:", font=('Helvetica', 10, 'bold')).pack(fill='x', pady=(15, 5))
        self.instruccion_text = tk.Text(form_frame, height=5, width=40, font=('Consolas', 9), relief=tk.FLAT, background=top.cget('bg'))
        self.instruccion_text.pack(fill='x', pady=5)
        self.instruccion_text.config(state=tk.DISABLED)


        def actualizar_instruccion(*args):
            metodo_nombre = metodo_var.get()
            
            if metodo_nombre in METODOS_DISPONIBLES:
                _, instruccion = METODOS_DISPONIBLES[metodo_nombre].pago()
            else:
                instruccion = "Método no reconocido."
            
            self.instruccion_text.config(state=tk.NORMAL)
            self.instruccion_text.delete('1.0', tk.END)
            self.instruccion_text.insert(tk.END, instruccion)
            self.instruccion_text.config(state=tk.DISABLED)

        metodo_combo.bind("<<ComboboxSelected>>", actualizar_instruccion)
        actualizar_instruccion() # Llama al inicio

        def registrar():
            try:
                cliente = cliente_entry.get().strip()
                monto = float(monto_entry.get())
                metodo_nombre = metodo_var.get()
                
                if not cliente or monto <= 0:
                    messagebox.showerror("Error de Datos", "Cliente y Monto deben ser válidos.")
                    return
                
                metodo_obj = METODOS_DISPONIBLES[metodo_nombre]
                pago_realizado, instruccion_final = metodo_obj.pago()

                data = {
                    'Cliente': cliente,
                    'Monto': monto,
                    'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M'),
                    'Método Pago': pago_realizado,
                    'Estado': 'Activo',
                    'Usuario Registrador': self.usuario_actual
                }

                id_prestamo = guardar_prestamo(data)
                
                self.generar_ticket(id_prestamo, data, instruccion_final)
                
                messagebox.showinfo("Registro Exitoso", f"Préstamo #{id_prestamo} registrado con {pago_realizado}.")
                self.actualizar_tabla()
                top.destroy()

            except ValueError:
                messagebox.showerror("Error", "El monto debe ser un número válido.")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al registrar: {e}")

        ttk.Button(form_frame, text="Confirmar Registro", command=registrar, bootstyle="primary").pack(fill='x', pady=15)

    def generar_ticket(self, id_prestamo, data, instruccion_final=""):
        ticket_window = Toplevel(self.master)
        ticket_window.title("TICKET DE PAGO")
        ticket_window.geometry("450x350")
        
        ticket_text = f"""
        ========================================
           TICKET DE REGISTRO DE PRÉSTAMO
        ========================================
        ID Transacción: {id_prestamo}
        Fecha y Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        Registrador: {self.usuario_actual}
        ----------------------------------------
        CLIENTE: {data['Cliente']}
        MONTO DEL PRÉSTAMO: S/ {data['Monto']:.2f}
        MÉTODO DE PAGO: {data['Método Pago']}
        ----------------------------------------
        INSTRUCCIÓN DE PAGO FINAL:
        {instruccion_final}
        
        ¡Operación Confirmada!
        ========================================
        """
        
        ticket_label = tk.Text(ticket_window, height=18, width=55, font=('Consolas', 10))
        ticket_label.insert(tk.END, ticket_text)
        ticket_label.config(state=tk.DISABLED)
        ticket_label.pack(padx=10, pady=10)

    def exportar_datos_gui(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Archivos Excel", "*.xlsx")],
            title="Exportar Datos de Préstamos"
        )
        if filepath:
            try:
                exportar_datos(filepath)
                messagebox.showinfo("Éxito", f"Datos exportados correctamente a:\n{filepath}")
            except Exception as e:
                messagebox.showerror("Error de Exportación", f"No se pudo exportar: {e}")

    def importar_datos_gui(self):
        filepath = filedialog.askopenfilename(
            defaultextension=".xlsx",
            filetypes=[("Archivos Excel", "*.xlsx")],
            title="Importar Datos de Préstamos"
        )
        if filepath:
            try:
                count = importar_datos(filepath)
                self.actualizar_tabla()
                messagebox.showinfo("Éxito", f"Se importaron {count} registros correctamente. Los datos actuales fueron reemplazados.")
            except Exception as e:
                messagebox.showerror("Error de Importación", f"No se pudo importar: {e}")
                
if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    app = SistemaPrestamos(root)
    root.mainloop()
