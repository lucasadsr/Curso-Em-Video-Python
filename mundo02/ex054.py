'''Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = ano - nasc
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'{maior} pessoas são maiores de idade\n'
      f'{menor} pessoas são menores de idade')
