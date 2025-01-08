#Aluguel de carros. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

valortotal =  (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(valortotal))

