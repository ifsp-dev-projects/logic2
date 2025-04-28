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
    def valor_total(self, valor):
        return self.preco*self.quantidade
    def atualizar_quantidade(self, novaquantidade):
        novaquantidade=self.quantidade
produto1=Produtos("camisa", 50, 800)
print(produto1.valor_total())