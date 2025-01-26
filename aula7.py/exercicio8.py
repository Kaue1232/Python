# Pedra papel tesoura
import random
from time import sleep


itens = ('Pedra','Papel','Tesoura')
computador = random.randint(0,2)
print('Suas Opções:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA')

jogada = int(input('Qual a sua jogada: '))

print('Pedraaaa')
sleep (1) #A função sleep recebe como argumento um número que representa o tempo, em segundos, que o programa deve esperar antes de continuar a execução.
print('Papeel')
sleep(1)
print('Tesoooouu')
sleep(1)
print('Raa!!!')

print('-=' *15)
print('O computador escolheu {}'.format(itens[computador])) #itens[computador] significa basicamente trocar as opções, invés de ser 0, 1 ou 2, escolher entre os itens
print('O jogador escolheu {}'.format(itens[jogada]))
print('-=' *15)

if computador == 0:
    if jogada ==0:
        print('Empate!')

    elif jogada ==1:
        print('JOGADOR VENCEU!')
    elif jogada ==2:
        print('COMPUTADOR VENCEU!')
    else:
        print('Jogada inválida!')


elif computador == 1:
    if jogada == 0:
        print('JOGADOR VENCEU!')
    elif jogada == 1:
        print('Empate!')
    elif jogada == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('Jogada inválida!')


elif computador == 2:
    if jogada == 0:
        print('JOGADOR GANHA!')
    elif jogada ==1:
        print('COMPUTADOR GANHA!')
    elif jogada == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')

else: 
    print('Jogada inválida!')
