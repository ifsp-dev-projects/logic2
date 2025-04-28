class contaBancaria:
  def __init__ (self, saldo_inicial):
      self._saldo=saldo_inicial # convenção para atributo protegido
  def depositar (self, valor):
      if valor>0:
          self._saldo += valor
          print(f"Depósito de {valor}realizado. Saldo atual:{self._saldo}")
      else:
          print("valor de deposito invalido")
  def sacar(self, valor): 
    if (valor>0 and valor <= self._saldo):
        self._saldo-=valor
        print(f"saque de {valor} realizado. Saldo atual:{self._saldo}")
    else:
        print("saldo insuuficiente ou valor invalido")
  def get_saldo(self):
      return self._saldo

#criando um obj contabancaria
minha_conta=contaBancaria(1000)
#acessando o saldo atraves do metodo publico
print(f"saldo inicial:{minha_conta.get_saldo()}")
#realizando operações atraves dos metodos publicos
minha_conta.depositar(500)
minha_conta.sacar(200)
#tentativa de acesso direto ao atributo(convenção de "protegido")
#print(minha_conta._saldo) #evitar acessso fora de classe