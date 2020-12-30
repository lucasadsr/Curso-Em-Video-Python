'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.'''

numero = int(input('Digite o número: '))

# gerando valor da unidade
unidade = numero % 10

# eliminando a unidade
numero = int((numero - unidade) / 10)

# gerando valor da dezena
dezena = numero % 10

# eliminando a dezena
numero = int((numero - dezena) / 10)

# gerando valor da centena
centena = numero % 10

# eliminando a centena
numero = int((numero - centena) / 10)

# gerando a milhar
milhar = numero % 10

print(f'unidade: {unidade}')
print(f'dezena: {dezena}')
print(f'centena: {centena}')
print(f'milhar: {milhar}')