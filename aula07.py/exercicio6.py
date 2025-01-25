# Programa para saber se podemos formar um triângulo, e se sim, ele é equilátero, isósceles ou escaleno

# Recebendo os segmentos
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

# Verificando se podemos formar um triângulo
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima podem formar um triângulo')

    # Verificando o tipo de triângulo
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Com os segmentos fornecidos acima, não podemos formar um triângulo')



