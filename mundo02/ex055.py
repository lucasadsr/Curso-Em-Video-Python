'''Faça umprograma que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor pesos lidos.'''

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite seu peso: KG'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > menor:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}KG e o menor é {menor}KG.')
