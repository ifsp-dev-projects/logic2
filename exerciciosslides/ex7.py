import math

class FormaGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(FormaGeometrica):
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def calcular_area(self):
        s = (self.l1 + self.l2 + self.l3) / 2
        return math.sqrt(s * (s - self.l1) * (s - self.l2) * (s - self.l3))

    def calcular_perimetro(self):
        return self.l1 + self.l2 + self.l3


formas = [
    Retangulo(3, 4),
    Triangulo(3, 4, 5)
]

for forma in formas:
    print("Área:", forma.calcular_area())
    print("Perímetro:", forma.calcular_perimetro())
    print("---")
