# MÓDULOS
import operator


def secao_menu(titulo_secao):
    # Gera um menu de strings.
    # Passe como argumento uma string com o nome do título da seção que deseja inserir.
    tam_titulo_secao = len(titulo_secao)
    print("=" * tam_titulo_secao)
    print(titulo_secao)
    print("=" * tam_titulo_secao)


def titulo_menu_principal(titulo_menu):
    # Passe como argumento uma string com o nome do título do menu que deseja inserir.
    tam_titulo_menu = len(titulo_menu)
    print("=" * tam_titulo_menu)
    print(titulo_menu)
    print("=" * tam_titulo_menu)


def opcoes_menu_principal():
    print("""
    O que deseja fazer?
    
    [E/e] IMPRIMIR EXTRATO
    [D/d] REALIZAR DEPÓSITO
    [S/s] REALIZAR SAQUE
    [T/s] TERMINAR E SAIR
    
    :""", end=" "
    )


def confirmacao_de_saida():
    resposta = input("""
        Tem certeza de que deseja sair?
    
        [S/s] SIM
        [N/n] NÃO
        : """
                     )
    resposta.lower()

    if resposta == "s":
        return False

    elif resposta == "n":
        return True


# CONSTANTES E VARIÁVEIS
MAXIMO_DE_SAQUES = 3
LIMITE_POR_SAQUE = 500

saldo = 0.0
extrato = "-"

nro_de_saques = 1
soma_dos_saques = 0

dicionario_extrato = {
    "depositos": "",
    "saques": "",
}

continuar = True
continuar_menu_principal = True

while continuar_menu_principal:

    titulo_menu_principal("       BRASIL SUPER BANCO       ")
    opcoes_menu_principal()

    opcao = input(" ").lower()

    match opcao:
        # FUNÇÃO DE EXTRATO:

        case "e":
            secao_menu("       OPERAÇÃO DE EXTRATO       ")
            extrato_depositos_vazio = len(dicionario_extrato["depositos"]) == 0
            extrato_saques_vazio = len(dicionario_extrato["saques"]) == 0

            if all([extrato_depositos_vazio, extrato_saques_vazio]):
                print("\n")
                secao_menu("       EXTRATO       ")

                print("Não foram realizadas movimentações.\n\n")

            else:
                print("\n")
                secao_menu("       EXTRATO       ")
                print("    DEPÓSITOS:")
                print(dicionario_extrato["depositos"])

                print("    SAQUES")

                if extrato_saques_vazio:

                    print("\nAinda não foram realizados saques.\n\n")

                else:
                    print(dicionario_extrato["saques"])
                    print("\n-----------------------------\n")

        # FUNÇÃO DE DEPÓSITO:

        case "d":

            try:
                secao_menu("       OPERAÇÃO DE DEPÓSITO       ")

                deposito = float(input("Valor para depósito: R$ "))
                deposito_positivo = operator.gt(deposito, 0.0)

                deposito_invalido = """
                Não é possível depositar valores negativos ou iguais a zero!
                Insira outro valor e tente novamente.\n
                """
                print("\n")

                # verificação
                if deposito_positivo:

                    dicionario_extrato["depositos"] = dicionario_extrato["depositos"] + f"    + R$ {deposito:.2f}\n"

                    saldo += deposito

                    print(f"    Valor depositado: R$ {deposito:.2f}\n    Saldo total da conta: R$ {saldo:.2f}")

                elif (deposito == 0) or (deposito < 0):
                    print(deposito_invalido)
            except ValueError:
                print("Tipo de dado inválido! Por favor, insira um valor numérico.")

        # FUNÇÃO DE SAQUE:

        case "s":

            try:
                secao_menu("       OEPRAÇÃO DE SAQUE       ")

                saque = float(input("Insira o valor que deseja sacar: R$ "))
                saque_positivo = operator.gt(saque, 0)

                if all([saque_positivo, nro_de_saques <= MAXIMO_DE_SAQUES, saque <= LIMITE_POR_SAQUE, saque <= saldo]):

                    saldo -= saque
                    dicionario_extrato["saques"] = dicionario_extrato["saques"] + f"    - R$ {saque:.2f}\n"
                    print(f"    Valor sacado: R$ {saque:.2f}\n    Saldo total da conta: R$ {saldo}")

                    nro_de_saques += 1
                    soma_dos_saques += saque

                elif (nro_de_saques > MAXIMO_DE_SAQUES) or (saque > LIMITE_POR_SAQUE):
                    print("""
                    Operação não permitida!
                    O valor informado pode ter:
                    1) Excedido o limite máximo de R$ 500.00 por saque; ou 
                    2) Excedido o  número máximo de 3 saques por dia.
                    
                    Tente novamente.
                    """
                          )

                elif saque > saldo:
                    print("\nOperação não permitida! Saldo insuficiente!")

                elif (saque == 0) or (saque < 0):
                    print(
                        "\nOperação não permitida! Não é possível sacar valores nulos ou negativos. Tente novamente.")

            except ValueError:
                print("Tipo de dado inválido! Por favor, insira um valor numérico.")

        case "t":

            secao_menu("       OPERAÇÃO DE SAÍDA       ")
            continuar_menu_principal = confirmacao_de_saida()
            print("Você saiu.")

        case _:
            print("\nEntrada não reconhecida. Por favor, escolha uma das opções do menu.\n")
