#Condições if e else 

tempo = int(input('Quanto anos tem seu carro? '))

if tempo <=3:
    print('Seu carro é novo!')

else:
    print('Seu carro é velho!')

'''--------------------------------------------------------------------------------------------------------------------------------------'''

nome = str(input('Qual o seu nome? '))
if nome == 'kaue':
        print('Que nome lindo que você tem!')

else:
        print('Que nome comum que você tem!')

print('Olá! Bom dia, {}'.format(nome))

'''--------------------------------------------------------------------------------------------------------------------------------------'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

print('A sua média foi de {:.1f}'.format(media))

if media >= 6:
    print('Parabéns, você foi aprovado!')

else:
    print('Você foi reprovado por falta de nota!')


