# Valor inteiro maior, menor ou igual

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print('{} é MAIOR que {}'.format(n1,n2))

elif n1 < n2:
    print('{} é MENOR QUE {}'.format(n1,n2))

else:
    print('OS dois valores são iguais!')