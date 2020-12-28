''' Crie um programa que leia o nome completo de uma pessoa e mostre:
a) O nome com todas as letras maiúsculas e minúsculas.
b) Quantas letras ao todo (sem considerar espaços).
c) Quantas letras tem o primeiro nome.'''

nome = str(input('Qual o seu nome? ')).strip()
print(nome.upper())
print(nome.lower())
espaços = nome.count(' ')
print(len(nome) - espaços)
print(len(nome.split()[0]))
