# Manipulando Texto

#Fatiamento de string

texto1 = 'Python é incrível'

print(texto1[0:7]) #Irá imprimir somente python, com 6 caracteres +1
print(texto1[9]) #Imprimir somente o caractere 9
print(texto1[0:16:2]) #Vai imprimir todos os caracteres de 0 a 16 pulando de 2 em 2. Ex: Kauê Kelvyn ----- 'Ku evn'
print(texto1[:7]) #Imprimir todos os caracteres de 0 até 6

#Análise e transformações de string

texto2 = 'Python é incrível'
print(len(texto2)) # len significa ler a quantidade de caracteres vou ter na string, no caso 'Python é incrível' temos 17
print(texto2.upper().count('P')) #upper verifica se tem uma letra maiúscula, já o count veifica qual letra quero verificar se tem na frase
print(texto2.replace('incrível','ruim')) # Replace significa alterar/substituir, então vou alterar a palavra incrível por ruim

print('Python' in texto2) # Verifica se a palavra python está dentro da frase

print(texto2.lower().find('incrível')) #Procurar e dizer a posição de 'incrível'
print(texto2.split()) #Printar todos os termos separadamente
