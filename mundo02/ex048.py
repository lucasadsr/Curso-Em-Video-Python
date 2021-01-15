'''Faça um programna que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 300.'''

cont = 0
soma = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        cont += 1
        soma = soma + c
print(f'A soma dos {cont} npumeros é de: {soma}')
