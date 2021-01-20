'''Escreva um program que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.'''

print('SEQUÊNCIA DE FIBONACCI')
n = int(input('Digite a quantidade de termos: '))
anterior = 0
atual = 1
termo = 2
if n == 1:
    print(f'{anterior}, ', end='')
if n > 1:
    print(f'{anterior}, ', end='')
    print(f'{atual}, ', end='')
while termo < n:
    soma = anterior + atual
    print(f'{soma}, ', end='')
    anterior = atual
    atual = soma
    termo += 1
print('FIM')