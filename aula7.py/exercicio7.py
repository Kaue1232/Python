#Simulador de Loja. O pagamento à vista no dinheiro tem um desconto de 10%, à vista no cartão de 5%, em até 2x parcelado é sem juros, a partir de 3x juros de 20%

print('============= LOJA KAUE =============')
pagamento = float(input('Preço das compras: '))

print('FORMA DE PAGAMENTO\n[1] à vista no dinheiro/cheque\n[2] à vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão ')

opção = int(input('Qual é a forma de pagamento? '))

if opção == 1:
    print('Sua compra de R${} passa a ser R${} com desconto'.format(pagamento, (pagamento - (10/100 * pagamento))))

elif opção == 2:
    print('Sua compra de R${:.2f} passa a ser R${:.2f} com desconto'.format(pagamento, (pagamento - (5/100 * pagamento))))

elif opção == 3:
    print('Suas parcelas será de R${:.2f}'.format(pagamento/2))

elif opção ==4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(parcelas, (pagamento + (20/100))/parcelas ))
    print('Sua compra de R${:.2f} vai custar R${} no final'.format(pagamento, pagamento + (pagamento * (20/100)) ))

else:
    print('Erro, tente novamente!')





