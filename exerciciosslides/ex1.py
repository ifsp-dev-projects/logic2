import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

c1 = Circulo(2)
c2 = Circulo(5)

print(c1.calcular_area(), c1.calcular_perimetro())
print(c2.calcular_area(), c2.calcular_perimetro())
