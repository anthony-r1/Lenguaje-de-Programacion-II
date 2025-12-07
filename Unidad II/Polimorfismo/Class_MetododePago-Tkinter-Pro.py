#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Pagos PRO - Interfaz mejorada
Mantiene toda la funcionalidad original:
- Login / Registro de usuarios (usuarios.txt, ahora con hash SHA256)
- Procesamiento de pagos con métodos polimórficos (Yape, Tarjeta, PayPal, Efectivo)
- Persistencia en CSV (registros_pagos.csv)
- Exportar / Importar CSV
- Confirmar pagos en efectivo
- Generación de QR y ventana Voucher
- Interfaz más amigable / estilo dashboard
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import datetime
from abc import ABC, abstractmethod
import qrcode
from PIL import Image, ImageTk
import os
import shutil
import hashlib
from io import BytesIO

# -----------------------
# Configuración global UI
# -----------------------
APP_TITLE = "✅ Sistema de Pagos PRO | UNAP"
USERS_FILE = "usuarios.txt"
DATA_FILE = "registros_pagos.csv"
DEFAULT_FONT = ("Segoe UI", 10)
PRIMARY_COLOR = "#2563eb"
SUCCESS_COLOR = "#10b981"
WARNING_COLOR = "#f59e0b"
DANGER_COLOR = "#ef4444"
BG_COLOR = "#f3f6fb"
CARD_BG = "#ffffff"
ACCENT_TEXT = "#1e293b"

# -------------------------------------------------
# Utilidades: hashing, manejo CSV, validaciones
# -------------------------------------------------
def hash_password(password: str) -> str:
    """Genera SHA256 hex digest para la contraseña."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def users_from_file(path=USERS_FILE) -> dict:
    """
    Lee usuarios del archivo. Soporta contraseñas en texto plano (legacy)
    y en hash (64 hex chars). Devuelve dict usuario -> hashed_password_or_plain.
    """
    users = {}
    if not os.path.exists(path):
        return users
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if ':' in line:
                    u, p = line.strip().split(':', 1)
                    users[u] = p
    except Exception:
        return {}
    return users

def save_user(username: str, password: str, path=USERS_FILE):
    """
    Guarda usuario; siempre almacena el hash (migración de legacy).
    """
    try:
        phash = hash_password(password)
        # Append new user
        with open(path, 'a', encoding='utf-8') as f:
            f.write(f"{username}:{phash}\n")
        return True, None
    except Exception as e:
        return False, str(e)

def verify_user(username: str, password: str, path=USERS_FILE) -> bool:
    """
    Verifica usuario: si archivo contiene hash, lo compara; si contiene texto plano,
    compara en crudo (compatible con datos legacy) y en tal caso *migramos* guardando
    el hash del password para ese usuario.
    """
    users = users_from_file(path)
    if username not in users:
        return False
    stored = users[username]
    # si stored parece hash (64 hex chars) comparamos hashes
    if len(stored) == 64 and all(c in "0123456789abcdef" for c in stored.lower()):
        return stored == hash_password(password)
    # legacy: texto plano -> comparamos directamente; si coincide, migramos guardando hash
    if stored == password:
        # migrar: reescribir todo reemplazando usuario por hash
        try:
            users[username] = hash_password(password)
            # reescribir archivo
            with open(path, 'w', encoding='utf-8') as f:
                for u, p in users.items():
                    f.write(f"{u}:{p}\n")
        except Exception:
            pass
        return True
    return False

# CSV utilities
CSV_HEADER = ["Timestamp", "Nombre", "Documento", "Metodo", "Monto", "Estado"]

def ensure_data_file(path=DATA_FILE):
    """Asegura que exista el archivo CSV con encabezado correcto."""
    if not os.path.exists(path):
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADER)
    else:
        # validar header
        try:
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader, None)
                if header != CSV_HEADER:
                    # rehacer archivo con el encabezado y conservar registros si posible (si columnas coinciden)
                    # intentando leer y reescribir
                    rows = []
                    for row in reader:
                        if len(row) >= len(CSV_HEADER):
                            rows.append(row[:len(CSV_HEADER)])
                    with open(path, 'w', newline='', encoding='utf-8') as fw:
                        writer = csv.writer(fw)
                        writer.writerow(CSV_HEADER)
                        writer.writerows(rows)
        except Exception:
            # si falla, reescribimos un archivo nuevo
            with open(path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(CSV_HEADER)

def read_all_records(path=DATA_FILE) -> list:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception:
        return []

def write_all_records(records: list, path=DATA_FILE):
    try:
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
            writer.writeheader()
            writer.writerows(records)
            return True, None
    except Exception as e:
        return False, str(e)

def append_record(record: dict, path=DATA_FILE):
    """
    Agrega un registro *eficientemente* en modo append sin reescribir todo el CSV.
    record: dict con keys igual a CSV_HEADER
    """
    try:
        with open(path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
            writer.writerow(record)
        return True, None
    except Exception as e:
        return False, str(e)

def safe_float(value, default=0.0):
    try:
        return float(value)
    except Exception:
        return default

# --------------------------------------
# Clases de métodos de pago (Polimorfismo)
# --------------------------------------
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> tuple:
        """Retorna (mensaje, estado)"""
        pass

class Yape(MetodoPago):
    def procesar_pago(self, monto: float) -> tuple:
        monto_final = monto * 1.01
        return (f"Pago procesado: S/. {monto_final:.2f} (incluye 1% comisión)", "Completado")

class TarjetaDeCredito(MetodoPago):
    def procesar_pago(self, monto: float) -> tuple:
        ref = f"TC{abs(hash((monto, datetime.datetime.now()))) % 99999:05d}"
        return (f"Pago autorizado - Ref: {ref}", "Completado")

class PayPal(MetodoPago):
    def procesar_pago(self, monto: float) -> tuple:
        if monto > 1000:
            return ("Transacción en revisión por monto alto", "Pendiente")
        return (f"Pago procesado exitosamente", "Completado")

class Efectivo(MetodoPago):
    def procesar_pago(self, monto: float) -> tuple:
        return ("Pago registrado - Pendiente de confirmación", "Pendiente")

# ----------------------------
# Ventana Voucher (TopLevel)
# ----------------------------
class VoucherWindow(tk.Toplevel):
    def __init__(self, master, datos_voucher):
        super().__init__(master)
        self.title("Comprobante de Pago")
        self.geometry("480x560")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)
        self.transient(master)
        self.grab_set()
        # centrar
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (480 // 2)
        y = (self.winfo_screenheight() // 2) - (560 // 2)
        self.geometry(f"480x560+{x}+{y}")
        self._crear_interfaz(datos_voucher)

    def _crear_interfaz(self, datos):
        header = tk.Frame(self, bg=PRIMARY_COLOR, height=90)
        header.pack(fill='x')
        header.pack_propagate(False)
        tk.Label(header, text="COMPROBANTE DE PAGO", font=("Segoe UI", 14, "bold"), fg="white", bg=PRIMARY_COLOR).pack(pady=18)

        content = tk.Frame(self, bg=CARD_BG, padx=20, pady=15)
        content.pack(fill='both', expand=True, padx=20, pady=(10, 20))

        items = [
            ("Fecha y Hora:", datos.get('timestamp', '-')),
            ("Cliente:", datos.get('nombre', '-')),
            ("Documento:", datos.get('documento', '-')),
            ("Método de Pago:", datos.get('metodo', '-')),
            ("Monto:", f"S/. {float(datos.get('monto', 0)):.2f}"),
            ("Estado:", datos.get('estado', '-'))
        ]

        for label, value in items:
            row = tk.Frame(content, bg=CARD_BG)
            row.pack(fill='x', pady=6)
            tk.Label(row, text=label, font=("Segoe UI", 10, "bold"), bg=CARD_BG, fg="#475569").pack(side='left')
            # color especial para estado
            fg_color = SUCCESS_COLOR if label == "Estado:" and value == "Completado" else ACCENT_TEXT
            tk.Label(row, text=value, font=("Segoe UI", 10), bg=CARD_BG, fg=fg_color).pack(side='right')

        # separador
        ttk.Separator(content, orient='horizontal').pack(fill='x', pady=10)

        # QR
        qr_frame = tk.Frame(content, bg=CARD_BG)
        qr_frame.pack(fill='x', pady=10)
        if datos.get('qr_data'):
            try:
                qr_img = qrcode.make(datos['qr_data'])
                qr_img = qr_img.resize((170, 170), Image.Resampling.LANCZOS)
                self.qr_photo = ImageTk.PhotoImage(qr_img)
                tk.Label(qr_frame, image=self.qr_photo, bg=CARD_BG).pack()
            except Exception:
                tk.Label(qr_frame, text="QR no disponible", bg=CARD_BG, fg="#94a3b8").pack()
        else:
            tk.Label(qr_frame, text="Sin QR", bg=CARD_BG, fg="#94a3b8").pack()

        # Botones
        btns = tk.Frame(content, bg=CARD_BG)
        btns.pack(fill='x', pady=(12, 0))
        tk.Button(btns, text="📄 Imprimir", bg=PRIMARY_COLOR, fg="white", relief='flat', cursor="hand2",
                  command=lambda: messagebox.showinfo("Imprimir", "Comprobante enviado a impresora virtual")).pack(side='left', expand=True, padx=8, ipady=8)
        tk.Button(btns, text="Cerrar", bg="#64748b", fg="white", relief='flat', cursor="hand2", command=self.destroy).pack(side='right', expand=True, padx=8, ipady=8)

# ----------------------------
# Ventana de Login / Registro
# ----------------------------
class LoginWindow:
    def __init__(self, master, app_callback):
        self.master = master
        self.app_callback = app_callback
        master.title("Acceso - Sistema de Pagos")
        master.geometry("470x580")
        master.configure(bg=BG_COLOR)
        master.resizable(False, False)
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.mode = tk.StringVar(value="login")

        # Revisar si existe archivo usuarios
        initial = self._initial_state()
        if initial == 'register':
            self.mode.set('register')
        self._build_ui()
        if initial == 'register':
            messagebox.showwarning("Primer Acceso", "No hay usuarios registrados. Crea una cuenta de administrador.")

    def _initial_state(self):
        if not os.path.exists(USERS_FILE): return 'register'
        try:
            if os.path.getsize(USERS_FILE) == 0: return 'register'
        except Exception:
            return 'register'
        return 'login'

    def _build_ui(self):
        # panel lateral decorativo
        top = tk.Frame(self.master, bg=PRIMARY_COLOR, height=140)
        top.pack(fill='x')
        top.pack_propagate(False)
        tk.Label(top, text="🔐 Sistema de Pagos", bg=PRIMARY_COLOR, fg="white", font=("Segoe UI", 18, "bold")).pack(pady=20)

        card = tk.Frame(self.master, bg=CARD_BG, padx=24, pady=20)
        card.pack(padx=20, pady=20, fill='both', expand=True)

        # modo
        mode_frame = tk.Frame(card, bg=CARD_BG)
        mode_frame.pack(fill='x', pady=(0, 12))
        btn_login = tk.Button(mode_frame, text="Entrar", command=lambda: self.switch_mode('login'),
                              bg=PRIMARY_COLOR, fg="white", relief='flat', cursor="hand2")
        btn_register = tk.Button(mode_frame, text="Crear Cuenta", command=lambda: self.switch_mode('register'),
                                 bg="#e2e8f0", fg=ACCENT_TEXT, relief='flat', cursor="hand2")
        btn_login.pack(side='left', expand=True, fill='x', padx=(0, 6), ipady=8)
        btn_register.pack(side='left', expand=True, fill='x', padx=(6, 0), ipady=8)
        self.btn_login = btn_login
        self.btn_register = btn_register

        self.form = tk.Frame(card, bg=CARD_BG)
        self.form.pack(fill='both', expand=True)

        self._draw_form()

    def switch_mode(self, mode):
        self.mode.set(mode)
        self._draw_form()

    def _draw_form(self):
        for w in self.form.winfo_children():
            w.destroy()

        title = "Iniciar Sesión" if self.mode.get() == 'login' else "Crear Cuenta"
        action_text = "Acceder" if self.mode.get() == 'login' else "Registrar"
        btn_bg = PRIMARY_COLOR if self.mode.get() == 'login' else SUCCESS_COLOR

        # actualizar estado botones
        if self.mode.get() == 'login':
            self.btn_login.config(bg=PRIMARY_COLOR, fg="white")
            self.btn_register.config(bg="#e2e8f0", fg=ACCENT_TEXT)
        else:
            self.btn_register.config(bg=PRIMARY_COLOR, fg="white")
            self.btn_login.config(bg="#e2e8f0", fg=ACCENT_TEXT)

        tk.Label(self.form, text=title, font=("Segoe UI", 14, "bold"), bg=CARD_BG, fg=ACCENT_TEXT).pack(anchor='w', pady=(0, 12))
        # usuario
        tk.Label(self.form, text="Usuario", font=("Segoe UI", 9), bg=CARD_BG, fg="#64748b").pack(anchor='w')
        tk.Entry(self.form, textvariable=self.username_var, font=DEFAULT_FONT, relief='solid', bd=1).pack(fill='x', pady=(4, 10), ipady=8)
        # contraseña
        tk.Label(self.form, text="Contraseña", font=("Segoe UI", 9), bg=CARD_BG, fg="#64748b").pack(anchor='w')
        tk.Entry(self.form, textvariable=self.password_var, show="●", font=DEFAULT_FONT, relief='solid', bd=1).pack(fill='x', pady=(4, 14), ipady=8)

        # acción principal
        tk.Button(self.form, text=action_text, bg=btn_bg, fg="white", font=("Segoe UI", 11, "bold"),
                  relief='flat', cursor="hand2", command=self._attempt_action).pack(fill='x', ipady=10)

        # nota en registro
        if self.mode.get() == 'register':
            tk.Label(self.form, text="La contraseña debe tener al menos 4 caracteres.", font=("Segoe UI", 8), fg=WARNING_COLOR, bg=CARD_BG).pack(pady=(8, 0))

    def _attempt_action(self):
        user = self.username_var.get().strip()
        pwd = self.password_var.get().strip()
        if self.mode.get() == 'login':
            if not user or not pwd:
                messagebox.showwarning("Error", "Usuario y contraseña son obligatorios.")
                return
            ok = verify_user(user, pwd, USERS_FILE)
            if ok:
                # cierra ventana login y lanza app principal
                self.master.destroy()
                self.app_callback()
            else:
                messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos.")
                self.password_var.set("")
        else:
            # registro
            if not user or not pwd or len(pwd) < 4:
                messagebox.showerror("Error de registro", "Usuario y contraseña requeridos. Contraseña min 4 caracteres.")
                return
            users = users_from_file(USERS_FILE)
            if user in users:
                messagebox.showerror("Registro", f"El usuario '{user}' ya existe.")
                return
            ok, err = save_user(user, pwd, USERS_FILE)
            if ok:
                messagebox.showinfo("Registro", "Cuenta creada con éxito. Ya puedes iniciar sesión.")
                self.switch_mode('login')
                self.username_var.set("")
                self.password_var.set("")
            else:
                messagebox.showerror("Error", f"No se pudo crear el usuario: {err}")

# ----------------------------
# Aplicación Principal PagoApp
# ----------------------------
class PagoApp:
    def __init__(self, master):
        self.master = master
        master.title(APP_TITLE)
        master.geometry("1060x760")
        master.configure(bg=BG_COLOR)
        ensure_data_file(DATA_FILE)

        # variables
        self.nombre_var = tk.StringVar(value="")
        self.documento_var = tk.StringVar(value="")
        self.monto_var = tk.StringVar(value="50.00")
        self.metodo_seleccionado = tk.StringVar(value="Tarjeta de Crédito")

        self.pago_clases = {
            "Tarjeta de Crédito": TarjetaDeCredito, "Yape": Yape,
            "PayPal": PayPal, "Efectivo": Efectivo
        }

        self.figura_qr = None

        self._config_styles()
        self._build_ui()
        self.cargar_tabla_registros()

    def _config_styles(self):
        style = ttk.Style(self.master)
        # tema base
        try:
            style.theme_use('clam')
        except Exception:
            pass
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=28)
        # botón estilo (usaremos botones tk personalizados)
        # estilos adicionales si se desea

    def _build_ui(self):
        # Header
        header = tk.Frame(self.master, bg=PRIMARY_COLOR, height=72)
        header.pack(fill='x')
        header.pack_propagate(False)
        tk.Label(header, text="💳 Sistema de Pagos PRO", font=("Segoe UI", 18, "bold"), bg=PRIMARY_COLOR, fg="white").pack(side='left', padx=20)
        # acciones
        actions = tk.Frame(header, bg=PRIMARY_COLOR)
        actions.pack(side='right', padx=18)
        tk.Button(actions, text="📤 Exportar", bg="#0f172a", fg="white", relief='flat', cursor="hand2", command=self.exportar_registros).pack(side='left', padx=6, ipady=6)
        tk.Button(actions, text="📥 Importar", bg="#0f172a", fg="white", relief='flat', cursor="hand2", command=self.importar_registros).pack(side='left', padx=6, ipady=6)

        # main container
        main = tk.Frame(self.master, bg=BG_COLOR)
        main.pack(fill='both', expand=True, padx=18, pady=18)

        left = tk.Frame(main, bg=BG_COLOR, width=420)
        left.pack(side='left', fill='y', padx=(0, 12))
        left.pack_propagate(False)
        right = tk.Frame(main, bg=BG_COLOR)
        right.pack(side='right', fill='both', expand=True)

        self._build_left_panel(left)
        self._build_right_panel(right)

    def _build_left_panel(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, padx=18, pady=18, relief='raised', bd=1)
        card.pack(fill='both', expand=True)

        tk.Label(card, text="Nueva Transacción", font=("Segoe UI", 14, "bold"), bg=CARD_BG, fg=ACCENT_TEXT).pack(anchor='w')

        # cliente
        tk.Label(card, text="Nombre / Razón Social *", bg=CARD_BG, fg="#64748b").pack(anchor='w', pady=(10, 0))
        tk.Entry(card, textvariable=self.nombre_var, font=DEFAULT_FONT, relief='solid', bd=1).pack(fill='x', pady=(6, 8), ipady=8)

        tk.Label(card, text="DNI / RUC", bg=CARD_BG, fg="#64748b").pack(anchor='w')
        tk.Entry(card, textvariable=self.documento_var, font=DEFAULT_FONT, relief='solid', bd=1).pack(fill='x', pady=(6, 12), ipady=8)

        # monto
        tk.Label(card, text="Monto (S/) *", bg=CARD_BG, fg="#64748b").pack(anchor='w')
        tk.Entry(card, textvariable=self.monto_var, font=("Segoe UI", 14, "bold"), relief='solid', bd=1).pack(fill='x', pady=(6, 12), ipady=10)

        # metodos
        tk.Label(card, text="Método de Pago *", bg=CARD_BG, fg="#64748b").pack(anchor='w')
        metodo_frame = tk.Frame(card, bg=CARD_BG)
        metodo_frame.pack(fill='x', pady=(6, 12))
        opciones = ["Tarjeta de Crédito", "Yape", "PayPal", "Efectivo"]
        etiquetas = ["💳 Tarjeta", "📱 Yape", "🌐 PayPal", "💵 Efectivo"]
        for opt, et in zip(opciones, etiquetas):
            tk.Radiobutton(metodo_frame, text=et, variable=self.metodo_seleccionado, value=opt, bg=CARD_BG, anchor='w', font=DEFAULT_FONT, cursor="hand2").pack(side='left', padx=4)

        # botones
        tk.Button(card, text="PROCESAR PAGO", bg=PRIMARY_COLOR, fg="white", font=("Segoe UI", 11, "bold"),
                  relief='flat', cursor="hand2", command=self.procesar_pago_click).pack(fill='x', pady=(8, 8), ipady=10)

        # resultado
        self.resultado_frame = tk.Frame(card, bg=BG_COLOR, relief='solid', bd=1)
        self.resultado_frame.pack(fill='x', pady=(6, 8))
        self.resultado_label = tk.Label(self.resultado_frame, text="", bg=BG_COLOR, font=DEFAULT_FONT, wraplength=360, justify='center')
        self.resultado_label.pack(padx=6, pady=6)
        self.resultado_frame.pack_forget()

        # confirmar efectivo
        self.confirm_button = tk.Button(card, text="✓ CONFIRMAR PAGO EN EFECTIVO", bg=SUCCESS_COLOR, fg="white", relief='flat', cursor="hand2", command=self.confirmar_pago_efectivo)
        self.confirm_button.pack(fill='x', ipady=10, pady=(6, 0))
        self.confirm_button.pack_forget()

        # QR
        tk.Label(card, text="Código QR de Verificación", bg=CARD_BG, fg=ACCENT_TEXT, font=("Segoe UI", 11, "bold")).pack(pady=(12, 6))
        self.qr_canvas = tk.Canvas(card, width=200, height=200, bg="white", highlightthickness=0)
        self.qr_canvas.pack(pady=(0, 8))
        self.generar_qr_default()

    def _build_right_panel(self, parent):
        top = tk.Frame(parent, bg=CARD_BG, padx=16, pady=12, relief='raised', bd=1)
        top.pack(fill='x')
        tk.Label(top, text="Historial de Transacciones", font=("Segoe UI", 14, "bold"), bg=CARD_BG, fg=ACCENT_TEXT).pack(side='left')
        btns = tk.Frame(top, bg=CARD_BG)
        btns.pack(side='right')
        tk.Button(btns, text="🗑️ Eliminar Seleccionado", bg=DANGER_COLOR, fg="white", relief='flat', cursor="hand2", command=self.eliminar_seleccionado).pack(side='left', padx=6, ipady=6)
        tk.Button(btns, text="⚠️ Vaciar Todo", bg=WARNING_COLOR, fg="white", relief='flat', cursor="hand2", command=self.vaciar_registros).pack(side='left', padx=6, ipady=6)

        # tabla
        table_card = tk.Frame(parent, bg=CARD_BG, padx=12, pady=12, relief='raised', bd=1)
        table_card.pack(fill='both', expand=True, pady=(12, 0))

        vsb = ttk.Scrollbar(table_card, orient="vertical")
        hsb = ttk.Scrollbar(table_card, orient="horizontal")
        vsb.pack(side='right', fill='y')
        hsb.pack(side='bottom', fill='x')

        columns = ("ID", "Fecha/Hora", "Cliente", "Documento", "Método", "Monto", "Estado")
        self.tree = ttk.Treeview(table_card, columns=columns, show="headings", yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.config(command=self.tree.yview); hsb.config(command=self.tree.xview)

        # headings
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.column("ID", width=44, anchor='center')
        self.tree.column("Fecha/Hora", width=160, anchor='center')
        self.tree.column("Cliente", width=200, anchor='w')
        self.tree.column("Documento", width=110, anchor='center')
        self.tree.column("Método", width=110, anchor='center')
        self.tree.column("Monto", width=100, anchor='e')
        self.tree.column("Estado", width=100, anchor='center')

        self.tree.tag_configure('oddrow', background='#fbfdff')
        self.tree.tag_configure('evenrow', background='white')
        self.tree.tag_configure('completado', foreground=SUCCESS_COLOR)
        self.tree.tag_configure('pendiente', foreground=WARNING_COLOR)
        self.tree.tag_configure('rechazado', foreground=DANGER_COLOR)

        self.tree.pack(fill='both', expand=True)
        self.tree.bind('<Double-1>', self.ver_voucher_desde_tabla)

    # -------------------------
    # Operaciones sobre registros
    # -------------------------
    def cargar_tabla_registros(self):
        for it in self.tree.get_children():
            self.tree.delete(it)
        registros = read_all_records(DATA_FILE)
        # mostrar en orden inverso (último primero)
        for idx, row in enumerate(reversed(registros)):
            row_id = len(registros) - idx
            tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
            estado = row.get('Estado', '')
            if estado == 'Completado': estado_tag = 'completado'
            elif estado == 'Pendiente': estado_tag = 'pendiente'
            else: estado_tag = 'rechazado'
            monto_text = f"S/. {safe_float(row.get('Monto', '0')):.2f}"
            try:
                self.tree.insert('', tk.END, values=(row_id, row.get('Timestamp', ''), row.get('Nombre', ''), row.get('Documento', ''), row.get('Metodo', ''), monto_text, estado), tags=(tag, estado_tag))
            except Exception:
                continue

    def eliminar_seleccionado(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una fila para eliminar.")
            return
        item = self.tree.item(seleccion[0])
        row_id = item['values'][0]
        resp = messagebox.askyesno("Confirmar Eliminación", f"¿Eliminar la transacción ID {row_id}?")
        if not resp: return
        registros = read_all_records(DATA_FILE)
        index_to_delete = len(registros) - row_id
        if 0 <= index_to_delete < len(registros):
            del registros[index_to_delete]
            ok, err = write_all_records(registros, DATA_FILE)
            if ok:
                self.cargar_tabla_registros()
                messagebox.showinfo("Éxito", f"Transacción ID {row_id} eliminada.")
            else:
                messagebox.showerror("Error", f"No se pudo eliminar: {err}")
        else:
            messagebox.showerror("Error", "No se encontró el registro seleccionado.")

    def vaciar_registros(self):
        resp = messagebox.askyesno("Confirmar", "⚠️ ¿Eliminar TODO el historial? Esta acción no se puede deshacer.")
        if not resp: return
        try:
            write_all_records([], DATA_FILE)
            self.cargar_tabla_registros()
            messagebox.showinfo("Éxito", "Todos los registros han sido eliminados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo vaciar: {str(e)}")

    def exportar_registros(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], initialfile="historial_pagos_exportado.csv")
        if not path: return
        try:
            shutil.copy(DATA_FILE, path)
            messagebox.showinfo("Exportado", f"Historial exportado a:\n{path}")
        except Exception as e:
            messagebox.showerror("Error", f"Fallo al exportar: {str(e)}")

    def importar_registros(self):
        path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Selecciona CSV a importar")
        if not path: return
        resp = messagebox.askyesno("Confirmar Importación", "La importación reemplazará todo su historial. ¿Continuar?")
        if not resp: return
        try:
            shutil.copy(path, DATA_FILE)
            self.cargar_tabla_registros()
            messagebox.showinfo("Importado", "Historial importado con éxito.")
        except Exception as e:
            messagebox.showerror("Error", f"Fallo al importar: {str(e)}")

    # -------------------------
    # Lógica de pago
    # -------------------------
    def confirmar_pago_efectivo(self):
        registros = read_all_records(DATA_FILE)
        encontrado = False
        for i in range(len(registros) - 1, -1, -1):
            if registros[i].get('Metodo') == "Efectivo" and registros[i].get('Estado') == "Pendiente":
                registros[i]['Estado'] = "Completado"
                encontrado = True
                break
        if encontrado:
            ok, err = write_all_records(registros, DATA_FILE)
            if ok:
                self.confirm_button.config(state=tk.DISABLED)
                self.resultado_frame.pack(fill='x', pady=12)
                self.resultado_frame.config(bg="#d1fae5")
                self.resultado_label.config(text="✓ Pago en efectivo confirmado exitosamente", bg="#d1fae5", fg=SUCCESS_COLOR)
                self.cargar_tabla_registros()
                messagebox.showinfo("Confirmado", "El pago en efectivo ha sido confirmado.")
            else:
                messagebox.showerror("Error", f"No se pudo confirmar: {err}")
        else:
            messagebox.showwarning("Sin pendientes", "No hay pagos en efectivo pendientes.")
            self.confirm_button.config(state=tk.DISABLED)

    def procesar_pago_click(self):
        metodo = self.metodo_seleccionado.get()
        try:
            monto = safe_float(self.monto_var.get())
            nombre = self.nombre_var.get().strip()
            documento = self.documento_var.get().strip()
            if monto <= 0 or not nombre:
                messagebox.showwarning("Datos incompletos", "El monto debe ser positivo y el nombre es obligatorio.")
                return
            ClasePago = self.pago_clases.get(metodo, TarjetaDeCredito)
            metodo_obj = ClasePago()
            mensaje, estado = metodo_obj.procesar_pago(monto)

            # manejo boton confirmar efectivo
            if estado == "Completado":
                self.confirm_button.pack_forget()
            elif estado == "Pendiente" and metodo == "Efectivo":
                self.confirm_button.pack(fill='x', ipady=10, pady=(8, 0))
                self.confirm_button.config(state=tk.NORMAL)
            else:
                self.confirm_button.pack_forget()

            # guardar registro (append)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_rec = {"Timestamp": timestamp, "Nombre": nombre, "Documento": documento, "Metodo": metodo, "Monto": f"{monto:.2f}", "Estado": estado}
            ok, err = append_record(new_rec, DATA_FILE)
            if not ok:
                messagebox.showerror("Error", f"No se pudo guardar la transacción: {err}")
                return

            # actualizar interfaz
            self._actualizar_estado_interfaz(mensaje, estado)
            self.cargar_tabla_registros()

            # generar qr y voucher
            qr_data = f"CLIENTE:{nombre}|DOC:{documento}|TIPO:{metodo}|MONTO:{monto:.2f}|ESTADO:{estado}|TS:{timestamp}"
            self._generar_qr_imagen(qr_data)
            self.generar_voucher(nombre, documento, metodo, monto, estado, qr_data)

            # limpiar campos (opcional, pero útil)
            # mantener nombre para varias transacciones? aquí lo dejamos.
            # self.nombre_var.set("")
            self.monto_var.set("50.00")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    def _actualizar_estado_interfaz(self, mensaje, estado):
        self.resultado_frame.pack(fill='x', pady=12)
        if estado == "Completado":
            bg, fg = "#d1fae5", SUCCESS_COLOR
        elif estado == "Pendiente":
            bg, fg = "#fff7ed", WARNING_COLOR
        else:
            bg, fg = "#fee2e2", DANGER_COLOR
        self.resultado_frame.config(bg=bg)
        self.resultado_label.config(text=mensaje, bg=bg, fg=fg)

    def ver_voucher_desde_tabla(self, event):
        seleccion = self.tree.selection()
        if not seleccion:
            return
        item = self.tree.item(seleccion[0])
        vals = item['values']
        # vals: ID, Timestamp, Nombre, Documento, Metodo, Monto, Estado
        datos_voucher = {
            'timestamp': vals[1],
            'nombre': vals[2],
            'documento': vals[3],
            'metodo': vals[4],
            'monto': float(str(vals[5]).replace('S/. ', '').strip()) if vals[5] else 0.0,
            'estado': vals[6],
            'qr_data': f"TRANSACCION|Cliente:{vals[2]}|Doc:{vals[3]}|Metodo:{vals[4]}|Monto:{vals[5]}|Estado:{vals[6]}"
        }
        VoucherWindow(self.master, datos_voucher)

    def generar_voucher(self, nombre, documento, metodo, monto, estado, qr_data):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        datos = {'timestamp': timestamp, 'nombre': nombre, 'documento': documento, 'metodo': metodo, 'monto': monto, 'estado': estado, 'qr_data': qr_data}
        VoucherWindow(self.master, datos)

    # -------------------------
    # QR helpers
    # -------------------------
    def generar_qr_default(self):
        self._generar_qr_imagen("Sistema de Pagos UNAP | Listo")

    def _generar_qr_imagen(self, data):
        try:
            qr = qrcode.QRCode(version=1, box_size=8, border=2)
            qr.add_data(data)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="#0f172a", back_color="white")
            qr_img = qr_img.resize((200, 200), Image.Resampling.LANCZOS)
            self.figura_qr = ImageTk.PhotoImage(qr_img)
            self.qr_canvas.delete("all")
            self.qr_canvas.create_image(100, 100, image=self.figura_qr)
        except Exception:
            self.qr_canvas.delete("all")
            self.qr_canvas.create_text(100, 100, text="Error al generar QR", fill="#ef4444", font=("Segoe UI", 9))

# ----------------------------
# Inicializadores main
# ----------------------------
def main_app_initializer():
    root_app = tk.Tk()
    PagoApp(root_app)
    root_app.mainloop()

def main():
    # aseguramos archivos necesarios
    ensure_data_file(DATA_FILE)
    root_login = tk.Tk()
    LoginWindow(root_login, main_app_initializer)
    root_login.mainloop()

if __name__ == "__main__":
    main()
