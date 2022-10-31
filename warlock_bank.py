# realizar no máximo 3 saques diários [ok] com limite de R$ 500,00
# operação depósito [OK]
# operação extrato

menu = """

######## WARLOCK BANK ########

O lugar certo para fazer seu gold render :)

[1] Consultar saldo
[2] Sacar
[3] Extrato
[8] Depositar
[0] Sair

"""

saldo = 0.52
numero_saque = 0
limite_por_saque = 500
extrato = ""
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print(f"######## CONSULTA SALDO ########\n\n    -> Saldo atual de R$ {saldo:.2f}\n")

    elif opcao == "8":
        deposito = float(input("Informe o valor que está depositando: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"\n   -> Depósito de R$ {deposito:.2f}\n"
        else:
            print("!!! Não é possível depositar essa quantia !!!")

    elif opcao == "2":
        saque = float(input("Digite o valor de saque: "))

        excedeu_saldo = saque > saldo
        limite_valor_saque = saque > limite_por_saque
        limite = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("!!! Você não possui saldo suficiente para esta operação!!! ")

        elif limite_valor_saque:
            print("!!! Valor ultrapassa o limite de saque!!! ")

        elif numero_saque:
            print("!!! Você atingiu o número máximo de saques diários!!! ")

        elif saque > 0:
            saldo -= saque
            extrato += f" -> Saque ATM R$ -{saque:.2f}\n"
            numero_saque =+ 1

        else:
            print("Opção inválida, tente novamente!")

    elif opcao == "3":
        print(f"########### EXTRATO ###########\n{extrato}")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"================================\n{extrato}")

    elif opcao == "0":
        print("### Warlock Bank agradece! ###")
        break

    else:
        print("Opção inválida, tente novamente!")