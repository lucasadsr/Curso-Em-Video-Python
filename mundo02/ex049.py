'''Refaça o desafio 009, mostraando a tabuada de um número que o usuário escolher, so que agora utilizando o laço for.'''

n = int(input('Digite um número para iniciar a tabuada: '))
print('-' * 14)
for c in range(1, 11):
    print(f'{n}  X  {c} = {c*n}')
print('-' * 14)