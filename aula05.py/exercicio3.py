# Crie um programa e diga se ela tem "Silva" no nome ou não.

nome = str(input('Digite seu nome completo: '))

print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))