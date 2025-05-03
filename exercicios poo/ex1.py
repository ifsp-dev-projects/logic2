#1. crie uma classe chamada "produtos" com os seguintes atributos: nome,preço e quantidade
#e os seguintes metodos: calcular_valortotal ( preço * qntdd)
#crie o metodo "atualizar qntdd" q recebe como parametro a nova qntdd

#objetivo: crie alguns objetos do tipo produto, calcule o valor total e o nova qntdd

#2.simule um carrinho de compras
#crie uma class "produto" e (se quiser)"carrinho de compras"
#dd ao carrinho os metodos "remover produto" e "valor total"

#3. cadastro de alunos com aluno, curso e turma e brincar c isso (adc, mudar)

class Produtos:
    def __init__ (self, nome, preço, quantidade):
        self.nome=nome
        self.preco=preço
        self.quantidade=quantidade
    def valor_total(self):
        return self.preco*self.quantidade
    def atualizar_quantidade(self, novaquantidade):
        self.quantidade=novaquantidade

class CarrinhodeCompras:
    def __init__(self):
        self.produtos=[]

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def removerProduto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                self.produtos.remove(produto)
                break

    def valorTotal(self):
        total=0
        for produto in self.produtos:
            total+= produto.valor_total()
        return total
    def listar_produtos(self):
        for produto in self.produtos:
            print("Produto: %s | Preço: R$ %.2f | Quantidade: %d" %
                  (produto.nome, produto.preco, produto.quantidade))

produto1=Produtos("camisa", 50, 2)
produto2=Produtos("calca", 100, 1)
produto3=Produtos("vestido",120,3)

carrinho=CarrinhodeCompras()
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)
carrinho.adicionar_produto(produto3)

carrinho.listar_produtos()

print("Valor total do carrinho: R$ %.2f" % carrinho.valorTotal())

carrinho.removerProduto("calca")
print("\nApós remover a Calça:")
carrinho.listar_produtos()
print("Valor total: R$ %.2f" % carrinho.valorTotal())