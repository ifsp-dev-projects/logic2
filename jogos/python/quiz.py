#Crie um jogo de perguntas e respostas a partir de uma lista de questões com múltiplas alternativas (ou verdadeiro/falso). O sistema deve apresentar uma pergunta de cada vez, permitir que o usuário selecione uma resposta e, em seguida, informar se a resposta está correta, atualizando uma pontuação.
questionario={
    "questoes":["Qual o menor pais do mundo?", "Quantas casas decimais tem o pi?", "Quanto tempo a luz do Sol demora para chegar a Terra?", "Qual a montanha mais alta do mundo?", "Que pais tem o formato de uma bota?"], 
}
contador=0
alternativas={
    questionario["questoes"][0]: " a)Ilhas Marshall \n b) Nova Zelandia \n c)Monaco \n d) Vaticano",
    questionario["questoes"][1]: " a) 90 \n b) Infinitas \n c) 2 \n d) 687",
    questionario["questoes"][2]: " a) 8 minutos \n b) 8 segundos \n c) 3 minutos \n d) 1 segundo",
    questionario["questoes"][3]: " a) Monte Kangchenjunga \n b) Monte Godwin-Austen \n c) Monte Everest \n d) Monte Lhotse",
    questionario["questoes"][4]: " a) Italia \n b) Espanha \n c) Portugal \n d) Holanda", 
}

respostascertas={
    alternativas[questionario["questoes"][0]]: ["d)"],
    alternativas[questionario["questoes"][1]]: ["b)"],
    alternativas[questionario["questoes"][2]]: ["a)"],
    alternativas[questionario["questoes"][3]]: ["c)"],
    alternativas[questionario["questoes"][4]]: ["a)"],
}
pontuacao=0

while contador<len(questionario["questoes"]):
    for i in range (len(questionario["questoes"])):
        perguntadavez=questionario["questoes"][i]
        print(perguntadavez)
        print (alternativas[questionario["questoes"][i]])
        respostausuario=input("Digite sua resposta ( a), b), c) ou d) ): ")
        if respostausuario in respostascertas[alternativas[questionario["questoes"][i]]]:
            pontuacao+=1
            print ("Certa resposta!")
        else:
            print ("Você errou!")
        contador+=1
print("O quiz acabou!, Sua pontuação total foi:",pontuacao,"/5")