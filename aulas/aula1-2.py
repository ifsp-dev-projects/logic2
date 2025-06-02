#exercicio: crie uma superclasse chamada funcionário com os atributos nome e salário base e o método calcular_salario(). crie uma subclasse gerente com o atributo bonus e uma segunda subclasse chamada vendedor com atributos comissão e vendas e uma terceira subclasse chamada desenvolvedor com atributo0 nível e experiencia
#implemente o metodo calcular_salario() de forma diferente em cada subclasse considerando seus atributos especificos

class Funcionario:
    def __init__ (self, nome, salario):
        self.nome=nome
        self.salario=salario
    def calcular_salario(self):
        print("salario")
class Gerente(Funcionario):
    def __init__ (self,nome, salario, bonus):
        self.bonus=bonus
        self.nome=nome
        self.salario=salario
    def calcular_salario(self):
        print(self.salario+self.bonus)
class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao, vendas):
        self.nome=nome
        self.salario=salario
        self.comissao=comissao
        self.vendas=vendas
    def calcular_salario(self):
        print(self.salario+self.comissao+self.vendas)
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, nivel, experiencia):
        self.nivel=nivel
        self.experiencia=experiencia
        self.nome=nome
        self.salario=salario
    def calcular_salario(self):
        print(self.salario)

gerente_1=Gerente("Eduardo", 2000, 300)
gerente_1.calcular_salario()

vendedor_1=Vendedor("Guilherme", 2000, 700, 200)
vendedor_1.calcular_salario()

desenvolvedor_1=Desenvolvedor("Heloisa", 5000, "alto", "média")
desenvolvedor_1.calcular_salario()

#adicionar nome no print!