numero = int(input('Digite um número: '))

print('O número digitado foi:', numero)

print('A unidade do número é: ', numero % 10)
print('A dezena do número é: ', (numero // 10) % 10)
print('A centena do número é: ', (numero // 100) % 10)
print('O milhar do número é: ', (numero // 1000)  % 10)
