#teste_class
class Computador:
    def __init__(self, marca, memoria, placa):
        self.marca = marca
        self.memoria = memoria
        self.placa = placa

    def ligar(self):
        print('Ligando computador...')

    def desliga(self):
        print('Desligando...')

    def exibe(self):
        print(self.marca, self.memoria, self.placa)


acessa = Computador('Asus', '16gb', 'Nvidia')
acessa.ligar()
acessa.exibe()
acessa.desliga()

