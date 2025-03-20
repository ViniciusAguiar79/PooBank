from Cliente import Cliente
from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

class Cadastro(Cliente):
    def __init__(self, nome, cpf, RG, endereco, dataNascimento, email, senha, cargo, tipo_usuario="cliente"):
        super().__init__(nome, cpf, RG, endereco, dataNascimento, cargo, telefone=None, email=email)
        self.__senha = senha
        self.__contas = []
        self.__tipo_usuario = tipo_usuario

    def getSenha(self):
        return self.__senha

    def setSenha(self, newPass):
        self.__senha = newPass
    
    def getTipoUsuario(self):
        return self.__tipo_usuario
    
    def abrirConta(self, tipo_conta, saldo_inicial=0):
        if tipo_conta.lower() == "corrente":
            nova_conta = ContaCorrente(self, self.getId(), saldo_inicial)
        elif tipo_conta.lower() == "poupanca":
            nova_conta = ContaPoupanca(self, self.getId(), saldo_inicial)
        else:
            return "Tipo de conta inválido!"
        
        self.__contas.append(nova_conta)
        return f"Conta {tipo_conta} aberta com sucesso!"
    
    def listarContas(self):
        return "\n".join([str(conta) for conta in self.__contas]) if self.__contas else "Nenhuma conta cadastrada."
    
    def login(self, email, senha):
        if self.getEmail() == email and self.__senha == senha:
            return f"Login bem-sucedido! Tipo de usuário: {self.__tipo_usuario}"
        return "Credenciais incorretas!"
