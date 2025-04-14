#Aula 1: introdução à orientação a objetos: herança e polimorfismo. 14/04
#OO: um modelo que organiza o software em torno de "OBJETOS"; objetos combinam dados (atributos) e comportamentos (metodos); enfatiza a modularidade, reutilização e manutenbilidade.
#pilares: encapsulamento; herança; abstração; polimorfismo.
class Animal:
    def __init__ (self, nome, idade):
        self.nome=nome
        self.idade=idade
    def emitir_som (self):
        print("Som generico de animal")
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")
class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

meu_cachorro =Cachorro("Rex", 3)
meu_cachorro.emitir_som()

meu_gato=Gato("Rex", 3)
meu_gato.emitir_som()