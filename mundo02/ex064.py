'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

print('Digite 999 para parar o programa.')
n = int(input('Digite um número inteiro: '))
soma = n
total = 0
while n != 999:
    n = int(input('Digite outro número: '))
    soma += n
    total += 1
print(f'A soma dos números inteiros é de: {soma - 999}')
print(f'Foram utilizados {total} números.')