import random 
from datetime import datetime

class Cliente:
    def __init__(self, nome, cpf, RG, endereco, dataNascimento, cargo, telefone, email, status="Ativo"):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = RG
        self.__endereco = endereco
        self.__dataNascimento = dataNascimento
        self.__cargo = cargo
        self.__telefone = telefone
        self.__email = email
        self.__status = status
        self.__idConta = random.randint(1, 100000)
        self.__contas = []

    def getNome(self):
        return self.__nome
    
    def getCPF(self):
        return self.__cpf
    
    def getRG(self):
        return self.__rg
    
    def getEndereco(self):
        return self.__endereco
    
    def getDataNascimento(self):
        return self.__dataNascimento
    
    def getId(self):
        return self.__idConta
    
    def getTelefone(self):
        return self.__telefone
    
    def getEmail(self):
        return self.__email
    
    def getStatus(self):
        return self.__status
    
    def getContas(self):
        return self.__contas
    
    def setNome(self, newNome):
        self.__nome = newNome

    def setCPF(self, newCPF):
        self.__cpf = newCPF
    
    def setRG(self, newRG):
        self.__rg = newRG

    def setEndereco(self, newEndereco):
        self.__endereco = newEndereco

    def setDataNascimento(self, newDataNascimento):
        self.__dataNascimento = newDataNascimento
    
    def setTelefone(self, newTelefone):
        self.__telefone = newTelefone
    
    def setEmail(self, newEmail):
        self.__email = newEmail
    
    def setStatus(self, newStatus):
        self.__status = newStatus
    
    def ativarConta(self):
        self.__status = "Ativo"
    
    def desativarConta(self):
        self.__status = "Inativo"
    
    def adicionarConta(self, conta):
        self.__contas.append(conta)
    
    def listarContas(self):
        return [str(conta) for conta in self.__contas]
    
    def calcularIdade(self):
        data_nasc = datetime.strptime(self.__dataNascimento, "%d/%m/%Y")
        hoje = datetime.today()
        return hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
    
    def __str__(self):
        return f"Cliente {self.__nome} - CPF: {self.__cpf}, Email: {self.__email}"
