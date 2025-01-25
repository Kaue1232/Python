# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
 
#Temos duas formas de resolver

# Declarando como caractere
 
número = int(input('Digite um número: '))

escolhido = str(número)

print('Analisando o número {} \n Unidade: {}\n Dezena: {}\n Sentena: {}\n Milhar: {}'.format(número, escolhido[3], escolhido[2], escolhido[1],escolhido[0] ))

'''--------------------------------------------------------------------------------------------------------------------------------------'''
#declarando como número

número = int(input('Digite um número: '))

u = int(número / 1 %10) # vai resultar no resto da divisão
d = int(número // 10 %10)
s = int(número //100 %10)
m = int(número//1000 %10)
print('Analisando o número {} \n Unidade: {}\n Dezena: {}\n Sentena: {}\n Milhar: {}'.format(número, u, d, s, m))