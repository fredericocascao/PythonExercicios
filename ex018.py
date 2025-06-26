#calculando seno, cosseno e tangente
import math

angulo = float(input('Digite o valor do angulo: '))

print('O valor de SENO do angulo {}, é {:.2f} !!'.format(angulo, math.sin(math.radians(angulo))))
print('O valor de COSSENO do angulo {}, é {:.2f} !!'.format(angulo, math.cos(math.radians(angulo))))
print('O valor da TANGENTE do angulo {}, é {:.2f} !!'.format(angulo, math.tan(math.radians(angulo))))
