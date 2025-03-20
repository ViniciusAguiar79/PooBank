from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, cliente, idConta, saldo):
        super().__init__(cliente, idConta, saldo, "Poupança")
        self.__rendimento_mensal = 0.005
    
    def aplicarRendimento(self):
        rendimento = self.getSaldo() * self.__rendimento_mensal
        self.setSaldo(self.getSaldo() + rendimento)
        return f"Rendimento de R$ {rendimento:.2f} aplicado ao saldo."
