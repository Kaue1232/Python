# contagem regressiva de 0 até 10 segundos, com intervalos de 1s

from time import sleep

for c in range(10, -1, -1): # o -1 do meio serve para contar até o 0, pois se fosse 0 ao invés de -1 iria de 10 até 1
    print(c) 
    sleep (1)

print('Explodir!')