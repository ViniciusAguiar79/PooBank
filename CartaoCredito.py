from Cliente import Cliente

class CartaoCredito:
    def __init__(self, cliente: Cliente):
        self.__limite = self.calcularCredito(cliente.calcularIdade())
        self.__tarifaMensal = self.__limite * 0.005
        self.__fatura = 0
        self.__transacoes = []

    def calcularCredito(self, idade):
        if idade < 18:
            return 0
        elif idade <= 20:
            return 500
        else:
            return min(500 * (1.25 ** ((idade - 20) // 2)), 5500)

    def comprar(self, valor, descricao):
        if valor > (self.__limite - self.__fatura):
            return "Limite insuficiente."
        self.__fatura += valor
        self.__transacoes.append(f"Compra de R$ {valor:.2f} em {descricao}")
        return f"Compra de R$ {valor:.2f} realizada."
