menu ='''
############ MENU ############
#                            #
#       depósito ->[0]       #
#       saque    ->[1]       #
#       extrato  ->[2]       #
#       sair     ->[3]       #
#                            #
##############################        
'''
print(menu)
LIMITE_SAQUES = 3
saldo = 2000
numero_saques = 0
extrato = ''

while True: 
    opcao = input('\nQual operação você deseja realizar? ')

    if opcao == '0':
        print('\nDepósito')
        quantidade = float(input('Quanto você deseja depositar? '))
        saldo = saldo + quantidade
        print(f'O saldo atual é de R$ {saldo:.2f}')
        extrato = extrato + f'Foi realizado um depósito de R$ {quantidade:.2f}, o saldo no momento era de; R$ {saldo:.2f}\n'

    elif opcao == '1':
        print('\nSaque')
        quantidade = float(input('Quanto você deseja sacar? '))
        numero_saques += 1
        if saldo >= quantidade and numero_saques <= 3:
            saldo = saldo - quantidade
            print(f'\nSaque realizado com sucesso, o saldo atual é de R$ {saldo:.2f}')
            extrato = extrato + f'Foi realizado um saque de R$ {quantidade:.2f}, o saldo no momento era de; R$ {saldo:.2f}\n'
        else:
            print('\nNão foi possível realizar o saque, entre em contato com o seu gerente.')

    elif opcao == '2':
        print(f'\nExtrato\n{extrato}')

    elif opcao == '3':
        print('Saindo do sistema')
        break

    else:
        print('Você selecionou uma opção inválida')

