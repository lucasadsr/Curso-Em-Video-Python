'''Melhore o DESAFIO 061, perguntando se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

a1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
termos = int(input('Quantos termos deseja ver? '))
n = a1

if razao != 0:
    while cont < termos:
        print(f'{a1}', end='')
        print(', ' if cont < termos - 1 else '.', end='')
        a1 = a1 + razao
        cont += 1
    acrescimo = 1
    while acrescimo != 0:
        acrescimo = int(input('\nDeseja acrescentar mais algum termo? '))
        cont = 0
        termos += acrescimo
        a1 = n
        while cont < termos:
            print(f'{a1}', end='')
            print(', ' if cont < termos - 1 else '.', end='')
            a1 = a1 + razao
            cont += 1
    print('\nPrograma encerrado.')
else:
    print('\nFim!')
