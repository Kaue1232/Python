# Conversão de um número inteiro para octal, binário ou hexadecimal

número = int(input('Digite um número inteiro: '))

print('Escolha uma base para conversão:')
print('[1] converter para binário.')
print('[2] converter para octal.')
print('[3] converter para hexadecimal.')

opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(número, bin(número) [2:]))

elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(número, oct(número)[2:]))

elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(número, hex(número)[2:]))

else:
    print('Opção inválida! Tente novamente.')



