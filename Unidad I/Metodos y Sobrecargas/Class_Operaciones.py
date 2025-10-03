class Operaciones:
    def Sumar(self,a,b,c=None):
        if c is not None:
            return a + b + c
        else :
            return a + b

operacion = Operaciones() 
sum_tres = operacion.Sumar(1, 2, 0)
print(sum_tres)
operacion1 = Operaciones() 
sum_dos = operacion1.Sumar(1, 2)
print(sum_dos)