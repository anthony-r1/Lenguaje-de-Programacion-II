def generar_fibonacci(n):
    
    if n <= 0:
        print("La cantidad de términos debe ser un número positivo mayor que cero.")
        return

    a = 0
    b = 1

    print("Serie de Fibonacci:")
    
    print(a)
    
    if n > 1:
        print(b)

    for i in range(3, n + 1):
        siguiente_termino = a + b
        print(siguiente_termino)
        
        a = b
        b = siguiente_termino


def main():
    try:
        n_terminos = float(input("Ingrese la cantidad de términos de Fibonacci a generar: "))
        
        if n_terminos != int(n_terminos) or n_terminos <= 0:
            raise ValueError("Debe ingresar un número entero positivo (ej: 10).")
        
        generar_fibonacci(int(n_terminos))

    except ValueError as ve:
        print("Error:", ve)
        
    except Exception as e:
        print("Ocurrió un problema inesperado:", e)

if __name__ == "__main__":
    main()
