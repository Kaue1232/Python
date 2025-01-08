# Calculadora de dólar e euro

conversão = float(input('Quanto você tem de dinheiro na carteira? R$ '))

dólar = conversão / 6.18
euro = conversão / 6.40

print('Você tem {:.2f} dólares e {:.2f} euros'.format(dólar, euro))