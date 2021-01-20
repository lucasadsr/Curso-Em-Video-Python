'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão da PA, mostrando os 10 primeiros termos da progressão usando a estrutura While.'''

termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
n = 0
while n < 10:
    print(f'{termo}', end = '')
    print(', 'if n < 10 - 1 else '. ', end = '')
    termo += razão
    n += 1