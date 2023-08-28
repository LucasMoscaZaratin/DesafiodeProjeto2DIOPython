import textwrap
import os 
os.system('cls')


def menu():
    menu = """\n
    ==========Inicio==========
    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [4] - Adicionar nova conta 
    [5] - Adicionar novo usário
    [6] - Listar contas 
    [7] - Sair
    ==========================
    ==>
    """
    return input(textwrap.dedent(menu))

def deposito(saldo, valor_depositado, extrato, /):
    if valor_depositado>0:
        saldo += valor_depositado
        extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
        print("Depósito realizado com sucesso!")

    else:
        print("Desculpe, sua operação não foi realizada!\n Tente novamente")

    return saldo, extrato

def saque(*,saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor_saque > saldo 
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("Operação não realizada!\nSaldo Insuficiente")

    elif excedeu_limite:
        print("Operação não realizada!\n Limite diario excedido")

    elif excedeu_saques:
        print("Operação não realizada!\n Quantidade máxima diaria de saques execedida")

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}"
        print("Saque realizado com sucesso!")

    else:
        print("Desculpe, sua operação não foi realizada!\n Tente novamente")
    
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações em sua conta." if not extrato else extrato)
    print(f"\nSaldo:\t\R$ {saldo:.2f}")
    print("==========================================") 

def criar_usuario(usuarios):
    cpf=input("Informe seu CPF: \nOBS: Somente os números")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Cadastro Inválido!\n CPF já cadastrado")
        return
    
    nome = str(input("Informe seu nom: "))
    data_nascimento = input("Informe sua data de nascimento")
    endereco = input("Informe seu endereço: \nLogradouro, numero - bairro - cidade/sigla estado")

    usuarios.append({"nome": nome, 
                    "data_nascimento" : data_nascimento,
                    "cpf" : cpf, 
                    "endereco" : endereco })

    print("Usuario cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Informe o seu CPF")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return{"agencia": agencia,
               "num_conta": num_conta,
               "usuario": usuario}
    print("Não foi possível criar sua conta.\nTente novamenta mais tarde.")

def list_conta(contas):
    for conta in contas:
        cont=f"""\
            agencia:\t{conta['agencia']}\n
            C/C:\t{conta['num_conta']}\n
            Titular:\t{conta['usuario']}"""
    print(textwrap.dedent(cont))

def main():
    LIMITE_SAQUES=3
    AGENCIA="0001"

    saldo = 0
    limite = 500
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        op = menu()

        if op == 1:
            valor_depositado = float(input("Informe o valor que deseja depositar."))
            
            saldo, extrato = deposito(saldo, valor_depositado, extrato)
        
        elif op == 2:
            valor_saque = float(input("Informe o valor que deseja sacar"))
            
            saldo, extrato =  saque(saldo = saldo,
                                    valor_saque = valor_saque, 
                                    extrato = extrato,
                                    limite = limite,
                                    numero_saques = numero_saques,
                                    limite_saques = LIMITE_SAQUES)
        
        elif op == 3:
            exibir_extrato(saldo, extrato=extrato)
        
        elif op == 4:
            criar_usuario(usuarios)

        elif op == 5:
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,num_conta,usuarios)
            
            if conta:
                contas.append(conta)
        
        elif op == 6:
            list_conta(contas)


        elif op == 7:
            break

        else:
            print("Operação inválida.\nTente novamente.")

main()