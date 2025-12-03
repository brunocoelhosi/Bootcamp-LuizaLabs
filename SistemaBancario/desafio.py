from dataclasses import dataclass

menu = """

[1] Criar Usuário
[2] Criar Conta
[3] Listar Contas
[4] Depositar
[5] Sacar
[6] Extrato
[0] Sair

=> """

AGENCIA = "0001"


@dataclass
class Usuario:
    nome: str
    nasc: str
    cpf: int
    end: str

@dataclass
class Conta:
    numero: int
    cpf: int
    agencia: str = AGENCIA
    saldo: float = 0.0
    extrato: str = ""
    saques: int = 0

dict_usuarios = {}
dict_contas = {}


# ============================
#           FUNÇÕES
# ============================

def criar_usuario(nome, nasc, cpf, end):
    """Cria usuário se CPF não existir."""
    if cpf in dict_usuarios:
        return 1
    
    usuario = Usuario(nome, nasc, cpf, end)
    dict_usuarios[cpf] = usuario
    return usuario


def criar_conta_corrente(numero, cpf):
    """Cria conta se CPF estiver cadastrado."""
    if cpf not in dict_usuarios:
        return 1
    
    conta = Conta(numero, cpf)
    dict_contas[numero] = conta
    return conta


def deposito(conta, valor, /):
    if valor <= 0:
        print("Valor inválido.")
        return

    conta.saldo += valor
    conta.extrato += f"Depósito: R$ {valor:.2f}\n"
    print("Depósito realizado com sucesso!")


def saque(*, conta, valor, limite=500, limite_saques=3):

    if valor <= 0:
        print("Operação falhou! Valor inválido.")
        return

    if valor > conta.saldo:
        print("Operação falhou! Saldo insuficiente.")
        return

    if valor > limite:
        print("Operação falhou! Valor excede o limite.")
        return

    if conta.saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return

    conta.saldo -= valor
    conta.extrato += f"Saque: R$ {valor:.2f}\n"
    conta.saques += 1
    print("Saque realizado com sucesso!")


def exibir_extrato(conta):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta.extrato else conta.extrato)
    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("==========================================")


# ============================
#            MENU
# ============================

while True:

    opcao = input(menu)

    # Criar Usuário
    if opcao == "1":
        nome = input("Digite o nome: ")
        nasc = input("Digite a data de nascimento: ")
        
        cpf_raw = input("Digite o CPF: ")
        cpf_limpo = "".join(filter(str.isdigit, cpf_raw))

        if not cpf_limpo.isdigit():
            print("CPF inválido.")
            continue

        cpf = int(cpf_limpo)

        print("\nPreencha seu endereço")
        end = input("Logradouro: ") + ', ' + input("Número: ") + ' - ' + input("Bairro: ") + ' - ' + input("Cidade/UF: ")

        retorno = criar_usuario(nome, nasc, cpf, end)

        if retorno == 1:
            print("CPF já cadastrado.")
        else:
            print("Usuário cadastrado com sucesso!")


    # Criar Conta
    elif opcao == "2":

        cpf = int(input("Digite o CPF do titular: "))

        numero_conta = len(dict_contas) + 1

        retorno = criar_conta_corrente(numero_conta, cpf)

        if retorno == 1:
            print("Usuário não cadastrado.")
        else:
            print(f"Conta criada com sucesso! Número da conta: {numero_conta}")


    # Listar Contas
    elif opcao == "3":
    
        if not dict_contas:
            print("Nenhuma conta cadastrada.")
        else:
            for conta in dict_contas.values():

                usuario = dict_usuarios[conta.cpf]

                print("\n====== CONTA ======")
                print(f"Agência:         {conta.agencia}")
                print(f"Número da Conta: {conta.numero}")
                print(f"Titular:         {usuario.nome}")
                print("======================")

    # Depositar
    elif opcao == "4":
        numero = int(input("Digite o número da conta: "))

        if numero not in dict_contas:
            print("Conta não encontrada.")
            continue

        conta = dict_contas[numero]
        valor = float(input("Informe o valor do depósito: "))

        deposito(conta, valor)

    # Sacar
    elif opcao == "5":
        numero = int(input("Digite o número da conta: "))

        if numero not in dict_contas:
            print("Conta não encontrada.")
            continue

        conta = dict_contas[numero]
        valor = float(input("Informe o valor do saque: "))

        saque(conta = conta, valor = valor)

    # Extrato
    elif opcao == "6":
        numero = int(input("Digite o número da conta: "))

        if numero not in dict_contas:
            print("Conta não encontrada.")
            continue

        conta = dict_contas[numero]
        exibir_extrato(conta)

    elif opcao == "0":
        break

    else:
        print("Operação inválida.")
