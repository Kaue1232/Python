#Exercícios

print(pow(4200,9)) #pow serve para calcular a potência entre dois números

print(81**(1/2)) # calcular a raiz quadrada de 81

print('='*20)


#fazendo a listagem

n1 = int((input('Digite um valor: ')))
n2 = int((input('Digite outro valor: ')))

s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2

print('A soma é {},a subtração é {}, a multiplicação é {}, a divisão é {:.2f} e a potenciação é {}'.format(s,su,m,d,p))
