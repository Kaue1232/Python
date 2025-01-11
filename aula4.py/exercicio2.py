#Faça um programa que leio o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo. Calcule o tamanho da hipotenusa
'''import math 

catetooposto = float(input('Digite o comprimento do cateto oposto: '))

catetoadjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = (catetooposto**2 + catetoadjacente**2)

raiz = float(math.sqrt(hipotenusa))

print('O tamanho da hipotenusa é igual a {:.2f}'.format(raiz))'''

from math import hypot

catetooposto = float(input('Digite o comprimento do cateto oposto: '))

catetoadjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = hypot(catetooposto,catetoadjacente) #math.hypot serve para calcular o valor da hipotenusa. O math. tem diversas funcionalidades e pode calcular diversas coisas, como seno, cosseno e tangente

print('O tamanho da hipotenusa é igual a {:.2f}'.format(hipotenusa))