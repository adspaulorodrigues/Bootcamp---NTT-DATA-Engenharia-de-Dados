import os

#Declaraçōes das variáveis
LIMITE_DIARIO_SAQUE = 3
saldo_conta = 0
numero_de_saques = 0
mensagem = "Bem vindo ao sistema!"
movimentacao = ""

#Definição do método depositar
def depositar():
    global saldo_conta, mensagem, movimentacao
    os.system("clear")
    print(""" ***** [DIO BOOTCAMP] - NTT DATA Engenharia de Dados com Python *****
    
        [DEPOSITO]
        
        """)
    valor = float(input("         Entre com um valor positivo: "))
    if valor > 0: 
        saldo_conta += valor
        movimentacao += f"        ENTRADA :    R$ {valor:10.2f}\n"
        mensagem = f"Deposito de R$ {valor:.2f}, realizado com sucesso!"
    else:
        mensagem = "Entre com um valor positivo!"

#Definição do método sacar
def sacar():
    global saldo_conta, numero_de_saques, mensagem, movimentacao
    if LIMITE_DIARIO_SAQUE > numero_de_saques:
        os.system("clear")
        print(""" ***** [DIO BOOTCAMP] - NTT DATA Engenharia de Dados com Python *****
    
        [RETIRADA]
        
        """)
        valor = float(input("       Entre como o valor do saque: "))
        if valor > 0 and valor <= saldo_conta:
            numero_de_saques += 1
            saldo_conta -= valor
            movimentacao += f"        SAÍDA   :  - R$ {valor:10.2f}\n"
            mensagem = f"Saque de R$ {valor:.2f}, realizado com sucesso!"
        else:
            mensagem = " Saldo insuficiente!"
    else:
        mensagem = "Limite de saque diário, excedido!"

#Definição do método movimentações
def movimentacoes():
    os.system("clear")
    global saldo_conta, mensagem4
    
    print(""" ***** [DIO BOOTCAMP] - NTT DATA Engenharia de Dados com Python *****
    
        [MOVIMENTAÇÕES]
        
        """)
    print("\n\n        Não foi encontrado histórico de movimentações!)" if not movimentacao else movimentacao) 
    print(f"\n        Saldo em conta: R$ {saldo_conta:.2f}")
    print(" ********************************************************************")
    input("\n Pressione qualquer tecla para voltar > ")

#Chamada do Menu de opções
while(True):
    os.system("clear")
    print("***** [DIO BOOTCAMP] - NTT DATA Engenharia de Dados com Python *****")
    menu = f"""
            [1] - Deposito
            [2] - Saque
            [3] - Extrato
            [4] - Sair
        
            Escolha uma das opções acima: 

        [MENSAGEM: {mensagem} ] """

    opcao = int(input(menu))
    #print(f"[MENSAGEM : {mensagem} ] ")
    if opcao == 1:
        depositar()
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        movimentacoes()
    elif opcao == 4:
        os.system("clear")
       
        menu = """
            ***** [DIO BOOTCAMP] - NTT DATA Engenharia de Dados com Python *****
            
            
            [MENSAGEM : Grato por utilizar nosso sistema! ]

            
            ********************************************************************
            """
        print(menu)
        break
    else:
        mensagem = "Escolha uma opção válida!"


    