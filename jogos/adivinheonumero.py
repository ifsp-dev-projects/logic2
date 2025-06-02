import random
numeroaleatorio=random.randint(1,100)
print("Regras: o usuário deve acertar o número aleatório, quando a diferença entre os números é menor ou igual a 10, eles estão próximos! Boa sorte!")
while True:
    numerousuario=int(input("Digite um numero aleatório: "))
    diferenca=numeroaleatorio-numerousuario
    if diferenca>=-10 and diferenca <=10 and numeroaleatorio != numerousuario:
        print("Quase lá")
    elif diferenca<=-10 and diferenca >=10:
        print("Longe")
    elif diferenca==0:
        print("Acertou!")
        break