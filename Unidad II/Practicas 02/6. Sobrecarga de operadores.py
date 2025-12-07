class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, escalar):
        return Vector2D(self.x * escalar, self.y * escalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector2D(2, 3)
v2 = Vector2D(1, 4)

print(f"Suma: {v1 + v2}")                  
print(f"Resta: {v1 - v2}")
print(f"Multiplicación : {v1 * 3}") 
