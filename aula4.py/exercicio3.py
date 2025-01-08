# O professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude o professor lendo o nome dos alunos aleatoriamente.

import random

nomes1 = ["Kauê", "Anderson", "Alan", "Wesley"]

nome_aleatorio = random.choice(nomes1) #random.choice serve para selecionarmos apenas um nome em uma lista qualquer de pessoas

print(nome_aleatorio)

# Para selecionarmos vários nomes, sem repetições usaremos o random.sample. Ex:
import random

nomes2 = ["Ana", "Carlos", "Bianca", "João", "Mariana", "Pedro"]
nomes_aleatorios = random.sample(nomes2, k=3)  # Seleciona 3 nomes sem repetição

print(nomes_aleatorios)
