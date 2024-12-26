# Calcular a área do quarto e a quantidade de tinta para ser pintado

b = float(input('largura da parede: '))
h = float(input('Altura da parede: '))

área = b*h
litro = área/2

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m².\nPara pintar sua parede, você vai precisar de {:.2f}litros de tinta'.format(b, h, área, litro))