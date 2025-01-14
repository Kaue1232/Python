# Faça um programa que pergunta a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 centavos por km de viagens com até 200km e R$0,45 centavos para viagens mais longas

viagem = float(input('Digite a distância da viagem: '))

if viagem <= 200:
    valor = viagem *0.50
    print('O valor da viagem vai ser no total de R${:.2f}'.format(valor))


else:
    valor = viagem *0.45
    print('O valor da viagem vai ser de R${:.2f}'.format(valor))