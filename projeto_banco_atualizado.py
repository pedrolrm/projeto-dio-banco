#saque = keyword only - declarando a variavel na hora de chamar
#deposito = positional only - somente enviado os argumentos na hora de chamar em ordem
#extrato = positional - saldo - nomeado = extrato
#######################################################################
saldo = 2000
extrato = ''
LIMITE_SAQUES = 3
quantidade_saques = 0
usuarios = []
cpfs = []
#######################################################################
# Definindo as funções bancárias
#######################################################################
def deposito(quantidade, saldo, extrato):
    if quantidade > 0:
        saldo = saldo + quantidade
        print(f'Seu depósito de R${quantidade:.2f} foi realizado com sucesso')
        extrato = extrato + f'Foi realizado um depósito de R$ {quantidade:.2f}\n'
    else:
        print('O valor digitado não é válido')
    return saldo, extrato 
#######################################################################
def saque(LIMITE_SAQUES, quantidade, saldo, extrato, quantidade_saques):
    if quantidade_saques < LIMITE_SAQUES and saldo >= quantidade:
        quantidade_saques += 1
        saldo = saldo - quantidade
        extrato = extrato + f'Foi realizado um saque de R$ {quantidade:.2f}\n'
        print(f'Seu saque de R${quantidade:.2f} foi realizado com sucesso')
    else: 
        print('Não foi possível realizar seu saque, contate seu gerente')
    return saldo, extrato, quantidade_saques
#######################################################################   
def ver_extrato(extrato):
    return f''' 
------------EXTRATO------------
{extrato}

-------------------------------
 '''
#######################################################################
def criar_usuario(nome, data_nascimento, endereco, cpf, usuarios):
    usuario = {'nome' : nome, 'data de nascimento' : data_nascimento, 'cpf': cpf, 'endereco': endereco}
    usuarios.append(usuario)
    cpfs.append(cpf)
    return usuarios
#######################################################################
def criar_conta_corrente(nome, cpf, agencia, numero_conta):
    usuario = {'Nome' : nome, 'cpf': cpf}
    numero_conta += 1
    conta_corrente = {'Usuário': usuario, 'Agência' : agencia, 'Número da conta': numero_conta}
    return conta_corrente
#######################################################################
# Criando o menu para o usuário
#######################################################################

menu ='''
############ MENU ########################
#                                        #
#       Depósito             ->[0]       #
#       Saque                ->[1]       #
#       Extrato              ->[2]       #
#       Criar usuário        ->[3]       #
#       Criar conta corrente ->[4]       #
#       Sair                 ->[5]       #
#                                        #
##########################################        
'''
print(menu)

#######################################################################
# Loop para solicitar a operação do usuário e chamar as funções definidas
#######################################################################

while True:
    opcao = input('\nQual operação você deseja realizar? ')

#######################################################################

    if opcao == '0':
        quantidade = float(input('Qual valor você deseja depositar? '))
        saldo, extrato = deposito(quantidade, saldo, extrato)

#######################################################################

    elif opcao == '1':
        quantidade = float(input('Qual valor você deseja sacar? '))
        saldo, extrato, quantidade_saques = saque(
            saldo=saldo,
            quantidade=quantidade,
            extrato=extrato,
            LIMITE_SAQUES=LIMITE_SAQUES,
            quantidade_saques=quantidade_saques
        )

#######################################################################

    elif opcao == '2':
        print(ver_extrato(extrato=extrato))

#######################################################################

    elif opcao == '3':
        nome = input('Digite seu nome: ')
        data_nascimento = input('Digite sua data de nascimento: ')
        cpf = input('Digite seu CPF: ')
        endereco = input('Digite seu endereço: ')
        if cpf in cpfs:
            print('Já existe um usuário com esse CPF!')
        else: 
            usuarios = criar_usuario(
            nome=nome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            endereco=endereco,
            usuarios=usuarios                         
            )
            print(f'Seu usuário foi criado com sucesso {nome}!')

#######################################################################

    elif opcao == '4':
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu CPF: ')
        agencia = '0001'
        numero_conta = 0 
        conta_corrente = criar_conta_corrente(
        nome=nome,
        cpf=cpf,
        agencia=agencia,
        numero_conta=numero_conta    
        )
        print(f'Sua conta corrente foi criada com sucesso {nome}!')

#######################################################################

    elif opcao == '5':
        break

#######################################################################
