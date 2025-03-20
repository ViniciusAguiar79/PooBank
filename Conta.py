from Cliente import Cliente

class Conta:
    def __init__(self, cliente: Cliente, idConta, saldo, tipoConta):
        self.__cliente = cliente
        self.__idConta = idConta
        self.__saldo = saldo
        self.__tipoConta = tipoConta
        self.__historico = []

    def getCliente(self):
        return self.__cliente
    
    def getId(self):
        return self.__idConta
    
    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, newSaldo):
        self.__saldo = newSaldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__historico.append(f"Depósito de R$ {valor:.2f}")
            return f"Depósito de R$ {valor:.2f} realizado."
        return "Valor inválido."

    def sacar(self, valor):
        if valor > self.__saldo:
            return "Saldo insuficiente."
        if valor > 0:
            self.__saldo -= valor
            self.__historico.append(f"Saque de R$ {valor:.2f}")
            return f"Saque de R$ {valor:.2f} realizado."
        return "Valor inválido."

    def __str__(self):
        return f"Conta {self.__idConta} - {self.__tipoConta}, Saldo: R$ {self.__saldo:.2f}"
