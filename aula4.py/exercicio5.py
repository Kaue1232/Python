#Faça um programa em python que lê um ângulo qualquer e calcule o valor do seu seno, cosseno e tangente.

from math import sin, cos, tan, radians

angulo = int(input('Digite um ângulo: '))

seno = sin(radians(angulo)) # Vamos pegar o ângulo, converter para radianos, e depois calcular seu seno
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O valor do seno é {:.2f} , do cosseno é {:.2f} e da tangente é {:.2f}'.format(seno,cosseno,tangente))

