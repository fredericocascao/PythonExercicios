frase = 'Teste de Caractere'

print(frase[9])
print(frase[9:13])  # fatiamento
print(frase[9:16:2])  # fatiamento com passo    

print(len(frase)) # tamanho da string
print(frase.count('e'))  # conta quantas vezes aparece o caractere 'e'
print(frase.count('e', 0, 13))  # conta quantas vezes aparece o caractere 'e' até a posição 13
print(frase.find('de'))  # encontra a posição da substring 'de'

print(frase.replace('Caractere', 'Texto'))  # substitui 'Caractere' por 'Texto'
print(frase.upper())  # converte a string para maiúsculas
print(frase.lower())  # converte a string para minúsculas
print(frase.capitalize())  # capitaliza a primeira letra da string
print(frase.title())  # capitaliza a primeira letra de cada palavra
print(frase.strip())  # remove espaços no início e no final da string
print(frase.rstrip())  # remove espaços no final da string
print(frase.lstrip())  # remove espaços no início da string
print(frase.split())  # divide a string em uma lista de palavras
print('-'.join(frase.split()))  # junta a lista de palavras em uma string, separando por espaço

