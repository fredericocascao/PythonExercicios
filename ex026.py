frase = input('Digite uma frase: ')
print('A frase digitada foi:', frase)

print('A palavra "R" aparece {} vezes'.format(frase.lower().count('r')))
print('A primeira ocorrência de "R" está na posição:', frase.lower().find('r'))
print('A última ocorrência de "R" está na posição:', frase.lower().rfind('r'))

