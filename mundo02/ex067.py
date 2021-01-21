'''Faça um programa que mostre a tabuada de vários números, um de cada vez, pera cada valor digitado pelo usuário. O programa será interrompido quando o número digitado for negativo.'''

while True:
    n = int(input('Digite um número para ver a tabuada: '))
    print('-' * 14)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n}  X  {c} = {c * n}')
print('FIM.')
