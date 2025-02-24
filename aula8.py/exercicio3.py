# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que estão em um intervalo de 1 a 500

soma = 0
cont = 0
for c in range (1,501, 2):
    if c %3 == 0: # Se c tiver um número que a divisão por 3 tiver o resto zero
        cont += 1 # abreviação de cont = cont + 1 
        soma += c # abreviação de soma = soma + c
print('A soma de todos {} valores solicitados é {}'.format(cont,soma)) # se o print for dentro do laço 'for', ele irá se repetir toda vez que achar um número ímpar divisível por 3 entre 1 e 500




