import veiculo

class Moto(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_passageiros):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_passageiros = qtd_passageiros

    def abastecer(self, qtd_combustivel):
        print("O método foi chamado através da classe moto")
        if self._qtd_combustivel >= 30:
            print("A moto está cheia")
        self._qtd_combustivel += qtd_combustivel

    def pintar(self, cor):
        if cor == "azul":
            print("A moto não pode ser azul")
        else:
            self._cor = cor
            print(f"A moto foi pintado de {self._cor}")
