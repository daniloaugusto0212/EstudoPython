class Carro():
    """"
    Essa é a classe carro. Esta classe é utilizada para instanciar novos carrso em nosso programa
    """
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia, qtd_combustivel, is_ligado, velocidade):
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = qtd_combustivel
        self.is_ligado = is_ligado
        self.velocidade = velocidade

    def abastecer(self, qtd_combustivel):
        """"O método abastecer recebe como parâmetro a quantidade de combustível e incrementa no atributo qtd_combustível"""
        self.qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.is_ligado == False:
            self.is_ligado = True
            print("O carro foi ligado!")
        else:
            print("O carro já está ligado!")

    def desligar(self):
        if self.is_ligado:
            self.is_ligado = False
            print("O carro foi desligado!")
        else:
            print("O carro já está desligado!")

    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print("Você precisa ligar o carro antes de acelerar")