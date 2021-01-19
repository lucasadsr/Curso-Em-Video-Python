'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

print('-' * 14)
print('NÚMEROS PRIMOS')
print('-' * 14)
n = int(input('Digite um número inteiro: '))
cont = 0

for c in range(1, n + 1):
    if n % c == 0:
       cont = cont + 1

if cont == 2:
        print('O número é PRIMO')
else:
        print('O número não é PRIMO')