#importando a função trunc do módulo math para truncar números decimais
from math import trunc

x = float(input('Digite um numero fracionado: '))

print('A parte inteira do numero {}, é {}'.format(x, trunc(x)))

