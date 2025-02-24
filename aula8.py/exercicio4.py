#Tabuada

tabuada = int(input('Digite um número para ver sua tabuada: '))

for c in range(11):
    resultado = tabuada * c
    print('{} x {} = {}'.format(tabuada, c, resultado))