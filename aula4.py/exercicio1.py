# Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira.
'''from math import trunc

número = float(input('Digite um número: '))
inteiro = int(trunc(número))
print('O número inteiro de {} é {}'.format(número,inteiro))'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))