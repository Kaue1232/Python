# Estrutura de repetição for

#código 1  
'''laço c no intervalo de um até 10

for c in range (0,10):
    print('Oi')

print('FIM!') # se o comando FIM estiver dentro do FOR, ele irá repetir OI e FIM 10 vezes'''

#código 2
'''n = int(input('Digite um número: '))

for c in range (0,n+1):
    print(c)

print('FIM!')'''

#código 3
'''i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo/intervalo: '))


for c in range(i, f+1, p):
    print(c)

print('FIM!')'''

#código 4

s = 0
for c in range (0,4):
    n = int(input('Digite um valor: ')) #Irei digitar 4 valores repetidamentes e fazer a somatória entre eles
    s += n

print('O somatório de todos os valores é de {}'.format(s))
