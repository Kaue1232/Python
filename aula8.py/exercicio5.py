# Desenvolva um programa que leia 6 números inteiros e faça a soma somente daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

soma = 0 # Armazena a soma dos números pares
cont = 0 # Contar quantos números pares vão ser armazenados na contagem do for
for c in range(1,7): 
    num = int(input('Digite um valor: '.format(c)))
    if num%2 == 0:
      soma += num
      cont += 1

print('Você informou {} números PARES e a soma foi de {}'.format(cont, soma))

    
