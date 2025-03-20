from Cadastro import Cadastro
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from Adm import Adm

class PooBank:
    def __init__(self):
        self.clientes = []
        self.administradores = []

    def menu_principal(self):
        while True:
            print("\n===== Bem-vindo ao POO Bank =====")
            print("1. Cadastrar Cliente")
            print("2. Login")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_cliente()
            elif opcao == "2":
                self.login()
            elif opcao == "3":
                print("Obrigado por usar o POO Bank. Até mais!")
                break
            else:
                print("Opção inválida, tente novamente.")

    def cadastrar_cliente(self):
        print("\n===== Cadastro de Cliente =====")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        rg = input("RG: ")
        endereco = input("Endereço: ")
        data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
        email = input("E-mail: ")
        senha = input("Senha: ")
        cargo = input("Cargo (cliente/adm): ").strip().lower()

        if cargo == "adm":
            admin = Adm(nome, cpf, rg, endereco, data_nascimento, email, senha)
            self.administradores.append(admin)
            print("Administrador cadastrado com sucesso!")
        else:
            cliente = Cadastro(nome, cpf, rg, endereco, data_nascimento, email, senha, cargo="Cliente")
            self.clientes.append(cliente)
            print("Cliente cadastrado com sucesso!")

    def login(self):
        email = input("E-mail: ")
        senha = input("Senha: ")

        usuario = next((u for u in self.clientes + self.administradores if u.getEmail() == email and u.getSenha() == senha), None)

        if usuario:
            print("Login realizado com sucesso!")
            if isinstance(usuario, Adm):
                self.menu_admin(usuario)
            else:
                self.menu_cliente(usuario)
        else:
            print("E-mail ou senha inválidos.")

    def menu_cliente(self, cliente):
        while True:
            print(f"\n===== Menu Cliente ({cliente.getNome()}) =====")
            print("1. Abrir Conta")
            print("2. Listar Contas")
            print("3. Depositar")
            print("4. Sacar")
            print("5. Transferir")
            print("6. Extrato")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                tipo = input("Tipo de conta (corrente/poupanca): ").strip().lower()
                saldo_inicial = float(input("Saldo inicial: "))
                if tipo == "corrente":
                    cliente.abrirConta("corrente", saldo_inicial)
                elif tipo == "poupanca":
                    cliente.abrirConta("poupanca", saldo_inicial)
                else:
                    print("Opção inválida.")

            elif opcao == "2":
                print("\nContas do cliente:")
                print(cliente.listarContas())

            elif opcao == "3":
                valor = float(input("Valor do depósito: "))
                contas = cliente.getContas()
                if contas:
                    contas[0].depositar(valor)
                    print("Depósito realizado com sucesso!")
                else:
                    print("Nenhuma conta encontrada.")

            elif opcao == "4":
                valor = float(input("Valor do saque: "))
                contas = cliente.getContas()
                if contas:
                    print(contas[0].sacar(valor))
                else:
                    print("Nenhuma conta encontrada.")

            elif opcao == "5":
                valor = float(input("Valor da transferência: "))
                cpf_destino = input("CPF do destinatário: ")
                destinatario = next((c for c in self.clientes if c.getCPF() == cpf_destino), None)

                if destinatario:
                    contas_origem = cliente.getContas()
                    contas_destino = destinatario.getContas()

                    if contas_origem and contas_destino:
                        resultado = contas_origem[0].transferir(valor, contas_destino[0])
                        print(resultado)
                    else:
                        print("Uma das contas não foi encontrada.")
                else:
                    print("Cliente destinatário não encontrado.")

            elif opcao == "6":
                contas = cliente.getContas()
                if contas:
                    print(contas[0].gerarExtrato())
                else:
                    print("Nenhuma conta encontrada.")

            elif opcao == "7":
                print("Saindo do menu cliente...")
                break

            else:
                print("Opção inválida, tente novamente.")

    def menu_admin(self, admin):
        while True:
            print(f"\n===== Menu Administrador ({admin.getNome()}) =====")
            print("1. Aprovar Conta")
            print("2. Bloquear Conta")
            print("3. Listar Clientes")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cpf = input("Digite o CPF do cliente para aprovar a conta: ")
                cliente = next((c for c in self.clientes if c.getCPF() == cpf), None)
                if cliente:
                    print(admin.aprovarConta(cliente))
                else:
                    print("Cliente não encontrado.")

            elif opcao == "2":
                cpf = input("Digite o CPF do cliente para bloquear a conta: ")
                cliente = next((c for c in self.clientes if c.getCPF() == cpf), None)
                if cliente:
                    print(admin.bloquearConta(cliente))
                else:
                    print("Cliente não encontrado.")

            elif opcao == "3":
                print("\nLista de Clientes:")
                print(admin.listarClientes(self.clientes))

            elif opcao == "4":
                print("Saindo do menu administrador...")
                break

            else:
                print("Opção inválida, tente novamente.")

    def iniciar(self):
        self.menu_principal()

if __name__ == "__main__":
    banco = PooBank()
    banco.iniciar()
