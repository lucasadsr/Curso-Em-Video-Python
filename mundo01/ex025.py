'''Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome.'''

nome = str(input('Digite seu nome: ').strip())
nomefind = 'SILVA' in nome.upper()
print(f'Existe Silva no seu nome? {nomefind}')
