'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

frase = str(input('Digite uma frase: ')).upper()
frasesemespaço = frase.replace(' ', '')
if frasesemespaço[:] == frasesemespaço[::-1]:
    print('É palindromo.')
else:
    print('Não é palindromo.')
