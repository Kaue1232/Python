#desafio 1. Crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o nome digitado
nome = input ('Qual é o seu nome? ')
print ('Olá {}, prazer em te conhecer!'.format(nome)) 

#desafio 2. Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre essa mensagem com a data formatada

dia = input ('Qual dia você nasceu?')
mes = input ('Qual mês você nasceu?')
ano = input('Qual ano você nasceu?')

print ('Data de nascimento: {}/{}/{}'.format(dia, mes, ano))