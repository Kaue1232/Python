#Faça um programa que leio o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo. Calcule o tamanho da hipotenusa
import math 

catetooposto = int(input('Digite o comprimento do cateto oposto: '))

catetoadjacente = int(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = (catetooposto**2 + catetoadjacente**2)

raiz = int(math.sqrt(hipotenusa))

print('O tamanho da hipotenusa é igual a {}'.format(raiz))