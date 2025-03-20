from Conta import Conta
from CartaoCredito import CartaoCredito

class ContaCorrente(Conta):
    def __init__(self, cliente, idConta, saldo):
        super().__init__(cliente, idConta, saldo, "Corrente")
        self.__cartao = CartaoCredito(cliente)

    def getCartao(self):
        return self.__cartao
