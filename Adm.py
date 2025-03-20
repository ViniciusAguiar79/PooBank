from Cadastro import Cadastro

class Adm(Cadastro):
    def __init__(self, nome, cpf, RG, endereco, dataNascimento, email, senha):
        super().__init__(nome, cpf, RG, endereco, dataNascimento, email, senha, cargo="Administrador", tipo_usuario="admin")

    def aprovarConta(self, cliente):
        cliente.ativarConta()
        return f"Conta do cliente {cliente.getNome()} aprovada!"

    def bloquearConta(self, cliente):
        cliente.desativarConta()
        return f"Conta do cliente {cliente.getNome()} bloqueada!"

    def listarClientes(self, clientes):
        return "\n".join([str(cliente) for cliente in clientes]) if clientes else "Nenhum cliente cadastrado."

    def __str__(self):
        return f"Administrador {self.getNome()} - Email: {self.getEmail()}"
