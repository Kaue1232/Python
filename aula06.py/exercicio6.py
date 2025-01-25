#Faça um programa que pergunte o salário da pessoa e calcule o valor do aumento. Para salários acima de 1250, o aumento é de 10%, para inferiores ou iguais, o aumento é de 15%




salário = int(input('Digite o valor do seu salário: R$ '))

if salário > 1250:
    novo = salário + (salário * 10/100)

else:
    novo = salário + (salário * 15/100)
    
print('O seu salário passará a ser R${:.2f}'.format(novo))
