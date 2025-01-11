# O professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude o professor lendo o nome dos alunos aleatoriamente.

import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4] #Em python, os colchetes servem em casos de listas, strings, tuplas ou matrizes.

escolhido = random.choice(lista)

print('O aluno(a) escolhido(a) será o(a) {}'.format(escolhido)) #random.choice escolhe um valor fornecido




'''# Para selecionarmos vários nomes, sem repetições usaremos o random.sample. Ex:
import random

nomes2 = ["Ana", "Carlos", "Bianca", "João", "Mariana", "Pedro"]
nomes_aleatorios = random.sample(nomes2, k=3)  # Seleciona 3 nomes sem repetição

print(nomes_aleatorios)'''
