#Isso é um teste de lista.

lista = ["Henrique", "Raphaelle", "Emanuelle"]

#estrutura
def busca():

    pesquisa = input("Pesquise o nome do convidado aqui:")

    if pesquisa in lista:
        print("OK")
        return busca()
    else:
        print("Convidado não está na lista.")
        return busca()

busca()