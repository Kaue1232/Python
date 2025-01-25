#faça um programa que leia 3 números e mostre qual deles é o maior e o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))


#Verificando o menor número 
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
        menor = n3

#Verificando o maior número
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
    
if n3 > n1 and n3 > n2:
        maior = n3
        
        
print('O menor número é o {}'.format(menor))
print('O maior número é o {}'.format(maior))
