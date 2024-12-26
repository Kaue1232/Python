# aula02. Tipos primitivos e saídas de dados


n1 = int (input('Digite um número: ')) # O código sem o int vai apenas juntar/concatenar os números, pois as variáveis n1 e n2 entendem como se os valores que estão dentro são do tipo caractere
print(type(n1))
n2 = int (input('Digite outro número: '))
print(type(n2))

s = (n1+n2) 
print('A soma entre {} + {} vale {}'.format(n1, n2, s))
print(type(s))

# ou poderia fazer print('A soma vale {}'.format(s)) 





#tabela dos is.
n = input('Digite algo: ')
print(n.isnumeric())  # Contém apenas números?

m = input('Digite algo: ')
print(m.isalpha()) # Contém apenas letras?.

o = input('Digite algo: ')
print(o.isalnum()) # Contém letras e/ou números? retornará falso se estiver vazio

p = input('Digite algo: ')
print(p.isupper()) # Está apenas com letras maiúsculas?