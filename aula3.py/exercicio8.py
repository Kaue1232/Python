#Calcule o desconto de 5% de um produto qualquer 

preço = float(input('Qual o preço do produto? R$'))

desconto = preço - ( preço *5/100 )
diferença = preço - desconto

print('O valor do produto com desconto de 5% é de R${}\nOu seja, R${} de desconto'.format(desconto, diferença))