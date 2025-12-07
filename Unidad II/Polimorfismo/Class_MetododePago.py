from abc import ABC, abstractmethod

# --- 1. CLASE BASE ABSTRACTA (Método Pago) ---

class MetodoPago(ABC):
    """
    Clase base abstracta que define la interfaz común para todos los métodos de pago.
    El método 'procesar_pago' debe ser implementado por todas las subclases.
    """
    
    @abstractmethod
    def procesar_pago(self, monto: float):
        """Método polimórfico para realizar el pago."""
        pass

# --- 2. SUBCLASES CON SOBREESCRITURA DE MÉTODOS ---

class Yape(MetodoPago):
    def __init__(self, numero_yape: str):
        self.numero_yape = numero_yape
        self.comision = 0.01  # 1% de comisión simulada

    def procesar_pago(self, monto: float):
        """Implementación de pago con Yape."""
        monto_final = monto * (1 + self.comision)
        print("-----------------------------------------")
        print(f"✅ Procesando pago con Yape a: {self.numero_yape}")
        print(f"Monto base: S/. {monto:.2f}")
        print(f"Comisión Yape ({self.comision*100:.0f}%): S/. {monto * self.comision:.2f}")
        print(f"Monto TOTAL cobrado: S/. {monto_final:.2f}")
        print("Estado: Pago con Yape Aceptado.")
        return True

class TarjetaDeCredito(MetodoPago):
    def __init__(self, numero_tarjeta: str):
        # En una aplicación real, no se almacenaría el número completo
        self.ultimos_digitos = numero_tarjeta[-4:]

    def procesar_pago(self, monto: float):
        """Implementación de pago con Tarjeta de Crédito."""
        referencia = "TRX-" + str(hash(monto) % 10000)
        print("-----------------------------------------")
        print(f"💳 Procesando pago con Tarjeta de Crédito (terminada en {self.ultimos_digitos})")
        print(f"Monto: S/. {monto:.2f}")
        print(f"Referencia de Transacción: {referencia}")
        print("Estado: Cargo a tarjeta realizado y verificado.")
        return True

class PayPal(MetodoPago):
    def __init__(self, correo: str):
        self.correo = correo

    def procesar_pago(self, monto: float):
        """Implementación de pago con PayPal."""
        print("-----------------------------------------")
        print(f"🌐 Procesando pago con PayPal al correo: {self.correo}")
        
        if monto > 1000:
            print("Estado: Pago pendiente de validación por monto alto.")
            return False # Simula que requiere validación extra
        else:
            print(f"Monto: USD {monto / 3.8:.2f} (Tasa simulada)")
            print("Estado: Pago con PayPal completado.")
            return True

class Efectivo(MetodoPago):
    def procesar_pago(self, monto: float):
        """Implementación de pago en Efectivo."""
        print("-----------------------------------------")
        print("💵 Procesando pago en Efectivo")
        print(f"Monto requerido: S/. {monto:.2f}")
        print("Instrucción: Se debe confirmar el pago al momento de la entrega.")
        print("Estado: Pago Pendiente de Recepción Física.")
        return True

# --- 3. FUNCIÓN DE PROCESAMIENTO CENTRAL Y DEMOSTRACIÓN ---

def realizar_pago(metodo: MetodoPago, monto: float):
    """
    Función Polimórfica: Llama al método procesar_pago sin saber
    qué clase específica lo implementará.
    """
    print(f"\n>>> Intento de Pago de S/. {monto:.2f} <<<")
    
    # Aquí ocurre el Polimorfismo: se llama al método correcto según el objeto
    metodo.procesar_pago(monto)

# --- DEMOSTRACIÓN ---

# Crear instancias de diferentes métodos de pago
pagos = [
    Yape("987654321"),
    TarjetaDeCredito("1234567890123456"),
    PayPal("cliente@ejemplo.com"),
    Efectivo()
]

# Simular pagos con diferentes montos
montos = [50.00, 1500.00, 200.00, 75.50]

for i, metodo in enumerate(pagos):
    realizar_pago(metodo, montos[i])