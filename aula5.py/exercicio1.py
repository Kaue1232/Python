#Crie um programa que leia o nome completo de uma pessoa e mostre: nome com todas as letras maiúsculas, nome com todas as letras minusculas, quantas letras ao todo e quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')) .strip() #serve para tirar os espaços antes e depois do nome.

print('O seu nome em maíusculo é {}'.format(nome.upper()))
print('O seu nome em minúsculo é {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

separa = nome.split()

print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0]))) # split faz com que o nome é divido e imprimido em partes, e separa[0] vai imprimir somente o primeiro nome, que é Kauê
'''print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))'''






