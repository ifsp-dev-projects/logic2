#O que define um item do cardápio: nome, descrição e preço
#O que precisa exibir: nome, descrição e preço

class ItemCardapio:
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
    
    def getnome(self):
        return self.nome
    
    def getdescricao(self):
        return self.descricao

    def getpreco(self):
        return self.preco

    def setnome(self, nvnome):
        self.nome = nvnome

    def setdescricao(self, nvdescricao):
        self.descricao = nvdescricao

    def setpreco(self, nvpreco):
        self.preco = nvpreco

    def exibir_detalhes(self):
        print (self.nome, ': ', self.descricao, ' - R$', self.preco)
    
class Cliente:
    def __init__(self, nome, numero, endereco):     
        self.nome = nome
        self.numero = numero
        self.endereco = endereco

    def getnome(self):
        return self.nome
    
    def getnumero(self):
        return self.numero

    def getendereco(self):
        return self.endereco

    def setnome(self, nvnome):
        self.nome = nvnome

    def setnumero(self, nvnumero):
        self.numero = nvnumero

    def setendereco(self, nvendereco):
        self.endereco = nvendereco

    def exibir_detalhes(self):
        print (self.nome, ' - ', self.numero, ' - ', self.endereco)

class Pedido():
    def __init__(self, cliente): 
        self.cliente = cliente
        self.itens_pedido = {}
        self.status = "Aberto"

    def adicionar_item(self, item, quantidade=1): 
        if item in self.itens_pedido:
            self.itens_pedido[item]+=quantidade
        else:
            self.itens_pedido[item]=quantidade

    def calcular_total(self):
        total=0
        for item, qtd in self.itens_pedido.items():
            total += item.getpreco()*qtd
        return total

    def exibir_resumo(self):
        self.cliente.exibir_detalhes()
        for item, qtd in self.itens_pedido.items():
            subtotal=item.getpreco()*qtd
            print(qtd, item.getnome(), ' - R$', item.getpreco(), "cada - Subtotal: R$", subtotal)
        print("Total: R$", self.calcular_total())
        print('Status: ', self.status) 
        
    def finalizar_pedido(self):
        self.status = 'Finalizado'

cardapio_lanchonete = []

xburger = ItemCardapio('X-Burger', 'Pão, queijo, picles, cebola, alface, carne', 15.00)
batatafrita = ItemCardapio('Batata frita', 'Batata, sal', 18.00)
refrigerantelata = ItemCardapio('Refrigerante', 'Lata, 300ml, Coca-Cola', 6.00)
suconatural = ItemCardapio('Suco', 'Natural, laranja, 200ml, com açúcar', 9.00)

cardapio_lanchonete = [xburger, batatafrita, refrigerantelata, suconatural]

nome_cliente=input("Olá! Para começar o pedido digite seu nome: ")
numero_cliente=input("Agora digite seu número:")
endereço_cliente=input("Por fim, digite o endereço de entrega:")
cliente1 = Cliente(nome_cliente, numero_cliente, endereço_cliente)
    
pedido1 = Pedido(cliente1)

print('Cardápio:')
for item in cardapio_lanchonete:
    item.exibir_detalhes()  

while(True):
    escolha = input("O que deseja (ex: 2 x-burger)? (para finalizar pedido, digite 1)").strip().lower() #strip e lower servem p comparar independente dfe ltras maiusculas e minusculas e de espaços.
    if escolha == '1':
        break
    try:
        partes=escolha.split(' ', 1)
        if len(partes)<2:
            raise ValueError
        qtd=int(partes[0])
        nome=partes[1].strip()
        encontrado=False
        for item in cardapio_lanchonete:
            if item.getnome().strip().lower()==nome:
                pedido1.adicionar_item(item)
                encontrado=True
                pedido1.exibir_resumo()
                break
        if not encontrado:
            print("Esse produto não está no cardápio") 
    except ValueError:
        print("Entrada inválida. Use o formato: (2 x-burger) ")

pedido1.finalizar_pedido()
pedido1.exibir_resumo()

#Cliente está sendo utilizado para fornecer alguns dados que são exibidos em exibir_resumo
#Item_cardapio fornece dados de 



