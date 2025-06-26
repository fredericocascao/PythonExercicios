salario = float(input('Digite o salario: R$ '))
aumento = 15 / 100
calculo = salario * aumento   

print('O novo salario do funcionário com aumento de 15% de desconto é: R$ {:,.2f}'.format(salario + calculo))

