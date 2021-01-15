'''Desenvolva umprograma que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar desconsidere-o'''

soma = 0
for c in range(1, 7):
    i = int(input('Digite um valor: '))
    if i % 2 == 0:
        soma = soma + i
print(f'a soma dos pares é: {soma}')
