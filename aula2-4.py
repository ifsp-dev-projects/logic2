from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    @abstractmethod
    def calcular_perimetro(self):
        pass
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura=largura
        self.altura=altura
        def calcular_area(self):
            return self.largura+self.altura
        def calcular_perimetro(self):
            return 2+(self.largura+self.altura)
class Circulo(FormaGeometrica): #outra subclasse concreta
    def __init__(self, raio):
        self.raio=raio
    def calcular_area(self):
        import math
        return math.pi*self.raio **2
    def calcular_perimetro(self):
      import math
      return 2 *math.pi*self.raio
#n podemnos instanciar formageometrica diretamente
#froma=formageometrica(). Isso da erro

ret=Retangulo(5,10)
circ=Circulo(7)
print(f"area do retangulo:{ret.calcular_area()}")
print(f"perimetro do circulo:{circ.calcular_perimetro()}")