'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.'''

nome = ' '
preco = barato = mil = total = cont = 0
opcao = ' '
maisbarato = ' '

while True:
    cont += 1
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    if preco > 1000:
        mil += 1
    total += preco
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S / N] ')).upper()
    if opcao == 'N':
        break
    opcao = ' '
    if cont == 1 or preco < barato:
        barato = preco
        maisbarato = nome

print('-' * 30)
print(f'O total foi de R${total}')
print(f'{mil} produtos custam mais que R$1000,00')
print(f'O mais barato é: {maisbarato}')
