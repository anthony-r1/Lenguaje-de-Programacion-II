class TorresDeHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.torres = {
            1: list(range(num_discos, 0, -1)),
            2: [],
            3: []
        }
        self.movimientos = 0
        self.lista_movimientos = []
    
    def mover_disco(self, origen, destino):
        if self.torres[origen]:
            disco = self.torres[origen].pop()
            self.torres[destino].append(disco)
            self.movimientos += 1
            self.lista_movimientos.append((self.movimientos, origen, destino))
    
    def resolver(self, n, origen, destino, auxiliar):
        if n > 0:
            self.resolver(n - 1, origen, auxiliar, destino)
            self.mover_disco(origen, destino)
            self.resolver(n - 1, auxiliar, destino, origen)
    
    def mostrar_estado(self):
        print(f"Torre 1: {self.torres[1]}")
        print(f"Torre 2: {self.torres[2]}")
        print(f"Torre 3: {self.torres[3]}")
    
    def iniciar_resolucion(self):
        print(f"\n{'='*60}")
        print(f"TORRES DE HANOI - {self.num_discos} discos")
        print(f"{'='*60}\n")
        print("Estado inicial:")
        self.mostrar_estado()
        print()
        self.resolver(self.num_discos, 1, 3, 2)
        print(f"{'='*60}")
        print("MOVIMIENTOS REALIZADOS:")
        print(f"{'='*60}")
        for mov, origen, destino in self.lista_movimientos:
            print(f"Movimiento {mov}: Mover disco de Torre {origen} → Torre {destino}")
        print(f"\n{'='*60}")
        print(f"Estado final:")
        self.mostrar_estado()
        print(f"\n{'='*60}")
        print(f"Total de movimientos: {self.movimientos}")
        print(f"Fórmula: 2^{self.num_discos} - 1 = {2**self.num_discos - 1}")
        print(f"{'='*60}\n")

if __name__ == "__main__":
    torres = TorresDeHanoi(4)
    torres.iniciar_resolucion()
