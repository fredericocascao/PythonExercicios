x = float(input('Digite a altura da parede: '))
y = float(input('Digite a largura da parede: '))
area = x * y
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(y, x, (x*y)))
print('Precisa de {} litros de tinta para pinta a area'.format(area / 2))
