x = float(input('Digite o preço do produto: R$ '))
porcentagem = 5/100
desconto = x * porcentagem

print('O produto que custava R$ {:.2f}, na promoção com 5% de desconto, vai custar R$ {:.2f}'.format( x, (x - desconto )))


