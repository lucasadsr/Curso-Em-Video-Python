'''Faça um programa que leia 3 números e mostre qual é o maior equal é o menor.'''

n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Digite um outro número qualquer: '))
n3 = float(input('Digite um outro número qualquer: '))

if n1 > n2 and n1 > n3:
    print(f'O maior é: {n1}')
else:
    if n2 > n1 and n2 > n3:
        print(f'O maior é: {n2}')
    else:
        print(f'O maior é: {n3}')

if n1 < n2 and n1 < n3:
    print(f'O menor é: {n1}')
else:
    if n2 < n1 and n2 < n3:
        print(f'O menor é: {n2}')
    else:
        print(f'O menor é: {n3}')
