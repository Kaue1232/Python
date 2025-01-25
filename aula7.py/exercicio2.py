# Aprovação de empréstimo, perguntar o salário, o valor da casa e quantos anos o compradorar irá demorar para pagar, sendo que se comprometer 30% de seu salário, o empréstimo será negado

valorcasa = int(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o valor do seu salário por mês? R$ '))
anos = int(input('Quantos anos vai demorar para pagar? '))

quantidademeses = (anos * 12)
prestacaomensal = valorcasa/quantidademeses

if prestacaomensal > (30/100) * salario:
    print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}\nEMPRÉSTIMO NEGADO!'.format(valorcasa, anos, prestacaomensal))

else:
     print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}\nEMPRÉSTIMO CONCEDIDO!'.format(valorcasa, anos, prestacaomensal))


