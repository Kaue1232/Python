#Reajuste salarial de 15%

salario = float(input(('Digite o valor do salário: R$ '))) 

reajuste = salario + (salario*15/100)

print('O salário que custava {}, com o reajuste passa a ser R${:.3f}'.format(salario, reajuste)) 
