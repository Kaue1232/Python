# Calculadora de dólar e euro

con = float(input('Quanto você tem de dinheiro na carteira? R$ '))

dólar = con / 6.18
euro = con / 6.40

print('Você tem {:.2f} dólares e {:.2f} euros'.format(dólar, euro))