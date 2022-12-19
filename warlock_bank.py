import textwrap


def menu():
    menu = """\n
    ######## WARLOCK BANK ########

    [1] Consultar saldo
    [2] Sacar
    [3] Extrato
    [4] Depositar
    [7] Cadastrar Novo Usuário
    [8] Criar conta
    [9] Listar Contas
    [0] Sair

    ##############################
    """
    return input(textwrap.dedent(menu))


def criar_usuario(usuarios):
    cpf = input("Informe apenas os números de seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("!!! CPF já cadastrado! !!!")
        return

    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe seu endereço completo (logradouro, Nº - bairro - CEP - cidade / UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereco": endereco})
    print("\n### USUÁRIO CRIADO COM SUCESSO! ###")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe apenas os números do seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n### CONTA CRIADA COM SUCESSO! ###")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n!!! Usuário não foi encontrado. !!!\n!!! Por favor realize primeiro o cadastro de um novo usuário/CPF !!!")


def depositar_grana(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"\n>==> Deposito:\tR$ {valor_deposito:.2f}"
        print("=== Depósito realizado com sucesso! ===")
    else:
        print("!!! Erro na operação! Não é possível depositar essa quantia. !!!")
    return saldo, extrato


def func_sacar(*, saldo, valor_saque, extrato, limite_por_saque, numero_saque, limite_saque_diario):
    excedeu_saldo = valor_saque > saldo
    limite_valor_saque = valor_saque > limite_por_saque
    limite_de_saque = numero_saque >= limite_saque_diario

    if excedeu_saldo:
        print("!!! Saldo insuficiente para realizar está operação !!!")
    elif limite_valor_saque:
        print("!!! Valor ultrapassa o limite de saque !!!")
    elif limite_de_saque:
        print("!!! Você atingiu o número máximo de saques diários !!!")
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"\nSaque ATM:\tR${valor_saque:.2f}"
        numero_saque += 1
        print("=== Saque realizado com sucesso! ===")
    else:
        print("Opção inválida, tente novamente!")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print(f"########### EXTRATO ###########")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n\nSaldo:\t R$ {saldo:.2f}\n")
    print(f"<================================>\n")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = 1585

    saldo = 1500
    numero_saque = 0
    limite_por_saque = 500
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            print(
                f"######## CONSULTA SALDO ########\n\n    -> Saldo atual de R$ {saldo:.2f}\n")

        elif opcao == "2":
            valor_saque = float(input("Digite o valor de saque: "))
            saldo, extrato = func_sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite_por_saque=limite_por_saque,
                numero_saque=numero_saque,
                limite_saque_diario=LIMITE_SAQUES
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            valor_deposito = float(
                input("Informe o valor que está depositando: "))
            saldo, extrato = depositar_grana(saldo, valor_deposito, extrato)

        elif opcao == "7":
            criar_usuario(usuarios)

        elif opcao == "8":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "9":
            listar_contas(contas)

        elif opcao == "0":
            print("### Warlock Bank agradece! ###")
            break

        else:
            print("Opção inválida, tente novamente!")


main()
