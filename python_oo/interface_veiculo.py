import abc

class InterfaceVeiculo(abc.ABC):
    @abc.abstractclassmethod
    def abastecer(self, qtd_combustivel):
        pass

    @abc.abstractclassmethod
    def ligar(self):
        pass

    @abc.abstractclassmethod
    def desligar(self):
        pass

    @abc.abstractclassmethod
    def acelerar(self, velocidade=10):
        pass

    @abc.abstractclassmethod
    def pintar(self, cor):
        pass
