frase = input('Digite uma frase: ').strip()
print('A frase digitada foi:', frase)

print('A palavra "R" aparece {} vezes'.format(frase.lower().count('r')))
print('A primeira ocorrência de "R" está na posição:', frase.lower().find('r')+1)
print('A última ocorrência de "R" está na posição:', frase.lower().rfind('r')+1)

