'''Faça um programa queleia um número qualquer e mostre o seu fatorial.'''

num = int(input('digite um número inteiro: '))
cont = 1
fatorial = 1
while cont < num:
    fatorial = fatorial * (cont + 1)
    cont += 1

print(f'O fatorial de {num} é: {fatorial}.')
