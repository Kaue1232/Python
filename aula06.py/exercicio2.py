# Faça um programa que leia a velocidade de um carro. Se ele passar de 80km/h, escreva uma mensagem informando que ele foi multado. A multa vai custar 7,00 reais por cada km acima do limite 

quilometragem = int(input('Qual a velocidade atual do carro? '))

multa = (quilometragem *7)

if quilometragem <= 80:
    print('Tenha um bom dia! Dirija com segurança.')


else:
    print('ATENÇÃO! VOCÊ FOI MULTADO POR ESTAR EM ALTA VELOCIDADE. O VALOR DA MULTA SERÁ DE R${}'.format(multa))

    


