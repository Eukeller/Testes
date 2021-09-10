def nomeia():
    pede = input("Digite seu nome:")
    vazio = ("")

    while(pede == vazio):
        print("Esse campo não pode ficar vazio.")
        return (nomeia())

    print("Olá", pede, "vamos prosseguir com o jogo.")

def opcoes():

    print("Opções: BLACKPINK e BTS.")
    resposta = input("Selecione uma opção para prosseguir:")

    blackpink = "YOU ARE BLINK"
    bts = "YOU ARE ARMY!"

    if(resposta.upper() == "BLACKPINK"):
        print(blackpink)
    elif(resposta.upper() == "BTS"):
        print(bts)

def mensagemInicio():
    print("BEM VINDOS!")

def mensagemFim():
    print("VEJO VOCÊS NA PRÓXIMA!")
    print("FIM DO PROGRAMA")

mensagemInicio()
nomeia()
opcoes()
mensagemFim()