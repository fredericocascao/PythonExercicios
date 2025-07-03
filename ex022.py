nome = input('Qual é o seu nome? ')

print('Seu nome em maiúscula é: ', nome.upper())  # converte o nome para maiúsculas
print('Seu nome em minúsculas é: ', nome.lower())  # converte o nome para minúsculas
print('O total de caracteres (sem espaços) é: ', len(''.join(nome.split()))) # remove espaços do nome

dividido = nome.split()
print('O tamanho do primeiro nome é: ', len(dividido[0]))  # divide o nome em uma lista de palavras

