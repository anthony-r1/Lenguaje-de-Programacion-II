from typing import TypeVar

T = TypeVar('T',int,float)

def suma (a:T,b:T)->T:
    return a+b

print(suma(5,10))
print(suma(3.5,2.5))
