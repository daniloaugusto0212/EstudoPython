class Veiculo():
    """"
    Essa é a classe Veículo. Esta classe é utilizada para instanciar novos veiculos em nosso programa
    """
    def __init__(self, cor, tipo_combustivel, potencia):
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0
        self.is_ligado = False
        self.velocidade = 0

    def __del__(self):
        print('O objeto foi removido da memória.')

    def abastecer(self, qtd_combustivel):
        """"O método abastecer recebe como parâmetro a quantidade de combustível e incrementa no atributo qtd_combustível"""
        self.qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.qtd_combustivel <= 0:
            print('O veiculo não possui combustível, impossível ligar!')
        else:
            if self.is_ligado == False:
                self.is_ligado = True
                print("O veiculo foi ligado!")
            else:
                print("O veiculo já está ligado!")

    def desligar(self):
        if self.is_ligado:
            self.is_ligado = False
            print("O veiculo foi desligado!")
        else:
            print("O veiculo já está desligado!")

    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print("Você precisa ligar o veiculo antes de acelerar")