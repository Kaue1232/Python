#Criança Esperança

print('-'*29)
print('CRIANÇA ESPERANÇA')
print('-'*29)
print('MUITO OBRIGADO POR NOS AJUDAR')
print('[1] para doar R$10')
print('[2] para doar R$25')
print('[3] para doar R$50')
print('[4] para doar outro valor')
print('[5] para cancelar')

dinheiro = int(input('Escolha um valor para doar: '))

match dinheiro:
    case 1: 
        dinheiro = 10
    
    case 2:
        dinheiro = 25

    case 3:
        dinheiro = 50

    case 4:
        dinheiro = int(input('Qual o valor da doação? R$ '))

    case 5:
        dinheiro = 0

print('-'*29)
print('Sua doação foi de R${}'.format(dinheiro))



    






