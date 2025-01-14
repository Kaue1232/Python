# Escreva um programa que faça o computador pensar em um número de 0 a 5 e peça para o usuário descobrir qual número o computador pensou
import random

print('Vou pensar em um número de 0 a 5 e você tenta adivinhar!')
número = int(input('Em que número eu pensei? '))

escolhido = random.randint(0,5) # random.randint gera um número aleatório entre 0 e 5

if escolhido == número:
    print('Você acertou! Eu realmente escolhi {}'.format(escolhido))
else:
    print('Você perdeu! Eu escolhi {}'.format(escolhido))

 
  


