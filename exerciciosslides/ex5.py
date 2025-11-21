class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

    def latir(self):
        print("Woof woof!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

    def miar(self):
        print("Meow meow!")


salsicha = Cachorro("Bob")
linguica = Gato("Miau")

salsicha.emitir_som()
salsicha.latir()

linguica.emitir_som()
linguica.miar()

animais = [salsicha, linguica]
for animal in animais:
    animal.emitir_som()
