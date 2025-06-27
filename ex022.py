nome = input('Qual é o seu nome? ')

print(nome.upper())  # converte o nome para maiúsculas
print(nome.lower())  # converte o nome para minúsculas
print(len(''.join(nome.split()))) # remove espaços do nome

dividido = nome.split()
print(len(dividido[0]))  # divide o nome em uma lista de palavras

