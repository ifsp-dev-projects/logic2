class Calculadora:
    def somar(self,a,b,c=None):
        if c is None: #a variavel c existe? diferente de =
            return a+b
        else:
            return a+b+c
calc=Calculadora()
print(calc.somar(2,3)) #saida 5
print(calc.somar(2,3,4)) #saida 9