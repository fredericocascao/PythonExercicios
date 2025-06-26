km = float(input('Quantos km o carro percorreu: '))
dia = int(input('Quantos dias o carro ficou alugado: '))
preço_dia = dia * 60
preço_km = km * 0.15
valor = preço_dia + preço_km

print('O carro percorreu {} km e ficou alugado por {} dias, o valor por dia a ser pago é de R$ {}, e o valor do km rodado é de R$ {:.2f}, custando um total de R$ {:.2f} pelo aluguel'.format(km, dia, preço_dia, preço_km, valor))