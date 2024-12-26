#desafio 3. Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('digite um valor: '))
print(type(n1)) 

n2 = int(input('Digite o segundo valor: '))
print(type(n2))

n = n1 + n2
print('O valor de {} + {} é igual a {}'.format(n1, n2, n))
print(type(n))




#desafio 4. Crie um programa que leia algo pelo teclado e mostre seu tipo e todas as informações possíveis sobre ele.

k = input('Digite algo: ')
print ('O tipo primitivo desse valor é {}'.format(type(k)) )
print('Só tem espaços? {}'.format(k.isspace()))
print('É um número? {}'.format(k.isnumeric()))
print('É alfabético? {}'.format(k.isalpha()))
print('É alfanumérico? {}'.format(k.isalnum()))
print('Contém somente letras maiúsculas? {}'.format(k.isupper()))
print('Contém somente letras minúsculas? {}'.format(k.islower()))
print('Está capitalizada? {}'.format(k.istitle()))

