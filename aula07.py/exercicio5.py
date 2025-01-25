#Faça um programa que pergunta ao recruta que ano ele nasceu. Informe se ele ainda vai se alistar, se é a hora dele se alistar ou se já passou do tempo

from datetime import date # Biblioteca que indica datas
atual = date.today().year # O ano atual que nós estamos.


nascimento = int(input('Que ano você nasceu, recruta? '))
idade = (2025 - nascimento)
temporestante = (18 - idade)

if idade < 18:
    print('Quem nasceu em {} tem {} em 2025.'.format(nascimento, idade))
    print('Ainda faltam {} anos para você se alistar.'.format(temporestante))
    print('Você irá se alistar somente em {}'.format(nascimento + 18))

elif idade == 18:
    print('Seu alistamento será agora em 2025!')

else:
    print('Quem nasceu em {} tem {} em 2025.'.format(nascimento, idade))
    print('Você deveria ter se alistado há {} anos atrás'.format(2025 - (nascimento + 18)))









