#calcular hipotenusa
import math

cateto_1 = float(input('Digite o valor do cateto oposto: '))
cateto_2 = float(input('digite o valor do cateto adjacente: '))

hipotenusa = math.sqrt(cateto_1 ** 2 + cateto_2 ** 2)

print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))

    